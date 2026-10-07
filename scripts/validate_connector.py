#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from pathlib import Path

def load(path: Path, errs: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        errs.append(f"invalid JSON {path.name}: {e}")
        return {}

def parse_version(v):
    if not v:
        return None
    m=re.fullmatch(r"(\d+)\.(\d+)\.(\d+)",str(v))
    return tuple(map(int,m.groups())) if m else None

def require_version(min_v, required, feature, errs):
    if min_v is None:
        errs.append(f"{feature} requires minWorkbuddyVersion >= {'.'.join(map(str,required))}")
    elif min_v < required:
        errs.append(
            f"{feature} requires minWorkbuddyVersion >= {'.'.join(map(str,required))}; "
            f"current={'.'.join(map(str,min_v))}"
        )

def has_path(obj, *keys):
    cur=obj
    for k in keys:
        if not isinstance(cur,dict) or k not in cur:
            return False
        cur=cur[k]
    return True

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

    version=meta.get("version")
    if version and not parse_version(version):
        errs.append(f"version is not semver: {version}")

    min_raw=meta.get("minWorkbuddyVersion")
    min_v=parse_version(min_raw) if min_raw else None
    if min_raw and min_v is None:
        errs.append(f"invalid minWorkbuddyVersion: {min_raw}")

    max_raw=meta.get("maxWorkbuddyVersion")
    if max_raw and not parse_version(max_raw):
        errs.append(f"invalid maxWorkbuddyVersion: {max_raw}")

    typ=meta.get("type","mcp")
    if typ not in {"mcp","cli","skill-only"}:
        errs.append(f"invalid type: {typ}")

    # Version-gated connector-meta fields.
    if any(k in meta for k in ["minWorkbuddyVersion","maxWorkbuddyVersion"]):
        require_version(min_v, (4,22,12), "min/maxWorkbuddyVersion", errs)

    if any(k in meta for k in ["name_zh","name_en","examples_zh","examples_en"]):
        require_version(min_v, (4,24,0), "name_zh/name_en/examples_zh/examples_en", errs)

    if any(k in meta for k in ["name_map","description_map"]):
        require_version(min_v, (5,2,0), "name_map/description_map", errs)

    if meta.get("examples_zh") is not None and not (2 <= len(meta["examples_zh"]) <= 5):
        errs.append("examples_zh should contain 2-5 examples")
    if meta.get("examples_en") is not None and not (2 <= len(meta["examples_en"]) <= 5):
        errs.append("examples_en should contain 2-5 examples")

    auth_mode=meta.get("auth_mode")
    if auth_mode=="token":
        require_version(min_v,(4,23,0),"auth_mode=token",errs)

    if typ=="mcp":
        mcp_p=root/"mcp.json"
        if not mcp_p.is_file():
            errs.append("missing mcp.json")
            mcp={}
        else:
            mcp=load(mcp_p,errs)

        servers=mcp.get("mcpServers",{}) if isinstance(mcp,dict) else {}
        if len(servers)!=1:
            errs.append("mcp.json must contain exactly one server")

        for server_name,server in servers.items():
            st=server.get("type")
            if st in {"sse","streamableHttp"} and not str(server.get("url","")).startswith("https://"):
                errs.append(f"remote MCP URL must use HTTPS: {server_name}")

            if any(k in server for k in ["cwd","disabledTools"]):
                require_version(min_v,(4,22,15),"MCP cwd/disabledTools",errs)
            if any(k in server for k in ["preAuth","runtime","staticEnv","staticHeaders"]):
                require_version(min_v,(5,0,0),"MCP preAuth/runtime/staticEnv/staticHeaders",errs)
            if "npmRegistries" in server:
                require_version(min_v,(4,24,0),"MCP npmRegistries",errs)
            if "npmRegistry" in server:
                # Supported earlier than npmRegistries.
                require_version(min_v,(4,22,0),"MCP npmRegistry",errs)

        if auth_mode=="token":
            schema_p=root/"token-schema.json"
            if not schema_p.is_file():
                errs.append("auth_mode=token requires token-schema.json")
            else:
                schema=load(schema_p,errs)
                for k in ["title","description","fields"]:
                    if not schema.get(k):
                        errs.append(f"token-schema missing field: {k}")

                fields=schema.get("fields",[]) if isinstance(schema,dict) else []
                keys=set()
                for i,f in enumerate(fields):
                    for k in ["key","label","type","required"]:
                        if k not in f:
                            errs.append(f"token-schema fields[{i}] missing {k}")
                    key=f.get("key")
                    if key:
                        keys.add(key)
                        if re.search(r"(TOKEN|SECRET|PASSWORD|API_?KEY|KEY)$", key, re.I) and f.get("type")!="password":
                            errs.append(f"sensitive field should use type=password: {key}")
                raw=mcp_p.read_text(encoding="utf-8") if mcp_p.is_file() else ""
                placeholders=set(re.findall(r"\$\{([A-Za-z_][A-Za-z0-9_]*)\}",raw))
                missing=placeholders-keys
                if missing:
                    errs.append(f"mcp placeholders missing from token schema: {sorted(missing)}")

    elif typ=="cli":
        cli_p=root/"cli.json"
        if not cli_p.is_file():
            errs.append("type=cli requires cli.json")
            cli={}
        else:
            cli=load(cli_p,errs)

        # WorkBuddy's CLI flow expects these lifecycle commands for authenticated CLIs.
        if "auth" in cli:
            for k in ["status","unAuth"]:
                if k not in cli:
                    errs.append(f"cli auth flow requires {k}")
            if "statusMatch" not in cli and "statusMatchJson" not in cli:
                errs.append("cli auth flow requires statusMatch or statusMatchJson")

        # init should at least support macOS and Linux for cross-platform connectors.
        if "init" in cli and isinstance(cli["init"],dict):
            for os_name in ["darwin","linux"]:
                if os_name not in cli["init"]:
                    errs.append(f"cli init missing {os_name}")

        if any(k in cli for k in ["runtime","npmRegistry","env","authWaitForExit","authQrModal"]):
            require_version(min_v,(4,22,0),"CLI runtime/npmRegistry/env/authWaitForExit/authQrModal",errs)
        if "authSuppressBrowser" in cli:
            require_version(min_v,(4,22,8),"CLI authSuppressBrowser",errs)
        if any(k in cli for k in ["statusMatchJson","versionCheck","npmRegistries"]):
            require_version(min_v,(4,24,0),"CLI statusMatchJson/versionCheck/npmRegistries",errs)
        if "authDeviceFlow" in cli:
            require_version(min_v,(5,0,0),"CLI authDeviceFlow",errs)
            if "authQrModal" in cli:
                errs.append("do not combine authDeviceFlow and authQrModal without explicit current official support")

        runtime=cli.get("runtime")
        if isinstance(runtime,dict) and runtime.get("type")=="python":
            require_version(min_v,(5,0,0),"CLI Python runtime",errs)

    # Basic icon presence check.
    icon_candidates=[root/"icon.svg",root/"icon.png",root/"icon.jpg",root/"icon.jpeg"]
    if not any(p.is_file() for p in icon_candidates):
        errs.append("missing connector icon (icon.svg/png/jpg)")

    # Never ship obvious local secrets.
    secret_names={".env",".env.local",".env.production","secrets.json","credentials.json"}
    for p in root.rglob("*"):
        if p.is_file() and p.name in secret_names:
            errs.append(f"possible secret file in package: {p.relative_to(root)}")

    if errs:
        print("CONNECTOR VALIDATION FAILED")
        for e in errs:
            print("-",e)
        return 1
    print("Connector validation passed")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
