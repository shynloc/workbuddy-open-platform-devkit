#!/usr/bin/env python3
"""Validate WB-OPDK official source registry and downstream impact mapping."""

from __future__ import annotations
import argparse, json, re
from pathlib import Path

import yaml

ROOT=Path(__file__).resolve().parents[1]
REGISTRY=ROOT/"sources"/"official-sources.yaml"
IMPACT=ROOT/"sources"/"source-impact-map.json"

DATE_RE=re.compile(r"^\d{4}-\d{2}-\d{2}$")

EXCLUDED_TOP_LEVEL={"80-recipes","90-templates"}

def iter_kb_markdown():
    for top in ROOT.iterdir():
        if not top.is_dir() or not re.fullmatch(r"\d{2}-.+",top.name):
            continue
        if top.name in EXCLUDED_TOP_LEVEL:
            continue
        for p in top.rglob("*.md"):
            yield p

def frontmatter(path: Path):
    text=path.read_text("utf-8",errors="replace")
    if not text.startswith("---\n"):
        return {}
    end=text.find("\n---\n",4)
    if end<0:
        return {}
    data=yaml.safe_load(text[4:end]) or {}
    return data if isinstance(data,dict) else {}

def path_exists(pattern: str):
    if "*" in pattern or "?" in pattern or "[" in pattern:
        return any(ROOT.glob(pattern))
    p=ROOT/pattern
    if pattern.endswith("/"):
        return p.is_dir()
    return p.exists()

def main():
    ap=argparse.ArgumentParser()
    ap.parse_args()

    failures=[]
    registry=yaml.safe_load(REGISTRY.read_text("utf-8")) or {}
    sources=registry.get("sources") or {}
    if not isinstance(sources,dict) or not sources:
        failures.append("official-sources.yaml has no sources mapping")
        sources={}

    for sid,row in sources.items():
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*",sid):
            failures.append(f"invalid source id: {sid}")
        if not isinstance(row,dict):
            failures.append(f"{sid}: source entry must be an object")
            continue
        for key in ("title","url","authority","category","last_verified"):
            if not row.get(key):
                failures.append(f"{sid}: missing {key}")
        if row.get("authority")!="official":
            failures.append(f"{sid}: authority should be official")
        if row.get("url") and not str(row["url"]).startswith("https://open.workbuddy.cn/"):
            failures.append(f"{sid}: unexpected official URL host: {row['url']}")
        if row.get("last_verified") and not DATE_RE.fullmatch(str(row["last_verified"])):
            failures.append(f"{sid}: invalid last_verified date")

    impact=json.loads(IMPACT.read_text("utf-8"))
    mappings=impact.get("sources") or {}
    for sid in sources:
        if sid not in mappings:
            failures.append(f"{sid}: missing source-impact mapping")
            continue
        affected=mappings[sid].get("affected") or []
        if not affected:
            failures.append(f"{sid}: impact mapping has no affected paths")
        for pattern in affected:
            if not path_exists(pattern):
                failures.append(f"{sid}: affected path does not resolve: {pattern}")

    for sid in mappings:
        if sid not in sources:
            failures.append(f"impact map references unknown source: {sid}")

    for p in iter_kb_markdown():
        fm=frontmatter(p)
        if not fm:
            continue
        refs=fm.get("official_sources") or []
        if isinstance(refs,str):
            refs=[refs]
        kt=fm.get("knowledge_type")
        if kt in {"OFFICIAL","DERIVED"} and not refs:
            failures.append(f"{p.relative_to(ROOT)}: {kt} document has no official_sources")
        for sid in refs:
            if sid not in sources:
                failures.append(f"{p.relative_to(ROOT)}: unknown official source id {sid}")

    print(f"registered official sources: {len(sources)}")
    print(f"impact mappings: {len(mappings)}")

    if failures:
        print("SOURCE REGISTRY VALIDATION FAILED")
        for x in failures:
            print("-",x)
        return 1

    print("Official source registry and impact map validation passed")
    return 0

if __name__=="__main__":
    raise SystemExit(main())