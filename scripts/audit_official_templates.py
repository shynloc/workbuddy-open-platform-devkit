#!/usr/bin/env python3
"""Download and audit official WorkBuddy template ZIPs.

This script never overwrites local starter templates. It creates an audit
artifact containing:
- archive SHA256 / size;
- member paths, sizes and hashes;
- safe copies of text configuration files for review.

The output is evidence for maintaining WB-OPDK, not an automatic sync.
"""

from __future__ import annotations
import hashlib
import io
import json
import shutil
import urllib.request
import zipfile
from pathlib import Path, PurePosixPath

ROOT=Path(__file__).resolve().parents[1]
REGISTRY=ROOT/"sources"/"official-templates.json"
OUT=ROOT/"build"/"official-template-audit"
TEXT_SUFFIXES={".json",".md",".yaml",".yml",".txt"}
MAX_TEXT_BYTES=512*1024

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def safe_member(name: str) -> bool:
    p=PurePosixPath(name)
    return not p.is_absolute() and ".." not in p.parts

def fetch(url: str) -> bytes:
    req=urllib.request.Request(
        url,
        headers={"User-Agent":"WB-OPDK-template-audit/1.0"}
    )
    with urllib.request.urlopen(req,timeout=60) as resp:
        if not (200 <= resp.status < 400):
            raise RuntimeError(f"HTTP {resp.status}: {url}")
        return resp.read()

def main():
    data=json.loads(REGISTRY.read_text(encoding="utf-8"))
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    report={
        "schema_version":1,
        "registry":str(REGISTRY.relative_to(ROOT)),
        "templates":[]
    }

    for item in data["templates"]:
        archive=fetch(item["download_url"])
        row={
            "id":item["id"],
            "page_url":item["page_url"],
            "download_url":item["download_url"],
            "filename":item["filename"],
            "archive_bytes":len(archive),
            "archive_sha256":sha256(archive),
            "files":[]
        }

        target=OUT/item["id"]
        target.mkdir()
        with zipfile.ZipFile(io.BytesIO(archive)) as z:
            for info in z.infolist():
                if info.is_dir():
                    continue
                if not safe_member(info.filename):
                    raise RuntimeError(f"unsafe ZIP member: {info.filename}")
                content=z.read(info)
                frow={
                    "path":info.filename,
                    "bytes":len(content),
                    "sha256":sha256(content)
                }
                row["files"].append(frow)

                suffix=PurePosixPath(info.filename).suffix.lower()
                if suffix in TEXT_SUFFIXES and len(content)<=MAX_TEXT_BYTES:
                    out=target/PurePosixPath(info.filename)
                    out.parent.mkdir(parents=True,exist_ok=True)
                    out.write_bytes(content)

        report["templates"].append(row)

    (OUT/"manifest.json").write_text(
        json.dumps(report,ensure_ascii=False,indent=2)+"\n",
        encoding="utf-8"
    )
    print(json.dumps(
        [
            {
                "id":x["id"],
                "archive_sha256":x["archive_sha256"],
                "archive_bytes":x["archive_bytes"],
                "files":len(x["files"])
            }
            for x in report["templates"]
        ],
        ensure_ascii=False,
        indent=2
    ))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
