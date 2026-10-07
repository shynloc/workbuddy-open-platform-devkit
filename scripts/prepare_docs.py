#!/usr/bin/env python3
"""Prepare a child docs_dir for MkDocs without changing the Agent-friendly repo layout."""

from __future__ import annotations
import shutil
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"build"/"docs"

ROOT_FILES=[
    "README.md",
    "START_HERE.md",
    "DEVELOPER_START.md",
    "ROADMAP.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "NOTICE.md",
    "COMPATIBILITY.md",
    "QUALITY_GATES.md",
    "SECURITY.md",
    "docs-site.md",
]
SOURCE_DIRS=[
    "00-platform",
    "05-qualification-compliance",
    "10-skill",
    "20-expert",
    "30-expert-team",
    "40-connector",
    "50-buddy-app",
    "55-hardware",
    "60-open-api",
    "65-security-governance",
    "70-release-engineering",
    "75-operations",
    "80-recipes",
    "90-templates",
    "95-validation",
    "schemas",
    "sources",
    "scripts",
    "examples",
]

def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    for name in ROOT_FILES:
        src=ROOT/name
        if src.exists():
            shutil.copy2(src,OUT/name)

    for name in SOURCE_DIRS:
        src=ROOT/name
        if src.exists():
            shutil.copytree(
                src,
                OUT/name,
                ignore=shutil.ignore_patterns("__pycache__","*.pyc",".DS_Store",".venv"),
            )

    subprocess.run([
        sys.executable,
        str(ROOT/"scripts"/"build_docs_dashboard.py"),
        "--output-dir",
        str(OUT/"_generated"),
    ],check=True,cwd=ROOT)

    print(f"prepared MkDocs source: {OUT}")
    return 0

if __name__=="__main__":
    raise SystemExit(main())