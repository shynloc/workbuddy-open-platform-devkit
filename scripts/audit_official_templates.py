#!/usr/bin/env python3
"""Download and audit official WorkBuddy template ZIPs.

This script never overwrites local starter templates. It produces:
- a full machine-readable audit manifest;
- safe copies of text configuration files for human/agent review;
- compact baseline output;
- archive and key-file change detection against a committed baseline.

A detected upstream change is a review signal, not an automatic sync.
"""

from __future__ import annotations
import argparse
import datetime
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
DEFAULT_BASELINE=ROOT/"sources"/"official-template-audit-baseline.json"
TEXT_SUFFIXES={".json",".md",".yaml",".yml",".txt"}
MAX_TEXT_BYTES=512*1024

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def safe_member(name: str) -> bool:
    p=PurePosixPath(name)
    return not p.is_absolute() and ".." not in p.parts

def fetch(url: str) -> bytes:
    req=urllib.request.Request(url,headers={"User-Agent":"WB-OPDK-template-audit/1.2"})
    with urllib.request.urlopen(req,timeout=60) as resp:
        if not (200 <= resp.status < 400):
            raise RuntimeError(f"HTTP {resp.status}: {url}")
        return resp.read()

def build_report():
    data=json.loads(REGISTRY.read_text(encoding="utf-8"))
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    report={
        "schema_version":1,
        "audited_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),
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
            "key_file_paths":item.get("key_files",[]),
            "key_files":{},
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
                if info.filename in row["key_file_paths"]:
                    row["key_files"][info.filename]={
                        "bytes":len(content),
                        "sha256":frow["sha256"]
                    }

                suffix=PurePosixPath(info.filename).suffix.lower()
                if suffix in TEXT_SUFFIXES and len(content)<=MAX_TEXT_BYTES:
                    out=target/PurePosixPath(info.filename)
                    out.parent.mkdir(parents=True,exist_ok=True)
                    out.write_bytes(content)

        missing=[p for p in row["key_file_paths"] if p not in row["key_files"]]
        if missing:
            row["missing_key_files"]=missing

        report["templates"].append(row)

    (OUT/"manifest.json").write_text(
        json.dumps(report,ensure_ascii=False,indent=2)+"\n",
        encoding="utf-8"
    )
    return report

def compact_baseline(report):
    rows=[]
    for x in report["templates"]:
        rows.append({
            "id":x["id"],
            "page_url":x["page_url"],
            "download_url":x["download_url"],
            "filename":x["filename"],
            "archive_bytes":x["archive_bytes"],
            "archive_sha256":x["archive_sha256"],
            "key_files":x.get("key_files",{})
        })
    return {
        "schema_version":1,
        "audited_at":report["audited_at"],
        "templates":rows
    }

def key_file_changes(current, old):
    changes=[]
    cur=current.get("key_files",{})
    prev=old.get("key_files",{})
    for path in sorted(set(cur)|set(prev)):
        if path not in prev:
            changes.append({"path":path,"change":"added"})
        elif path not in cur:
            changes.append({"path":path,"change":"removed"})
        elif cur[path].get("sha256")!=prev[path].get("sha256"):
            changes.append({
                "path":path,
                "change":"content_changed",
                "old_sha256":prev[path].get("sha256"),
                "new_sha256":cur[path].get("sha256")
            })
    return changes

def compare(report, baseline):
    current={x["id"]:x for x in report["templates"]}
    old={x["id"]:x for x in baseline.get("templates",[])}
    changed=[]
    for tid in sorted(set(current)|set(old)):
        if tid not in old:
            changed.append({"id":tid,"change":"added"})
        elif tid not in current:
            changed.append({"id":tid,"change":"removed"})
        elif current[tid]["archive_sha256"]!=old[tid].get("archive_sha256"):
            changed.append({
                "id":tid,
                "change":"archive_changed",
                "old_sha256":old[tid].get("archive_sha256"),
                "new_sha256":current[tid]["archive_sha256"],
                "key_file_changes":key_file_changes(current[tid],old[tid])
            })
    return changed

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--baseline",default=str(DEFAULT_BASELINE))
    ap.add_argument("--fail-on-change",action="store_true")
    ap.add_argument("--write-baseline")
    ap.add_argument("--changes-out")
    args=ap.parse_args()

    report=build_report()

    summary=[
        {
            "id":x["id"],
            "archive_sha256":x["archive_sha256"],
            "archive_bytes":x["archive_bytes"],
            "files":len(x["files"]),
            "key_files":len(x.get("key_files",{}))
        }
        for x in report["templates"]
    ]
    print(json.dumps(summary,ensure_ascii=False,indent=2))

    if args.write_baseline:
        Path(args.write_baseline).write_text(
            json.dumps(compact_baseline(report),ensure_ascii=False,indent=2)+"\n",
            encoding="utf-8"
        )

    baseline_path=Path(args.baseline)
    changes=[]
    if baseline_path.is_file():
        baseline=json.loads(baseline_path.read_text(encoding="utf-8"))
        changes=compare(report,baseline)
        if changes:
            print("UPSTREAM TEMPLATE CHANGES DETECTED")
            print(json.dumps(changes,ensure_ascii=False,indent=2))
        else:
            print("Official template archives and key files match committed baseline.")

    if args.changes_out:
        Path(args.changes_out).write_text(
            json.dumps({"schema_version":1,"changes":changes},ensure_ascii=False,indent=2)+"\n",
            encoding="utf-8"
        )

    if changes and args.fail_on_change:
        return 2
    return 0

if __name__=="__main__":
    raise SystemExit(main())
