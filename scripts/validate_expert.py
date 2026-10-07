#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from pathlib import Path

CATEGORY_PREFIXES = {f"{i:02d}-" for i in range(1,16)}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("path")
    args=ap.parse_args()
    root=Path(args.path)
    errs=[]
    cfg=root/".codebuddy-plugin"/"plugin.json"
    if not cfg.is_file():
        errs.append("missing .codebuddy-plugin/plugin.json")
        data={}
    else:
        try:
            data=json.loads(cfg.read_text(encoding="utf-8"))
        except Exception as e:
            data={}
            errs.append(f"invalid plugin.json: {e}")
    required=["name","version","description","author","agents","expertType","agentName","displayName","profession","displayDescription","avatar","categoryId","defaultInitPrompt","plugin","tags","quickPrompts"]
    for k in required:
        if k not in data:
            errs.append(f"missing plugin field: {k}")
    if data.get("expertType") != "agent":
        errs.append("expertType must be agent")
    name=data.get("name","")
    if name and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*",name):
        errs.append("name must be kebab-case")
    if data.get("plugin") and data.get("plugin")!=name:
        errs.append("plugin must equal name")
    if data.get("tags") is not None and len(data.get("tags",[]))!=3:
        errs.append("tags must contain exactly 3 items")
    if data.get("quickPrompts") is not None and len(data.get("quickPrompts",[]))!=3:
        errs.append("quickPrompts must contain exactly 3 items")
    if data.get("quickPrompts") and data.get("defaultInitPrompt") != data["quickPrompts"][0]:
        errs.append("defaultInitPrompt must equal quickPrompts[0]")
    cat=data.get("categoryId","")
    if cat and not any(cat.startswith(x) for x in CATEGORY_PREFIXES):
        errs.append(f"unknown categoryId: {cat}")
    for rel in data.get("agents",[]) or []:
        if not (root/rel).is_file():
            errs.append(f"missing agent file: {rel}")
    avatar=data.get("avatar")
    if avatar:
        p=root/avatar
        if not p.is_file():
            errs.append(f"missing avatar: {avatar}")
        elif p.stat().st_size>500*1024:
            errs.append(f"avatar exceeds 500KB: {avatar}")
    desc=data.get("displayDescription")
    zh=desc.get("zh") if isinstance(desc,dict) else None
    if zh and not (40 <= len(zh) <= 50):
        errs.append(f"displayDescription.zh length is {len(zh)}, expected 40-50")
    if errs:
        print("EXPERT VALIDATION FAILED")
        for e in errs:
            print("-",e)
        return 1
    print("Expert validation passed")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
