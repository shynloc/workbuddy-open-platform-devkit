#!/usr/bin/env python3
"""Create a local snapshot manifest for WorkBuddy official source pages.

Stores hashes/headers only. It does not mirror full official page contents.
"""

from __future__ import annotations
import argparse,datetime,hashlib,json,re,urllib.request
from pathlib import Path

def parse_registry(path):
    items=[]; current=None
    for raw in Path(path).read_text("utf-8").splitlines():
        m=re.match(r"^  ([a-z0-9-]+):\s*$",raw)
        if m: current={"id":m.group(1)}; items.append(current); continue
        if current:
            m=re.match(r"^    url:\s*(\S+)",raw)
            if m: current["url"]=m.group(1)
    return [x for x in items if "url" in x]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--registry",default="sources/official-sources.yaml")
    ap.add_argument("--output",default="sources/source-snapshots.json")
    args=ap.parse_args()
    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    rows={}
    for src in parse_registry(args.registry):
        req=urllib.request.Request(src["url"],headers={"User-Agent":"WB-OPDK-snapshot/1.0"})
        try:
            with urllib.request.urlopen(req,timeout=20) as r:
                data=r.read()
                text=re.sub(r"\s+"," ",data.decode("utf-8","replace")).strip().encode()
                rows[src["id"]]={
                    "url":src["url"],"checked_at":now,"status":r.status,
                    "sha256":hashlib.sha256(text).hexdigest(),
                    "etag":r.headers.get("ETag"),"last_modified":r.headers.get("Last-Modified")
                }
        except Exception as e:
            rows[src["id"]]={"url":src["url"],"checked_at":now,"error":str(e)}
    Path(args.output).write_text(json.dumps({"generated_at":now,"sources":rows},ensure_ascii=False,indent=2)+"\n","utf-8")
    print(f"wrote {args.output}")

if __name__=="__main__": main()
