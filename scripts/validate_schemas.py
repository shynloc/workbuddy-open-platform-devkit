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

def md_frontmatter(path):
    text=path.read_text("utf-8")
    m=re.match(r"^---\n(.*?)\n---\n",text,re.S)
    if not m:
        raise ValueError(f"{path} has no YAML frontmatter")
    return yaml.safe_load(m.group(1))

def load_json(path): return json.loads(path.read_text("utf-8"))

def main():
    skill=check_schema("skill-frontmatter.schema.json")
    agent=check_schema("agent-frontmatter.schema.json")
    expert=check_schema("expert-plugin.schema.json")
    team=check_schema("expert-team-plugin.schema.json")
    connector=check_schema("connector-meta.schema.json")
    mcp=check_schema("mcp-config.schema.json")
    cli=check_schema("cli-config.schema.json")
    token=check_schema("token-schema.schema.json")
    check_schema("release-manifest.schema.json")
    check_schema("validation-record.schema.json")

    ok=True

    # Skill.
    ok &= validate(md_frontmatter(T/"skill-template"/"SKILL.md"),skill,"skill-template")

    # Expert.
    ok &= validate(
        load_json(T/"expert-template"/".codebuddy-plugin"/"plugin.json"),
        expert,
        "expert-template/plugin.json"
    )
    ok &= validate(
        md_frontmatter(T/"expert-template"/"agents"/"your-expert.md"),
        agent,
        "expert-template agent frontmatter"
    )

    # Expert Team.
    ok &= validate(
        load_json(T/"expert-team-template"/".codebuddy-plugin"/"plugin.json"),
        team,
        "expert-team-template/plugin.json"
    )
    for p in sorted((T/"expert-team-template"/"agents").glob("*.md")):
        ok &= validate(md_frontmatter(p),agent,f"expert-team agent frontmatter: {p.name}")

    # Connector metadata.
    connector_names=[
        "connector-mcp-token-template",
        "connector-mcp-oauth-template",
        "connector-cli-template",
    ]
    for name in connector_names:
        ok &= validate(
            load_json(T/name/"connector-meta.json"),
            connector,
            name+"/connector-meta.json"
        )

    # MCP configs.
    for name in ["connector-mcp-token-template","connector-mcp-oauth-template"]:
        ok &= validate(load_json(T/name/"mcp.json"),mcp,name+"/mcp.json")

    # CLI config.
    ok &= validate(
        load_json(T/"connector-cli-template"/"cli.json"),
        cli,
        "connector-cli-template/cli.json"
    )

    # Token form.
    ok &= validate(
        load_json(T/"connector-mcp-token-template"/"token-schema.json"),
        token,
        "connector token-schema"
    )

    return 0 if ok else 1

if __name__=="__main__":
    raise SystemExit(main())