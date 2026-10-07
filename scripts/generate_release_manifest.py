#!/usr/bin/env python3
"""Generate a reproducible WB-OPDK release-manifest.json for an asset directory."""

from __future__ import annotations
import argparse, datetime, hashlib, json, re, subprocess
from pathlib import Path

SKIP_PARTS={".git","__pycache__",".pytest_cache",".mypy_cache",".venv","node_modules","build","dist"}
SKIP_NAMES={".DS_Store","Thumbs.db","release-manifest.json"}
SKIP_SUFFIX={".pyc",".log"}

def files(root):
    for p in sorted(root.rglob("*")):
        rel=p.relative_to(root)
        if not p.is_file(): continue
        if any(x in SKIP_PARTS for x in rel.parts): continue
        if p.name in SKIP_NAMES or p.suffix.lower() in SKIP_SUFFIX: continue
        yield p,rel

def sha256(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()

def semver_from_skill(path):
    text=path.read_text("utf-8")
    def field(name):
        m=re.search(rf"(?m)^{re.escape(name)}:\s*[\"']?([^\n\"']+)",text)
        return m.group(1).strip() if m else None
    return field("name"),field("version")

def detect(root):
    if (root/"SKILL.md").is_file():
        n,v=semver_from_skill(root/"SKILL.md")
        return "skill",n or root.name,v or "unknown"
    p=root/".codebuddy-plugin"/"plugin.json"
    if p.is_file():
        d=json.loads(p.read_text("utf-8"))
        typ="expert-team" if d.get("expertType")=="team" else "expert"
        return typ,d.get("name",root.name),d.get("version","unknown")
    p=root/"connector-meta.json"
    if p.is_file():
        d=json.loads(p.read_text("utf-8"))
        return "connector",d.get("source") or d.get("name") or root.name,d.get("version","unknown")
    return None,root.name,"unknown"

def git_commit(root):
    try:
        return subprocess.check_output(
            ["git","-C",str(root),"rev-parse","HEAD"],stderr=subprocess.DEVNULL,text=True
        ).strip()
    except Exception:
        return None

def registry_date(repo_root):
    p=repo_root/"sources"/"official-sources.yaml"
    if not p.is_file(): return None
    m=re.search(r"(?m)^last_registry_review:\s*(\S+)",p.read_text("utf-8"))
    return m.group(1) if m else None

def secret_scan(root):
    suspicious=[]
    names={".env",".env.local",".env.production","secrets.json","credentials.json"}
    for p,rel in files(root):
        low=p.name.lower()
        if p.name in names or low.endswith(".pem") or low.endswith(".key"):
            suspicious.append(rel.as_posix())
    return suspicious

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--type",choices=["skill","expert","expert-team","connector","buddy-app","third-party-app"])
    ap.add_argument("--name")
    ap.add_argument("--version")
    ap.add_argument("--validator")
    ap.add_argument("--validation-status",choices=["pass","fail","not-run"],default="not-run")
    ap.add_argument("--side-effect-review",choices=["pass","fail","not-applicable","not-run"],default="not-run")
    ap.add_argument("--output")
    args=ap.parse_args()

    root=Path(args.path).resolve()
    if not root.is_dir(): raise SystemExit("path must be an asset directory")
    auto_type,auto_name,auto_version=detect(root)
    typ=args.type or auto_type
    if not typ: raise SystemExit("cannot infer asset type; pass --type")

    manifest_files=[
        {"path":rel.as_posix(),"sha256":sha256(p),"bytes":p.stat().st_size}
        for p,rel in files(root)
    ]
    suspicious=secret_scan(root)

    repo_root=Path(__file__).resolve().parents[1]
    manifest={
        "schema_version":1,
        "asset":{
            "type":typ,
            "name":args.name or auto_name,
            "version":args.version or auto_version
        },
        "generated_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "source":{
            "path":str(root),
            "git_commit":git_commit(root),
            "official_registry_reviewed_at":registry_date(repo_root)
        },
        "files":manifest_files,
        "validation":{
            "status":args.validation_status,
            "validator":args.validator,
            "notes":[]
        },
        "security":{
            "secret_scan":"fail" if suspicious else "pass",
            "side_effect_review":args.side_effect_review
        }
    }
    if suspicious:
        manifest["validation"]["notes"].append("Suspicious secret-like files: "+", ".join(suspicious))

    out=Path(args.output or root/"release-manifest.json")
    out.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n","utf-8")
    print(out)
    return 1 if suspicious else 0

if __name__=="__main__":
    raise SystemExit(main())
