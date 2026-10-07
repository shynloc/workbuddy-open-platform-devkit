#!/usr/bin/env python3
"""Validate one WorkBuddy asset package against WB-OPDK DERIVED JSON Schemas.

This complements (not replaces) the product-specific validators. JSON Schema
checks structural shape; product validators enforce cross-file consistency,
version gates, file existence, image constraints, and operational rules.
"""

from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]
SCHEMAS=ROOT/"schemas"

def schema(name):
    return json.loads((SCHEMAS/name).read_text("utf-8"))

def validate(instance, schema_name, label):
    s=schema(schema_name)
    Draft202012Validator.check_schema(s)
    errors=sorted(Draft202012Validator(s).iter_errors(instance),key=lambda e:list(e.path))
    if errors:
        print(f"SCHEMA FAILED: {label}")
        for e in errors:
            loc=".".join(map(str,e.path)) or "<root>"
            print(f"- {loc}: {e.message}")
        return False
    print(f"schema passed: {label}")
    return True

def load_json(path): return json.loads(path.read_text("utf-8"))

def frontmatter(path):
    text=path.read_text("utf-8")
    m=re.match(r"^---\n(.*?)\n---\n",text,re.S)
    if not m:
        raise ValueError(f"missing YAML frontmatter: {path}")
    return yaml.safe_load(m.group(1))

def detect(root):
    if (root/"SKILL.md").is_file():
        return "skill"
    p=root/".codebuddy-plugin"/"plugin.json"
    if p.is_file():
        d=load_json(p)
        return "expert-team" if d.get("expertType")=="team" else "expert"
    if (root/"connector-meta.json").is_file():
        return "connector"
    raise ValueError("cannot detect supported asset type")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("path")
    args=ap.parse_args()
    root=Path(args.path).resolve()

    if not root.is_dir():
        raise SystemExit("asset path must be a directory")

    try:
        typ=detect(root)
    except Exception as e:
        print(f"ERROR: {e}")
        return 1

    ok=True

    if typ=="skill":
        ok &= validate(frontmatter(root/"SKILL.md"),"skill-frontmatter.schema.json","SKILL.md frontmatter")

    elif typ in {"expert","expert-team"}:
        plugin=root/".codebuddy-plugin"/"plugin.json"
        ok &= validate(
            load_json(plugin),
            "expert-team-plugin.schema.json" if typ=="expert-team" else "expert-plugin.schema.json",
            "plugin.json"
        )
        for p in sorted((root/"agents").glob("*.md")) if (root/"agents").is_dir() else []:
            ok &= validate(frontmatter(p),"agent-frontmatter.schema.json",f"agent frontmatter: {p.name}")

    elif typ=="connector":
        meta=load_json(root/"connector-meta.json")
        ok &= validate(meta,"connector-meta.schema.json","connector-meta.json")
        ctype=meta.get("type","mcp")

        if ctype=="mcp" and (root/"mcp.json").is_file():
            ok &= validate(load_json(root/"mcp.json"),"mcp-config.schema.json","mcp.json")
        if ctype=="cli" and (root/"cli.json").is_file():
            ok &= validate(load_json(root/"cli.json"),"cli-config.schema.json","cli.json")
        if meta.get("auth_mode")=="token" and (root/"token-schema.json").is_file():
            ok &= validate(load_json(root/"token-schema.json"),"token-schema.schema.json","token-schema.json")

    return 0 if ok else 1

if __name__=="__main__":
    raise SystemExit(main())
