#!/usr/bin/env python3
"""Run the WB-OPDK pre-release pipeline for a packageable WorkBuddy asset.

Pipeline:
detect type -> validator -> external release manifest -> schema validation -> clean ZIP

Requires:
  python3 -m pip install -r requirements-dev.txt
"""

from __future__ import annotations
import argparse, json, re, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SCRIPTS=ROOT/"scripts"
SCHEMAS=ROOT/"schemas"

def run(args):
    print("$"," ".join(map(str,args)))
    p=subprocess.run(list(map(str,args)),cwd=ROOT)
    if p.returncode:
        raise SystemExit(p.returncode)

def parse_skill(path):
    text=(path/"SKILL.md").read_text("utf-8")
    def f(k):
        m=re.search(rf"(?m)^{re.escape(k)}:\s*[\"']?([^\n\"']+)",text)
        return m.group(1).strip() if m else None
    return f("name") or path.name, f("version") or "unknown"

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

    typ,name,version,validator=detect(asset)
    dist=Path(args.dist).resolve()
    dist.mkdir(parents=True,exist_ok=True)
    base=f"{safe_name(name)}-v{safe_name(version)}"
    manifest=dist/f"{base}.manifest.json"
    archive=dist/f"{base}.zip"

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

    summary={
        "type":typ,
        "name":name,
        "version":version,
        "manifest":str(manifest),
        "archive":str(archive),
        "status":"ready-for-platform-parse-and-runtime-test"
    }
    print(json.dumps(summary,ensure_ascii=False,indent=2))
    return 0

if __name__=="__main__":
    raise SystemExit(main())