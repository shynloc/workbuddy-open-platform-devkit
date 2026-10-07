#!/usr/bin/env python3
"""Check WorkBuddy official source URLs and detect upstream changes.

The script is intentionally read-only with respect to KB documents. It can:
- fetch every registered official source;
- compute raw-HTML and visible-text hashes;
- compare the current snapshot with a committed baseline;
- write a baseline snapshot when explicitly requested;
- fail CI when registered source content changes.

A detected change is a review signal, not permission to overwrite local KB files.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import urllib.request
from pathlib import Path


def parse_registry(path: Path):
    """Parse the tiny YAML subset used by official-sources.yaml."""
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


def collapse_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def normalize_html(data: bytes) -> bytes:
    text = data.decode("utf-8", errors="replace")
    return collapse_ws(text).encode("utf-8")


def visible_text(data: bytes) -> bytes:
    """Best-effort deterministic visible-text extraction with stdlib only.

    We remove scripts/styles and markup noise so a frontend bundle/hash change does
    not automatically look like a documentation-content change. This is not a
    semantic parser; a change is still only a signal for human/agent review.
    """
    text = data.decode("utf-8", errors="replace")
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(
        r"<(script|style|noscript|svg)\b[^>]*>.*?</\1>",
        " ",
        text,
        flags=re.S | re.I,
    )
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    return collapse_ws(text).encode("utf-8")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch(url: str, timeout: int):
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "WB-OPDK-source-check/2.0",
            "Accept": "text/html,application/xhtml+xml",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()
        return resp.status, dict(resp.headers), data


def load_baseline(path: Path | None):
    if path is None or not path.is_file():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return {x["id"]: x for x in data if isinstance(x, dict) and x.get("id")}
    if isinstance(data, dict) and isinstance(data.get("sources"), list):
        return {x["id"]: x for x in data["sources"] if x.get("id")}
    raise ValueError(f"unsupported baseline format: {path}")


def public_snapshot(results):
    fields = (
        "id",
        "url",
        "status",
        "html_sha256",
        "text_sha256",
        "visible_text_bytes",
        "last_modified",
        "etag",
    )
    return [{k: row.get(k) for k in fields if k in row} for row in results if row.get("ok")]


def compare(row, baseline):
    old = baseline.get(row["id"])
    if not old:
        return "new-source"
    if old.get("url") != row.get("url"):
        return "url-changed"

    # Prefer visible-text hash. Fall back to raw HTML for sources where visible
    # extraction yields very little useful text.
    current_text = row.get("text_sha256")
    old_text = old.get("text_sha256")
    if current_text and old_text and row.get("visible_text_bytes", 0) >= 200:
        if current_text != old_text:
            return "content-changed"
        return None

    if old.get("html_sha256") and old.get("html_sha256") != row.get("html_sha256"):
        return "html-changed"
    return None


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--registry", default="sources/official-sources.yaml")
    p.add_argument("--timeout", type=int, default=20)
    p.add_argument("--json", action="store_true")
    p.add_argument("--baseline", help="Compare against a committed baseline JSON file.")
    p.add_argument("--write-baseline", help="Write the current successful snapshot to this JSON file.")
    p.add_argument(
        "--fail-on-change",
        action="store_true",
        help="Exit 2 if a source is new/changed relative to --baseline.",
    )
    args = p.parse_args()

    baseline_path = Path(args.baseline) if args.baseline else None
    baseline = load_baseline(baseline_path)

    results = []
    for src in parse_registry(Path(args.registry)):
        row = {"id": src["id"], "url": src["url"]}
        try:
            status, headers, data = fetch(src["url"], args.timeout)
            vis = visible_text(data)
            row.update(
                {
                    "ok": 200 <= status < 400,
                    "status": status,
                    "html_sha256": sha256(normalize_html(data)),
                    "text_sha256": sha256(vis),
                    "bytes": len(data),
                    "visible_text_bytes": len(vis),
                    "last_modified": headers.get("Last-Modified"),
                    "etag": headers.get("ETag"),
                }
            )
            if baseline:
                change = compare(row, baseline)
                if change:
                    row["change"] = change
        except Exception as exc:
            row.update({"ok": False, "error": str(exc)})
        results.append(row)

    if args.write_baseline:
        out = Path(args.write_baseline)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "registry": args.registry,
                    "sources": public_snapshot(results),
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for row in results:
            if row["ok"]:
                marker = "CHG" if row.get("change") else "OK "
                digest = row["text_sha256"][:16]
                suffix = f' [{row["change"]}]' if row.get("change") else ""
                print(f'{marker} {row["id"]:<36} {digest} {row["url"]}{suffix}')
            else:
                print(
                    f'FAIL {row["id"]:<36} '
                    f'{row.get("error", row.get("status"))} {row["url"]}'
                )

    if not all(row["ok"] for row in results):
        return 1
    if args.fail_on_change and any(row.get("change") for row in results):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
