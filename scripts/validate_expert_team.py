#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from pathlib import Path
from _image_utils import validate_avatar

CATEGORY_PREFIXES={f"{i:02d}-" for i in range(1,16)}

def load_json(path: Path, errs: list[str], label: str):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        errs.append(f"invalid {label}: {e}")
        return {}

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
        data=load_json(cfg,errs,"plugin.json")

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

    v=data.get("version","")
    if v and not re.fullmatch(r"\d+\.\d+\.\d+",v):
        errs.append(f"version is not semver: {v}")

    agents=data.get("agents",[]) or []
    agent_ids={Path(x).stem for x in agents}
    for rel in agents:
        p=root/rel
        if not p.is_file():
            errs.append(f"missing agent file: {rel}")
        else:
            text=p.read_text(encoding="utf-8",errors="replace")
            m=re.search(r"(?m)^name:\s*([^\n]+)",text)
            if m and m.group(1).strip().strip("'\"")!=Path(rel).stem:
                errs.append(f"Agent MD name must match filename: {rel}")

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

    # Official docs currently say settings.json, while the official trading-team.zip
    # currently contains setting.json with {"agent": "<lead>"}. Accept either one
    # but never both; see sources/known-inconsistencies.md.
    singular=root/"setting.json"
    plural=root/"settings.json"
    if singular.is_file() and plural.is_file():
        errs.append("both setting.json and settings.json exist; upstream naming is inconsistent, package must choose one")
    elif singular.is_file():
        setting=load_json(singular,errs,"setting.json")
        if setting.get("agent")!=lead:
            errs.append(f"setting.json agent must equal lead agent: expected {lead!r}, got {setting.get('agent')!r}")
    elif plural.is_file():
        settings=load_json(plural,errs,"settings.json")
        # Public docs do not currently expose a schema. If an agent field is
        # present, at least enforce consistency with the lead.
        if "agent" in settings and settings.get("agent")!=lead:
            errs.append(f"settings.json agent must equal lead agent: expected {lead!r}, got {settings.get('agent')!r}")
    else:
        errs.append("missing lead settings file: official docs say settings.json; official trading-team.zip uses setting.json")

    # Team-level market avatar.
    if data.get("avatar"):
        validate_avatar(root/data["avatar"],"team avatar",errs)

    # Member avatars.
    for m in members:
        av=m.get("avatar")
        if av:
            validate_avatar(root/av,f"member avatar {m.get('id') or av}",errs)

    desc=data.get("displayDescription")
    zh=desc.get("zh") if isinstance(desc,dict) else None
    if zh and not (40 <= len(zh) <= 50):
        errs.append(f"displayDescription.zh length is {len(zh)}, expected 40-50")

    if errs:
        print("EXPERT TEAM VALIDATION FAILED")
        for e in errs:
            print("-",e)
        return 1
    print("Expert Team validation passed")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
