#!/usr/bin/env python3
"""Validate all WB-OPDK real-world validation YAML records."""

from __future__ import annotations
import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]
SCHEMA=json.loads((ROOT/"schemas"/"validation-record.schema.json").read_text("utf-8"))
RECORDS=ROOT/"95-validation"/"records"

def main():
    Draft202012Validator.check_schema(SCHEMA)
    if not RECORDS.exists():
        print("no validation records directory yet")
        return 0

    failures=[]
    count=0
    for p in sorted(RECORDS.glob("*.yaml")):
        count+=1
        data=yaml.safe_load(p.read_text("utf-8"))
        errors=sorted(Draft202012Validator(SCHEMA).iter_errors(data),key=lambda e:list(e.path))
        for e in errors:
            loc=".".join(map(str,e.path)) or "<root>"
            failures.append(f"{p.relative_to(ROOT)}:{loc}: {e.message}")

    print(f"checked {count} validation records")
    if failures:
        print("\n".join("ERROR: "+x for x in failures))
        return 1
    print("real-world validation records passed schema validation")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
