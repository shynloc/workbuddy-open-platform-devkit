from __future__ import annotations
import struct
from pathlib import Path

JPEG_SOF = {
    0xC0,0xC1,0xC2,0xC3,0xC5,0xC6,0xC7,
    0xC9,0xCA,0xCB,0xCD,0xCE,0xCF
}

def image_dimensions(path: Path):
    data=path.read_bytes()
    if data.startswith(b"\x89PNG\r\n\x1a\n") and len(data)>=24:
        width,height=struct.unpack(">II",data[16:24])
        return "png",width,height

    if data.startswith(b"\xff\xd8"):
        i=2
        n=len(data)
        while i+4<=n:
            if data[i]!=0xFF:
                i+=1
                continue
            while i<n and data[i]==0xFF:
                i+=1
            if i>=n:
                break
            marker=data[i]
            i+=1
            if marker in {0xD8,0xD9}:
                continue
            if marker==0xDA:
                break
            if i+2>n:
                break
            seglen=int.from_bytes(data[i:i+2],"big")
            if seglen<2 or i+seglen>n:
                break
            if marker in JPEG_SOF and seglen>=7:
                height=int.from_bytes(data[i+3:i+5],"big")
                width=int.from_bytes(data[i+5:i+7],"big")
                return "jpeg",width,height
            i+=seglen
    return None,None,None

def validate_avatar(path: Path, label: str, errs: list[str]):
    if not path.is_file():
        errs.append(f"missing {label}: {path}")
        return
    if path.suffix.lower() not in {".png",".jpg",".jpeg"}:
        errs.append(f"{label} must be PNG/JPG: {path}")
        return
    if path.stat().st_size>500*1024:
        errs.append(f"{label} exceeds 500KB: {path}")
    fmt,w,h=image_dimensions(path)
    if fmt is None:
        errs.append(f"{label} is not a readable PNG/JPEG: {path}")
    elif (w,h)!=(512,512):
        errs.append(f"{label} must be 512x512, got {w}x{h}: {path}")
