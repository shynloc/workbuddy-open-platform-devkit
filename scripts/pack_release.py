#!/usr/bin/env python3
from __future__ import annotations
import argparse, os, tempfile, zipfile
from pathlib import Path
from _package_files import include
from validate_asset_schemas import detect
from validate_release_zip import validate_archive, validate_source

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--out")
    args=ap.parse_args()
    root=Path(args.path).resolve()
    out=Path(args.out or f"{root.name}.zip").resolve()
    if out.is_relative_to(root):
        raise SystemExit('ZIP output must be outside the asset directory')
    temporary = None
    try:
        typ = detect(root)
        validate_source(root, typ)
        if any(p.is_symlink() for p in root.rglob('*')):
            raise ValueError('source package must not contain symlinks')
        out.parent.mkdir(parents=True, exist_ok=True)
        handle, temporary = tempfile.mkstemp(prefix='.'+out.name, suffix='.tmp', dir=out.parent)
        os.close(handle)
        with zipfile.ZipFile(temporary,"w",zipfile.ZIP_DEFLATED) as z:
            for p in sorted(root.rglob("*")):
                if include(p,root):
                    z.write(p,Path(root.name)/p.relative_to(root))
        validate_archive(temporary, typ, root)
        os.replace(temporary, out)
    except (ValueError, OSError, zipfile.BadZipFile) as exc:
        raise SystemExit(f'PACKAGING FAILED: {exc}')
    finally:
        if temporary and Path(temporary).exists():
            Path(temporary).unlink()
    print(out)
    return 0

if __name__=="__main__":
    raise SystemExit(main())
