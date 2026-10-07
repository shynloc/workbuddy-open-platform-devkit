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
    # Compressible solid RGBA placeholder generated only in the temporary smoke-test directory.
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
    if p.stdout:
        print(p.stdout.rstrip())
    if p.stderr:
        print(p.stderr.rstrip(),file=sys.stderr)
    if p.returncode:
        raise SystemExit(p.returncode)

def copy_template(name: str, dst: Path):
    shutil.copytree(TEMPLATES/name,dst)

def main():
    with tempfile.TemporaryDirectory(prefix="wb-opdk-smoke-") as td:
        base=Path(td)

        skill=base/"skill"
        copy_template("skill-template",skill)
        run(SCRIPTS/"validate_skill.py",skill)

        expert=base/"expert"
        copy_template("expert-template",expert)
        write_png(expert/"avatars"/"expert.png")
        run(SCRIPTS/"validate_expert.py",expert)

        for template in [
            "connector-mcp-token-template",
            "connector-mcp-oauth-template",
            "connector-cli-template",
        ]:
            dst=base/template
            copy_template(template,dst)
            write_svg(dst/"icon.svg")
            run(SCRIPTS/"validate_connector.py",dst)

        out=base/"skill-release.zip"
        run(SCRIPTS/"pack_release.py",skill,"--out",out)
        if not out.is_file() or out.stat().st_size==0:
            raise SystemExit("release packer did not produce a zip")
        print(f"release zip OK: {out.name} ({out.stat().st_size} bytes)")

    print("All template smoke tests passed")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
