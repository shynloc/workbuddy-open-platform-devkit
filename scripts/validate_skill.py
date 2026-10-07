#!/usr/bin/env python3
from __future__ import annotations
import argparse, re
from pathlib import Path

REQUIRED = ["description", "description_zh", "description_en", "version", "author"]

def parse_frontmatter(text: str):
    if not text.startswith("---\n"):
        return None, "missing YAML frontmatter"
    end = text.find("\n---\n", 4)
    if end < 0:
        return None, "unterminated YAML frontmatter"
    fm = {}
    for raw in text[4:end].splitlines():
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", raw)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip("\"'")
    return fm, None

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
                if not fm.get(k):
                    failures.append(f"missing frontmatter field: {k}")
            v = fm.get("version", "")
            if v and not re.fullmatch(r"\d+\.\d+\.\d+", v):
                failures.append(f"version is not semver: {v}")
        for ref in re.findall(r"@references/([^\s)\`]+)", text):
            if not (root / "references" / ref).exists():
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
