#!/usr/bin/env python3
from __future__ import annotations
import argparse, re
from pathlib import Path
from _skill_frontmatter import parse_frontmatter

REQUIRED = [
    "name",
    "display_name",
    "display_name_en",
    "description",
    "description_zh",
    "description_en",
    "version",
    "author",
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="Skill root directory")
    args = ap.parse_args()
    root = Path(args.path)
    failures = []
    skill = root / "SKILL.md"
    if not skill.is_file():
        failures.append("missing SKILL.md")
    else:
        text = skill.read_text(encoding="utf-8")
        fm, err = parse_frontmatter(text)
        if err:
            failures.append(err)
        else:
            for k in REQUIRED:
                if not isinstance(fm.get(k), str) or not fm[k].strip():
                    failures.append(f"missing or invalid frontmatter field: {k} (non-empty string required)")
            v = fm.get("version", "")
            if isinstance(v, str) and v and not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", v):
                failures.append(f"version is not semver: {v}")
        for ref in re.findall(r"@references/([^\s)\`]+)", text):
            referenced = (root / "references" / ref).resolve()
            if not referenced.is_relative_to(root.resolve()) or not referenced.is_file():
                failures.append(f"missing reference: references/{ref}")
    for p in root.rglob("*"):
        if p.is_file() and (p.name == ".DS_Store" or p.suffix == ".pyc" or "__pycache__" in p.parts):
            failures.append(f"temporary file in package: {p.relative_to(root)}")
    if failures:
        print("SKILL VALIDATION FAILED")
        for x in failures:
            print("-", x)
        return 1
    print("Skill validation passed")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
