#!/usr/bin/env python3
"""Turn Source Watch status JSON into an impact-aware review report."""

from __future__ import annotations
import argparse, datetime, json
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("status_json")
    ap.add_argument("--impact-map",default="sources/source-impact-map.json")
    ap.add_argument("--json-out",default="source-change-report.json")
    ap.add_argument("--markdown-out",default="source-change-report.md")
    args=ap.parse_args()

    status=json.loads(Path(args.status_json).read_text("utf-8"))
    impact=json.loads(Path(args.impact_map).read_text("utf-8")).get("sources",{})
    changed=[]

    for row in status:
        if not row.get("change") and row.get("ok",False):
            continue
        item={
            "id":row.get("id"),
            "url":row.get("url"),
            "change":row.get("change") or ("fetch-failed" if not row.get("ok") else None),
            "error":row.get("error"),
            "affected":impact.get(row.get("id"),{}).get("affected",[])
        }
        item["recommended_actions"]=[
            "Re-open the current official source and identify the semantic change.",
            "Review every affected KB/schema/template/validator path.",
            "Mark affected knowledge as STALE when the change can alter behavior or publishing compatibility.",
            "Update tests before updating templates or validators.",
            "Only update the committed baseline after review is complete."
        ]
        changed.append(item)

    report={
        "schema_version":1,
        "generated_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "changes":changed
    }
    Path(args.json_out).write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n","utf-8")

    lines=["# WorkBuddy Official Source Change Review",""]
    if not changed:
        lines += ["No registered official source changes or fetch failures were detected.",""]
    else:
        lines += [
            f"Detected **{len(changed)}** source change(s) / failure(s).",
            "",
            "> This is a review artifact. It does not authorize automatic KB updates.",
            ""
        ]
        for item in changed:
            lines += [
                f"## {item['id']}",
                "",
                f"- Change: `{item['change']}`",
                f"- Official URL: {item['url']}",
            ]
            if item.get("error"):
                lines.append(f"- Error: `{item['error']}`")
            lines += ["","### STALE candidates",""]
            if item["affected"]:
                lines += [f"- `{p}`" for p in item["affected"]]
            else:
                lines.append("- No impact mapping registered yet.")
            lines += ["","### Review actions",""]
            lines += [f"- [ ] {x}" for x in item["recommended_actions"]]
            lines.append("")

    Path(args.markdown_out).write_text("\n".join(lines)+"\n","utf-8")
    print(json.dumps({"changes":len(changed),"json":args.json_out,"markdown":args.markdown_out},ensure_ascii=False))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
