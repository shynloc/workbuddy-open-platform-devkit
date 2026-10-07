#!/usr/bin/env python3
"""Create a real-world WorkBuddy validation record from the WB-OPDK template."""

from __future__ import annotations
import argparse, datetime, re, shutil
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TEMPLATE=ROOT/"95-validation"/"record-template.yaml"

def safe(s):
    return re.sub(r"[^A-Za-z0-9._-]+","-",s).strip("-").lower()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--type",required=True,choices=["skill","expert","expert-team","connector","buddy-app","third-party-app"])
    ap.add_argument("--name",required=True)
    ap.add_argument("--version",required=True)
    ap.add_argument("--output")
    args=ap.parse_args()

    out=Path(args.output or ROOT/"95-validation"/"records"/f"{safe(args.name)}-{safe(args.version)}.yaml")
    out.parent.mkdir(parents=True,exist_ok=True)
    if out.exists():
        raise SystemExit(f"record already exists: {out}")

    text=TEMPLATE.read_text("utf-8")
    text=text.replace("type: skill",f"type: {args.type}",1)
    text=text.replace("name: your-asset",f"name: {args.name}",1)
    text=text.replace("version: 1.0.0",f"version: {args.version}",1)
    text=text.replace('"YYYY-MM-DD"',f'"{datetime.date.today().isoformat()}"',1)
    out.write_text(text,"utf-8")
    print(out)
    return 0

if __name__=="__main__":
    raise SystemExit(main())
