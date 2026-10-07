#!/usr/bin/env python3
"""Lightweight structural validator for WB-OPDK knowledge-page metadata."""

from __future__ import annotations
import re
from pathlib import Path

VALID_TYPES = {"OFFICIAL", "DERIVED", "OBSERVED", "EXPERIMENTAL"}
VALID_STATUS = {"VERIFIED", "STALE", "DEPRECATED"}
EXCLUDED_TOP_LEVEL = {"80-recipes", "90-templates"}


def frontmatter(text: str):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    block = text[4:end]
    out = {}
    for line in block.splitlines():
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def main():
    root = Path(".")
    failures = []
    checked = 0

    for path in root.glob("[0-9][0-9]-*/**/*.md"):
        if path.parts and path.parts[0] in EXCLUDED_TOP_LEVEL:
            # Recipes and distribution templates have their own schemas and
            # validators. Do not confuse their YAML with KB metadata.
            continue
        if path.name == "README.md":
            continue

        fm = frontmatter(path.read_text(encoding="utf-8"))
        if fm is None:
            # Operational checklists may intentionally omit KB metadata.
            continue

        checked += 1
        for key in ("title", "knowledge_type", "last_verified", "status"):
            if not fm.get(key):
                failures.append(f"{path}: missing {key}")

        if fm.get("knowledge_type") not in VALID_TYPES:
            failures.append(f"{path}: invalid knowledge_type={fm.get('knowledge_type')}")
        if fm.get("status") not in VALID_STATUS:
            failures.append(f"{path}: invalid status={fm.get('status')}")

    print(f"checked {checked} metadata documents")
    if failures:
        print("\n".join(failures))
        return 1

    print("KB metadata validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
