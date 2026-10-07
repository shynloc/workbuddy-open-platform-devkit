#!/usr/bin/env python3
"""Validate a JSON or YAML document against a JSON Schema."""

from __future__ import annotations
import argparse, json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

def load(path: Path):
    text=path.read_text("utf-8")
    if path.suffix.lower() in {".yaml",".yml"}:
        return yaml.safe_load(text)
    return json.loads(text)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("instance")
    ap.add_argument("schema")
    args=ap.parse_args()

    instance_path=Path(args.instance)
    schema_path=Path(args.schema)
    schema=load(schema_path)
    Draft202012Validator.check_schema(schema)
    validator=Draft202012Validator(schema,format_checker=FormatChecker())

    errors=sorted(validator.iter_errors(load(instance_path)), key=lambda e:list(e.path))
    if errors:
        print("SCHEMA VALIDATION FAILED")
        for e in errors:
            loc=".".join(map(str,e.path)) or "<root>"
            print(f"- {loc}: {e.message}")
        return 1
    print(f"Schema validation passed: {instance_path} <- {schema_path}")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
