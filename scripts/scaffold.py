#!/usr/bin/env python3
"""Create a new WorkBuddy asset from WB-OPDK starter templates."""

from __future__ import annotations
import argparse, shutil
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

REPLACEMENTS={
    "your-skill-name":"{name}",
    "your-expert-team":"{name}",
    "your-expert":"{name}",
    "your-service-token":"{name}",
    "your-service-oauth":"{name}",
    "your-cli-service":"{name}",
}

TEXT_EXT={".md",".json",".yaml",".yml",".txt",".svg",".toml",".ini"}

def replace_text(root: Path, name: str):
    for p in root.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in TEXT_EXT:
            continue
        text=p.read_text("utf-8")
        for old,new in REPLACEMENTS.items():
            text=text.replace(old,new.format(name=name))
        p.write_text(text,"utf-8")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("type",choices=sorted(TYPES))
    ap.add_argument("name",help="kebab-case asset name")
    ap.add_argument("output",help="destination directory")
    ap.add_argument("--force",action="store_true")
    args=ap.parse_args()

    src=TEMPLATES/TYPES[args.type]
    dst=Path(args.output).resolve()
    if not src.is_dir():
        raise SystemExit(f"template not found: {src}")
    if dst.exists():
        if not args.force:
            raise SystemExit(f"destination exists: {dst}; use --force to replace")
        shutil.rmtree(dst)

    shutil.copytree(src,dst)
    replace_text(dst,args.name)
    print(f"created {args.type}: {dst}")
    print("Next: edit metadata/content, add required visual assets, then run the matching validator.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
