#!/usr/bin/env python3
"""Create a new WorkBuddy asset from WB-OPDK starter templates."""

from __future__ import annotations
import argparse, re, shutil
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TEMPLATES=ROOT/"90-templates"

TYPES={
    "skill":"skill-template",
    "expert":"expert-template",
    "expert-team":"expert-team-template",
    "connector-token":"connector-mcp-token-template",
    "connector-oauth":"connector-mcp-oauth-template",
    "connector-cli":"connector-cli-template",
    "buddy-app":"buddy-app-template",
}

TEXT_EXT={".md",".json",".yaml",".yml",".txt",".svg",".toml",".ini"}

def replacements(name: str):
    # Longest/specific placeholders first.
    return [
        ("your-expert-team",name),
        ("your-service-token",name),
        ("your-service-oauth",name),
        ("your-cli-service",name),
        ("your-skill-name",name),
        ("your-expert",name),
        ("connector-usage",f"{name}-usage"),
        ("cli-usage",f"{name}-usage"),
        ("your-service",name),
        ("your-cli",name),
    ]

def replace_content(root: Path, name: str):
    pairs=replacements(name)
    for p in root.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in TEXT_EXT:
            continue
        text=p.read_text("utf-8")
        for old,new in pairs:
            text=text.replace(old,new)
        p.write_text(text,"utf-8")

def rename_paths(root: Path, name: str):
    pairs=replacements(name)
    # Deepest paths first so child renames happen before parent directories.
    paths=sorted(root.rglob("*"),key=lambda p:len(p.parts),reverse=True)
    for p in paths:
        new_name=p.name
        for old,new in pairs:
            new_name=new_name.replace(old,new)
        if new_name!=p.name:
            target=p.with_name(new_name)
            if target.exists():
                raise RuntimeError(f"scaffold rename collision: {p} -> {target}")
            p.rename(target)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("type",choices=sorted(TYPES))
    ap.add_argument("name",help="kebab-case asset name")
    ap.add_argument("output",help="destination directory")
    ap.add_argument("--force",action="store_true")
    args=ap.parse_args()

    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*",args.name):
        raise SystemExit("name must be lowercase kebab-case")

    src=TEMPLATES/TYPES[args.type]
    dst=Path(args.output).resolve()
    if not src.is_dir():
        raise SystemExit(f"template not found: {src}")
    if dst.exists():
        if not args.force:
            raise SystemExit(f"destination exists: {dst}; use --force to replace")
        shutil.rmtree(dst)

    shutil.copytree(src,dst)
    replace_content(dst,args.name)
    rename_paths(dst,args.name)

    print(f"created {args.type}: {dst}")
    print("Next: edit product-specific metadata/content, add required visual assets, then run the matching validator.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
