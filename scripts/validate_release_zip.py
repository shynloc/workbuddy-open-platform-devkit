#!/usr/bin/env python3
"""Validate the actual archive for an explicitly selected WorkBuddy asset type.

WB-OPDK accepts a logical root at ZIP root or under one wrapper directory.
The packer emits one wrapper. This is a local static profile, not a platform upload.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import sys
import tempfile
import zipfile
from jsonschema import Draft202012Validator

from _package_files import include, SKIP_NAMES, SKIP_PARTS, SKIP_SUFFIX
from _skill_frontmatter import read_frontmatter

SCRIPTS = Path(__file__).resolve().parent
TYPES = ('skill', 'expert', 'expert-team', 'connector')
MARKERS = {'skill': 'SKILL.md', 'expert': '.codebuddy-plugin/plugin.json',
           'expert-team': '.codebuddy-plugin/plugin.json', 'connector': 'connector-meta.json'}


def run_check(script, root):
    process = subprocess.run([sys.executable, str(SCRIPTS/script), str(root)],
                             text=True, capture_output=True, encoding='utf-8',
                             env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    if process.returncode:
        raise ValueError(process.stdout.strip() or process.stderr.strip() or f'{script} failed')


def confined_path(root, relative):
    if not isinstance(relative, str) or '\\' in relative or not relative:
        raise ValueError(f'invalid package-relative path: {relative!r}')
    if PurePosixPath(relative).is_absolute() or '..' in PurePosixPath(relative).parts:
        raise ValueError(f'path escapes package root: {relative}')
    path = (root/relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f'path escapes package root: {relative}')
    if not path.exists():
        raise ValueError(f'missing declared path: {relative}')
    current = root
    for part in PurePosixPath(relative).parts:
        if part not in {child.name for child in current.iterdir()}:
            raise ValueError(f'path case does not match ZIP entries: {relative}')
        current = current/part
    return path


def validate_source(root, asset_type):
    marker = root/MARKERS[asset_type]
    if not marker.is_file():
        hint = ' Check the upload asset type and remove extra wrapper directories.'
        if asset_type in ('expert', 'expert-team'):
            hint += ' A native Skill belongs in the Skill entry, not Configure Expert.'
        raise ValueError(f'missing {MARKERS[asset_type]} at package root.{hint}')
    present = [name for name in set(MARKERS.values()) if (root/name).is_file()]
    if len(present) != 1:
        raise ValueError('ambiguous package root: multiple asset markers; choose the correct asset type and upload entry')
    run_check('validate_asset_schemas.py', root)
    if asset_type == 'skill':
        for reference in re.findall(r'@references/([^\s)`]+)', marker.read_text('utf-8')):
            confined_path(root, 'references/'+reference)
    if asset_type in ('expert', 'expert-team'):
        if asset_type == 'expert-team':
            confined_path(root, 'settings.json')
        data = json.loads(marker.read_text('utf-8'))
        expected = 'team' if asset_type == 'expert-team' else 'agent'
        if data.get('expertType') != expected:
            raise ValueError(f'expected expertType {expected} for {asset_type}')
        paths = list(data.get('agents', []))
        paths += [data['avatar']] if data.get('avatar') else []
        paths += [m['avatar'] for m in data.get('members', []) if m.get('avatar')]
        for relative in paths:
            confined_path(root, relative)
        agent_schema = json.loads((SCRIPTS.parent/'schemas/agent-frontmatter.schema.json').read_text('utf-8'))
        for relative in data.get('agents', []):
            agent = confined_path(root, relative)
            fields = read_frontmatter(agent)
            errors = list(Draft202012Validator(agent_schema).iter_errors(fields))
            if errors:
                raise ValueError(f'invalid declared Agent frontmatter {relative}: {errors[0].message}')
            if fields['name'] != agent.stem:
                raise ValueError(f'Agent name must match filename: {relative}')
        dependencies = data.get('dependencies') or {}
        if not isinstance(dependencies, dict):
            raise ValueError('plugin dependencies must be an object')
        mcp_paths = dependencies.get('mcpServers', [])
        if isinstance(mcp_paths, str):
            mcp_paths = [mcp_paths]
        if not isinstance(mcp_paths, list) or not all(isinstance(p, str) for p in mcp_paths):
            raise ValueError('dependencies.mcpServers must be a file path or array of file paths')
        if not mcp_paths and (root/'.mcp.json').exists():
            mcp_paths = ['.mcp.json']
        for relative in mcp_paths:
            config = json.loads(confined_path(root, relative).read_text('utf-8'))
            if not isinstance(config, dict):
                raise ValueError(f'MCP configuration must be a JSON object: {relative}')
        for relative in data.get('skills', []):
            confined_path(root, relative)
            skill = confined_path(root, relative.rstrip('/')+'/SKILL.md')
            # Embedded plugin skills are not assumed to be standalone marketplace submissions.
            read_frontmatter(skill)
            for reference in re.findall(r'@references/([^\s)`]+)', skill.read_text('utf-8')):
                confined_path(skill.parent, 'references/'+reference)
    if asset_type == 'connector':
        data = json.loads(marker.read_text('utf-8'))
        for name in ('mcp.json', 'cli.json', 'token-schema.json'):
            if (root/name).exists():
                confined_path(root, name)
        if data.get('icon'):
            confined_path(root, data['icon'])
    run_check({'skill': 'validate_skill.py', 'expert': 'validate_expert.py',
               'expert-team': 'validate_expert_team.py', 'connector': 'validate_connector.py'}[asset_type], root)


def validate_archive(archive, asset_type, source=None):
    with zipfile.ZipFile(archive) as package, tempfile.TemporaryDirectory(prefix='wb-zip-check-') as tmp:
        seen = set()
        members = []
        for info in package.infolist():
            name = info.filename
            parts = PurePosixPath(name).parts
            if (not parts or name.startswith('/') or '\\' in name or ':' in name
                    or any(p in ('', '.', '..') for p in name.rstrip('/').split('/'))):
                raise ValueError(f'unsafe ZIP path: {name}')
            if any(p.endswith(('.', ' ')) or re.search(r'[<>|"?*\x00-\x1f]', p)
                   or re.fullmatch(r'(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9]|CONIN\$|CONOUT\$)(\..*)?', p, re.I)
                   for p in parts):
                raise ValueError(f'non-portable ZIP path (Windows normalization): {name}')
            if name.rstrip('/').casefold() in seen:
                raise ValueError(f'duplicate or case-colliding ZIP path: {name}')
            seen.add(name.rstrip('/').casefold())
            if stat.S_ISLNK(info.external_attr >> 16):
                raise ValueError(f'symlink in ZIP: {name}')
            if (any(p in SKIP_PARTS or p == '__MACOSX' for p in parts)
                    or parts[-1] in SKIP_NAMES or parts[-1].startswith('.env')
                    or PurePosixPath(name).suffix in SKIP_SUFFIX):
                raise ValueError(f'temporary/private file in ZIP: {name}')
            if not info.is_dir():
                members.append(name)
        if not members:
            raise ValueError('empty ZIP')
        marker = MARKERS[asset_type]
        prefix = ''
        if marker not in members:
            first = {name.split('/')[0] for name in members}
            if len(first) != 1:
                raise ValueError(f'missing {marker} at ZIP logical root; mixed assets or wrong upload type')
            prefix = next(iter(first))+'/'
            if prefix+marker not in members:
                raise ValueError(f'missing {marker} after one wrapper; wrong asset type, omitted hidden manifest, or extra nesting')
        package.extractall(tmp)
        unpacked = {p.relative_to(tmp).as_posix() for p in Path(tmp).rglob('*') if p.is_file()}
        if unpacked != set(members) or any(
                hashlib.sha256((Path(tmp)/name).read_bytes()).digest()
                != hashlib.sha256(package.read(name)).digest() for name in members):
            raise ValueError('extraction changed ZIP paths or bytes')
        root = Path(tmp)/prefix
        validate_source(root, asset_type)
        if source is not None:
            source = Path(source).resolve()
            expected = {p.relative_to(source).as_posix(): p.read_bytes()
                        for p in source.rglob('*') if include(p, source)}
            actual = {name[len(prefix):]: package.read(name) for name in members}
            if actual != expected:
                raise ValueError('ZIP content differs from the filtered source directory (file list or bytes)')
    return hashlib.sha256(Path(archive).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive')
    parser.add_argument('--type', required=True, choices=TYPES)
    parser.add_argument('--source', help='Also compare file inventory and bytes to the source directory')
    args = parser.parse_args()
    try:
        digest = validate_archive(Path(args.archive), args.type, args.source)
    except (ValueError, OSError, zipfile.BadZipFile, RuntimeError) as exc:
        print(f'ZIP VALIDATION FAILED: {exc}')
        return 1
    print(f'ZIP validation passed ({args.type}); sha256={digest}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
