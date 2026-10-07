#!/usr/bin/env python3
"""Check WorkBuddy official source URLs and compute normalized HTML hashes.

This script does NOT update KB documents automatically. It only reports status
and hashes so a human/agent can compare upstream changes before editing.
"""

from __future__ import annotations
import argparse
import hashlib
import json
import re
import sys
import urllib.request
from pathlib import Path


def parse_registry(path: Path):
    # Tiny YAML subset parser: only extracts source ids + url lines from our registry.
    items = []
    current = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^  ([a-z0-9-]+):\s*$", raw)
        if m:
            current = {"id": m.group(1)}
            items.append(current)
            continue
        if current:
            m = re.match(r"^    url:\s*(\S+)\s*$", raw)
            if m:
                current["url"] = m.group(1)
    return [x for x in items if "url" in x]


def normalize_html(data: bytes) -> bytes:
    text = data.decode("utf-8", errors="replace")
    text = re.sub(r"\s+", " ", text).strip()
    return text.encode("utf-8")


def fetch(url: str, timeout: int):
    req = urllib.request.Request(url, headers={"User-Agent": "WB-OPDK-source-check/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()
        return resp.status, dict(resp.headers), data


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--registry", default="sources/official-sources.yaml")
    p.add_argument("--timeout", type=int, default=20)
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    results = []
    for src in parse_registry(Path(args.registry)):
        row = {"id": src["id"], "url": src["url"]}
        try:
            status, headers, data = fetch(src["url"], args.timeout)
            norm = normalize_html(data)
            row.update({
                "ok": 200 <= status < 400,
                "status": status,
                "sha256": hashlib.sha256(norm).hexdigest(),
                "bytes": len(data),
                "last_modified": headers.get("Last-Modified"),
                "etag": headers.get("ETag"),
            })
        except Exception as exc:
            row.update({"ok": False, "error": str(exc)})
        results.append(row)

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for r in results:
            if r["ok"]:
                print(f'OK   {r["id"]:<36} {r["sha256"][:16]} {r["url"]}')
            else:
                print(f'FAIL {r["id"]:<36} {r.get("error", r.get("status"))} {r["url"]}')

    return 0 if all(r["ok"] for r in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
