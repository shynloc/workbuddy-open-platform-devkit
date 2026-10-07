#!/usr/bin/env python3
"""Check technical-literal consistency across WorkBuddy zh/en official docs.

This does NOT claim semantic translation equivalence. It detects:
- fetch failures;
- technical literals present in one language but absent in the other;
- extreme visible-text size divergence as a review signal.
"""

from __future__ import annotations
import argparse, datetime, html, json, re, urllib.request
from pathlib import Path

def collapse(text):
    return re.sub(r"\s+"," ",text).strip()

def visible(data):
    text=data.decode("utf-8","replace")
    text=re.sub(r"<!--.*?-->"," ",text,flags=re.S)
    text=re.sub(r"<(script|style|noscript|svg)\b[^>]*>.*?</\1>"," ",text,flags=re.S|re.I)
    text=re.sub(r"<[^>]+>"," ",text)
    return collapse(html.unescape(text))

def fetch(url,timeout):
    req=urllib.request.Request(url,headers={
        "User-Agent":"WB-OPDK-bilingual-check/1.0",
        "Accept":"text/html,application/xhtml+xml"
    })
    with urllib.request.urlopen(req,timeout=timeout) as r:
        return r.status,visible(r.read())

def contains(text,literal):
    return literal.casefold() in text.casefold()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--registry",default="sources/bilingual-docs.json")
    ap.add_argument("--timeout",type=int,default=20)
    ap.add_argument("--json-out",default="bilingual-report.json")
    ap.add_argument("--markdown-out",default="bilingual-report.md")
    ap.add_argument("--fail-on-mismatch",action="store_true")
    args=ap.parse_args()

    cfg=json.loads(Path(args.registry).read_text("utf-8"))
    rows=[]
    critical=False

    for pair in cfg["pairs"]:
        row={"id":pair["id"],"zh":pair["zh"],"en":pair["en"]}
        try:
            zstatus,ztext=fetch(pair["zh"],args.timeout)
            estatus,etext=fetch(pair["en"],args.timeout)
            row["zh_status"]=zstatus
            row["en_status"]=estatus
            row["zh_text_bytes"]=len(ztext.encode())
            row["en_text_bytes"]=len(etext.encode())
            row["missing_in_zh"]=[]
            row["missing_in_en"]=[]
            for lit in pair.get("required_literals",[]):
                if not contains(ztext,lit): row["missing_in_zh"].append(lit)
                if not contains(etext,lit): row["missing_in_en"].append(lit)
            smaller=max(1,min(row["zh_text_bytes"],row["en_text_bytes"]))
            larger=max(row["zh_text_bytes"],row["en_text_bytes"])
            row["size_ratio"]=round(larger/smaller,2)
            row["size_warning"]=row["size_ratio"]>3.0
            row["ok"]=(
                200<=zstatus<400 and 200<=estatus<400
                and not row["missing_in_zh"]
                and not row["missing_in_en"]
            )
        except Exception as exc:
            row.update({"ok":False,"error":str(exc)})
        if not row["ok"]: critical=True
        rows.append(row)

    report={
        "schema_version":1,
        "generated_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "note":"Technical-literal consistency signal only; not semantic translation validation.",
        "pairs":rows
    }
    Path(args.json_out).write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n","utf-8")

    md=[
        "# WorkBuddy zh/en Official Docs Consistency Review",
        "",
        "> This checks technical literals and structural signals only. It does not assert semantic translation equivalence.",
        ""
    ]
    for row in rows:
        mark="✅" if row["ok"] else "⚠️"
        md += [f"## {mark} {row['id']}",""]
        if row.get("error"):
            md += [f"- Error: `{row['error']}`",""]
            continue
        md += [
            f"- zh bytes: {row['zh_text_bytes']}",
            f"- en bytes: {row['en_text_bytes']}",
            f"- size ratio: {row['size_ratio']}",
            f"- missing in zh: {', '.join(row['missing_in_zh']) or 'none'}",
            f"- missing in en: {', '.join(row['missing_in_en']) or 'none'}",
            ""
        ]
    Path(args.markdown_out).write_text("\n".join(md)+"\n","utf-8")
    print(json.dumps({"pairs":len(rows),"critical":critical},ensure_ascii=False))
    return 2 if critical and args.fail_on_mismatch else 0

if __name__=="__main__":
    raise SystemExit(main())
