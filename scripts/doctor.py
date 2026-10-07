#!/usr/bin/env python3
"""Run the WB-OPDK local working-grade health checks."""

from __future__ import annotations
import argparse, json, shutil, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SCRIPTS=ROOT/"scripts"

CHECKS=[
    ("KB metadata", [sys.executable, SCRIPTS/"validate_kb.py"]),
    ("Official source registry", [sys.executable, SCRIPTS/"validate_source_registry.py"]),
    ("Schemas and starters", [sys.executable, SCRIPTS/"validate_schemas.py"]),
    ("Real-world validation records", [sys.executable, SCRIPTS/"validate_validation_records.py"]),
    ("Starter/scaffold smoke tests", [sys.executable, SCRIPTS/"smoke_test_templates.py"]),
]

def run(label,cmd):
    p=subprocess.run(list(map(str,cmd)),cwd=ROOT,text=True,capture_output=True)
    return {
        "label":label,
        "status":"pass" if p.returncode==0 else "fail",
        "returncode":p.returncode,
        "stdout":p.stdout.strip(),
        "stderr":p.stderr.strip(),
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--online",action="store_true",help="Also compare current official sources with the committed baseline.")
    ap.add_argument("--docs",action="store_true",help="Also build the MkDocs site; requires docs dependencies.")
    ap.add_argument("--json",action="store_true")
    args=ap.parse_args()

    checks=list(CHECKS)

    if args.online:
        checks.append((
            "Official source baseline",
            [
                sys.executable,
                SCRIPTS/"check_official_sources.py",
                "--baseline",ROOT/"sources"/"source-baseline.json",
                "--fail-on-change",
            ],
        ))

    if args.docs:
        checks.append(("Prepare docs",[sys.executable,SCRIPTS/"prepare_docs.py"]))
        if shutil.which("mkdocs"):
            checks.append(("Build MkDocs",["mkdocs","build"]))
        else:
            print("mkdocs is not installed; run make setup first.",file=sys.stderr)
            return 2

    results=[]
    for label,cmd in checks:
        result=run(label,cmd)
        results.append(result)
        if not args.json:
            marker="PASS" if result["status"]=="pass" else "FAIL"
            print(f"[{marker}] {label}")
            if result["status"]=="fail":
                if result["stdout"]: print(result["stdout"])
                if result["stderr"]: print(result["stderr"],file=sys.stderr)

    summary={
        "status":"pass" if all(x["status"]=="pass" for x in results) else "fail",
        "checks":[{"label":x["label"],"status":x["status"],"returncode":x["returncode"]} for x in results],
    }

    if args.json:
        print(json.dumps(summary,ensure_ascii=False,indent=2))
    else:
        print(f"WB-OPDK doctor: {summary['status'].upper()}")

    return 0 if summary["status"]=="pass" else 1

if __name__=="__main__":
    raise SystemExit(main())
