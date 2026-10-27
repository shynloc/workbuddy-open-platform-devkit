#!/usr/bin/env python3
"""Run the WB-OPDK pre-release pipeline for a packageable WorkBuddy asset.

Pipeline:
detect type -> validator -> external release manifest -> schema validation -> clean ZIP

Requires:
  python3 -m pip install -r requirements-dev.txt
"""

from __future__ import annotations
import argparse, hashlib, json, re, subprocess, sys
from pathlib import Path
from _skill_frontmatter import skill_identity

ROOT=Path(__file__).resolve().parents[1]
SCRIPTS=ROOT/"scripts"
SCHEMAS=ROOT/"schemas"

def run(args):
    print("$"," ".join(map(str,args)))
    p=subprocess.run(list(map(str,args)),cwd=ROOT)
    if p.returncode:
        raise SystemExit(p.returncode)

def parse_skill(path):
    return skill_identity(path/"SKILL.md")

def detect(path):
    if (path/"SKILL.md").is_file():
        n,v=parse_skill(path)
        return "skill",n,v,SCRIPTS/"validate_skill.py"
    p=path/".codebuddy-plugin"/"plugin.json"
    if p.is_file():
        d=json.loads(p.read_text("utf-8"))
        if d.get("expertType")=="team":
            return "expert-team",d.get("name",path.name),d.get("version","unknown"),SCRIPTS/"validate_expert_team.py"
        return "expert",d.get("name",path.name),d.get("version","unknown"),SCRIPTS/"validate_expert.py"
    p=path/"connector-meta.json"
    if p.is_file():
        d=json.loads(p.read_text("utf-8"))
        return "connector",d.get("source") or d.get("name",path.name),d.get("version","unknown"),SCRIPTS/"validate_connector.py"
    raise SystemExit("unsupported package: could not detect Skill/Expert/Expert Team/Connector")

def safe_name(s):
    return re.sub(r"[^A-Za-z0-9._-]+","-",s).strip("-") or "workbuddy-asset"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--dist",default="dist")
    ap.add_argument("--side-effect-review",choices=["pass","fail","not-applicable","not-run"],default="not-run")
    args=ap.parse_args()

    asset=Path(args.path).resolve()
    if not asset.is_dir():
        raise SystemExit("asset path must be a directory")

    try:
        typ,name,version,validator=detect(asset)
    except (ValueError, OSError) as exc:
        raise SystemExit(f"Invalid package metadata: {exc}")
    dist=Path(args.dist).resolve()
    dist.mkdir(parents=True,exist_ok=True)
    base=f"{safe_name(name)}-v{safe_name(version)}"
    manifest=dist/f"{base}.manifest.json"
    archive=dist/f"{base}.zip"
    submission=dist/f"{base}.submission-notes.md"

    run([sys.executable,SCRIPTS/"validate_asset_schemas.py",asset])
    run([sys.executable,validator,asset])

    run([
        sys.executable,SCRIPTS/"generate_release_manifest.py",asset,
        "--type",typ,
        "--name",name,
        "--version",version,
        "--validator",str(validator.relative_to(ROOT)),
        "--validation-status","pass",
        "--side-effect-review",args.side_effect_review,
        "--output",manifest
    ])

    run([
        sys.executable,SCRIPTS/"validate_json_schema.py",
        manifest,SCHEMAS/"release-manifest.schema.json"
    ])

    run([sys.executable,SCRIPTS/"pack_release.py",asset,"--out",archive])
    run([sys.executable,SCRIPTS/"validate_release_zip.py",archive,"--type",typ,"--source",asset])

    run([
        sys.executable,SCRIPTS/"generate_submission_notes.py",asset,
        "--output",submission
    ])

    summary={
        "type":typ,
        "name":name,
        "version":version,
        "manifest":str(manifest),
        "archive":str(archive),
        "archive_sha256":hashlib.sha256(archive.read_bytes()).hexdigest(),
        "archive_validation":"pass",
        "submission_notes":str(submission),
        "status":"ready-for-platform-parse-and-runtime-test"
    }
    print(json.dumps(summary,ensure_ascii=False,indent=2))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
