#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from pathlib import Path

def load(path, errs):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        errs.append(f"invalid JSON {path.name}: {e}")
        return {}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("path")
    args=ap.parse_args()
    root=Path(args.path)
    errs=[]

    meta_p=root/"connector-meta.json"
    if not meta_p.is_file():
        errs.append("missing connector-meta.json")
        meta={}
    else:
        meta=load(meta_p,errs)

    for k in ["name","name_en","description","description_zh","description_en","source"]:
        if not meta.get(k):
            errs.append(f"missing connector-meta field: {k}")

    source=meta.get("source","")
    if source and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*",source):
        errs.append("source must be kebab-case")

    typ=meta.get("type","mcp")
    if typ not in {"mcp","cli","skill-only"}:
        errs.append(f"invalid type: {typ}")

    if meta.get("examples_zh") is not None and not (2 <= len(meta["examples_zh"]) <= 5):
        errs.append("examples_zh should contain 2-5 examples")
    if meta.get("examples_en") is not None and not (2 <= len(meta["examples_en"]) <= 5):
        errs.append("examples_en should contain 2-5 examples")

    if typ=="mcp":
        mcp_p=root/"mcp.json"
        if not mcp_p.is_file():
            errs.append("missing mcp.json")
        else:
            mcp=load(mcp_p,errs)
            servers=mcp.get("mcpServers",{})
            if len(servers)!=1:
                errs.append("mcp.json must contain exactly one server")
            for server in servers.values():
                if server.get("type") in {"sse","streamableHttp"} and not str(server.get("url","")).startswith("https://"):
                    errs.append("remote MCP URL must use HTTPS")

        if meta.get("auth_mode")=="token":
            schema_p=root/"token-schema.json"
            if not schema_p.is_file():
                errs.append("auth_mode=token requires token-schema.json")
            else:
                schema=load(schema_p,errs)
                fields=schema.get("fields",[])
                if not fields:
                    errs.append("token-schema fields must not be empty")
                keys={f.get("key") for f in fields}
                if mcp_p.is_file():
                    raw=mcp_p.read_text(encoding="utf-8")
                    placeholders=set(re.findall(r"\$\{([A-Za-z_][A-Za-z0-9_]*)\}",raw))
                    missing=placeholders-keys
                    if missing:
                        errs.append(f"mcp placeholders missing from token schema: {sorted(missing)}")

    elif typ=="cli" and not (root/"cli.json").is_file():
        errs.append("type=cli requires cli.json")

    if errs:
        print("CONNECTOR VALIDATION FAILED")
        for e in errs:
            print("-",e)
        return 1
    print("Connector validation passed")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
