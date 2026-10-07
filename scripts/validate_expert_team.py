#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from pathlib import Path

CATEGORY_PREFIXES={f"{i:02d}-" for i in range(1,16)}

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

    required=["name","version","description","author","agents","expertType","agentName","teamInfo","members","displayName","profession","displayDescription","avatar","categoryId","defaultInitPrompt","plugin","tags","quickPrompts"]
    for k in required:
        if k not in data:
            errs.append(f"missing plugin field: {k}")

    if data.get("expertType")!="team":
        errs.append("expertType must be team")

    name=data.get("name","")
    if name and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*",name):
        errs.append("name must be kebab-case")
    if data.get("plugin") and data.get("plugin")!=name:
        errs.append("plugin must equal name")

    agents=data.get("agents",[]) or []
    agent_ids={Path(x).stem for x in agents}
    for rel in agents:
        if not (root/rel).is_file():
            errs.append(f"missing agent file: {rel}")

    lead=data.get("agentName")
    team=data.get("teamInfo") or {}
    if team.get("leadAgent") and lead!=team.get("leadAgent"):
        errs.append("agentName must equal teamInfo.leadAgent")
    if lead and lead not in agent_ids:
        errs.append("lead agent is not present in agents[]")

    member_agents=set(team.get("memberAgents") or [])
    unknown=member_agents-agent_ids
    if unknown:
        errs.append(f"teamInfo.memberAgents missing from agents[]: {sorted(unknown)}")

    members=data.get("members",[]) or []
    member_ids={m.get("id") for m in members}
    if lead and lead not in member_ids:
        errs.append("members[] must include the lead agent")
    if member_agents-member_ids:
        errs.append(f"members[] missing declared members: {sorted(member_agents-member_ids)}")
    leads=[m for m in members if m.get("role")=="lead"]
    if len(leads)!=1:
        errs.append("members[] must contain exactly one role=lead")

    if data.get("tags") is not None and len(data.get("tags",[]))!=3:
        errs.append("field table currently requires exactly 3 tags; see sources/known-inconsistencies.md")
    if data.get("quickPrompts") is not None and len(data.get("quickPrompts",[]))!=3:
        errs.append("quickPrompts must contain exactly 3 items")
    if data.get("quickPrompts") and data.get("defaultInitPrompt")!=data["quickPrompts"][0]:
        errs.append("defaultInitPrompt must equal quickPrompts[0]")

    cat=data.get("categoryId","")
    if cat and not any(cat.startswith(x) for x in CATEGORY_PREFIXES):
        errs.append(f"unknown categoryId: {cat}")

    if not (root/"settings.json").is_file():
        errs.append("missing required settings.json; do not invent schema—use current official template")

    for m in members:
        av=m.get("avatar")
        if av:
            p=root/av
            if not p.is_file():
                errs.append(f"missing member avatar: {av}")
            elif p.stat().st_size>500*1024:
                errs.append(f"member avatar exceeds 500KB: {av}")

    if errs:
        print("EXPERT TEAM VALIDATION FAILED")
        for e in errs:
            print("-",e)
        return 1
    print("Expert Team validation passed")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
