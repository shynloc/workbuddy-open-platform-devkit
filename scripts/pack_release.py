#!/usr/bin/env python3
from __future__ import annotations
import argparse, zipfile
from pathlib import Path

SKIP_NAMES={".DS_Store","Thumbs.db"}
SKIP_PARTS={"__pycache__",".git",".idea",".vscode"}
SKIP_SUFFIX={".pyc",".log"}

def include(p: Path, root: Path):
    rel=p.relative_to(root)
    if any(x in SKIP_PARTS for x in rel.parts):
        return False
    if p.name in SKIP_NAMES or p.suffix in SKIP_SUFFIX:
        return False
    if p.name.startswith(".env"):
        return False
    return p.is_file()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--out")
    args=ap.parse_args()
    root=Path(args.path).resolve()
    out=Path(args.out or f"{root.name}.zip").resolve()
    with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as z:
        for p in sorted(root.rglob("*")):
            if include(p,root):
                z.write(p,Path(root.name)/p.relative_to(root))
    print(out)
    return 0

if __name__=="__main__":
    raise SystemExit(main())
