#!/usr/bin/env python3
from __future__ import annotations
import binascii
import shutil
import struct
import subprocess
import sys
import tempfile
import zlib
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SCRIPTS=ROOT/"scripts"
TEMPLATES=ROOT/"90-templates"

def png_chunk(kind: bytes, data: bytes) -> bytes:
    body=kind+data
    return struct.pack(">I",len(data))+body+struct.pack(">I",binascii.crc32(body)&0xffffffff)

def write_png(path: Path, width=512, height=512):
    pixel=bytes([0,55,179,255])
    raw=b"".join(b"\x00"+pixel*width for _ in range(height))
    data=(
        b"\x89PNG\r\n\x1a\n"
        +png_chunk(b"IHDR",struct.pack(">IIBBBBB",width,height,8,6,0,0,0))
        +png_chunk(b"IDAT",zlib.compress(raw,9))
        +png_chunk(b"IEND",b"")
    )
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_bytes(data)

def write_svg(path: Path):
    path.write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">'
        '<rect width="64" height="64" rx="14" fill="#0037B3"/>'
        '<path d="M18 32h28M32 18v28" stroke="white" stroke-width="5" stroke-linecap="round"/>'
        '</svg>',
        encoding="utf-8"
    )

def run(*args):
    cmd=[sys.executable,*map(str,args)]
    p=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True)
    print("$"," ".join(cmd))
    if p.stdout: print(p.stdout.rstrip())
    if p.stderr: print(p.stderr.rstrip(),file=sys.stderr)
    if p.returncode: raise SystemExit(p.returncode)

def copy_template(name: str, dst: Path):
    shutil.copytree(TEMPLATES/name,dst)

def main():
    with tempfile.TemporaryDirectory(prefix="wb-opdk-smoke-") as td:
        base=Path(td)

        # Raw starter validation.
        skill=base/"skill"
        copy_template("skill-template",skill)
        run(SCRIPTS/"validate_skill.py",skill)

        expert=base/"expert"
        copy_template("expert-template",expert)
        write_png(expert/"avatars"/"expert.png")
        run(SCRIPTS/"validate_expert.py",expert)

        team=base/"expert-team"
        copy_template("expert-team-template",team)
        for name in ["team.png","team-lead.png","research-specialist.png","delivery-specialist.png"]:
            write_png(team/"avatars"/name)
        run(SCRIPTS/"validate_expert_team.py",team)

        for template in ["connector-mcp-token-template","connector-mcp-oauth-template","connector-cli-template"]:
            dst=base/template
            copy_template(template,dst)
            write_svg(dst/"icon.svg")
            run(SCRIPTS/"validate_connector.py",dst)

        # Scaffold output must also be structurally valid and path-renamed.
        sx=base/"scaffold-expert"
        run(SCRIPTS/"scaffold.py","expert","demo-expert",sx)
        assert (sx/"agents"/"demo-expert.md").is_file(), "expert agent file was not renamed"
        write_png(sx/"avatars"/"expert.png")
        run(SCRIPTS/"validate_expert.py",sx)

        st=base/"scaffold-team"
        run(SCRIPTS/"scaffold.py","expert-team","demo-team",st)
        assert (st/"agents"/"demo-team-team-lead.md").is_file(), "team lead file was not renamed"
        for name in ["team.png","team-lead.png","research-specialist.png","delivery-specialist.png"]:
            write_png(st/"avatars"/name)
        run(SCRIPTS/"validate_expert_team.py",st)

        sc=base/"scaffold-connector"
        run(SCRIPTS/"scaffold.py","connector-token","demo-service",sc)
        assert (sc/"skills"/"demo-service-usage"/"SKILL.md").is_file(), "connector skill directory was not renamed"
        write_svg(sc/"icon.svg")
        run(SCRIPTS/"validate_connector.py",sc)

        for name,root in [("skill-release.zip",skill),("expert-team-release.zip",team)]:
            out=base/name
            run(SCRIPTS/"pack_release.py",root,"--out",out)
            if not out.is_file() or out.stat().st_size==0:
                raise SystemExit(f"release packer did not produce {name}")
            print(f"release zip OK: {out.name} ({out.stat().st_size} bytes)")

    print("All template and scaffold smoke tests passed")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
