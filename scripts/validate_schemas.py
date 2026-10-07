#!/usr/bin/env python3
"""Check WB-OPDK schemas and validate representative starter files."""

from __future__ import annotations
import json, re
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]
SCHEMAS=ROOT/"schemas"
T=ROOT/"90-templates"

def check_schema(name):
    data=json.loads((SCHEMAS/name).read_text("utf-8"))
    Draft202012Validator.check_schema(data)
    print("schema OK:",name)
    return data

def validate(instance,schema,label):
    errors=sorted(Draft202012Validator(schema).iter_errors(instance),key=lambda e:list(e.path))
    if errors:
        print(f"FAILED: {label}")
        for e in errors:
            loc=".".join(map(str,e.path)) or "<root>"
            print(f"- {loc}: {e.message}")
        return False
    print("starter OK:",label)
    return True

def skill_frontmatter(path):
    text=path.read_text("utf-8")
    m=re.match(r"^---\n(.*?)\n---\n",text,re.S)
    if not m:
        raise ValueError("SKILL.md has no YAML frontmatter")
    return yaml.safe_load(m.group(1))

def load_json(path): return json.loads(path.read_text("utf-8"))

def main():
    skill=check_schema("skill-frontmatter.schema.json")
    expert=check_schema("expert-plugin.schema.json")
    team=check_schema("expert-team-plugin.schema.json")
    connector=check_schema("connector-meta.schema.json")
    token=check_schema("token-schema.schema.json")
    check_schema("release-manifest.schema.json")

    ok=True
    ok &= validate(skill_frontmatter(T/"skill-template"/"SKILL.md"),skill,"skill-template")
    ok &= validate(load_json(T/"expert-template"/".codebuddy-plugin"/"plugin.json"),expert,"expert-template")
    ok &= validate(load_json(T/"expert-team-template"/".codebuddy-plugin"/"plugin.json"),team,"expert-team-template")

    for name in ["connector-mcp-token-template","connector-mcp-oauth-template","connector-cli-template"]:
        ok &= validate(load_json(T/name/"connector-meta.json"),connector,name+"/connector-meta.json")
    ok &= validate(load_json(T/"connector-mcp-token-template"/"token-schema.json"),token,"connector token-schema")

    return 0 if ok else 1

if __name__=="__main__":
    raise SystemExit(main())
