"""MkDocs hooks for WB-OPDK metadata badges."""

from __future__ import annotations
import html

COLORS={
    "OFFICIAL":("#0f766e","#ecfdf5"),
    "DERIVED":("#1d4ed8","#eff6ff"),
    "OBSERVED":("#a16207","#fefce8"),
    "EXPERIMENTAL":("#7e22ce","#faf5ff"),
    "STALE":("#b91c1c","#fef2f2"),
    "DEPRECATED":("#4b5563","#f3f4f6"),
}

def badge(text,fg="#374151",bg="#f3f4f6"):
    return (
        f'<span style="display:inline-block;padding:3px 8px;margin:0 6px 6px 0;'
        f'border-radius:999px;background:{bg};color:{fg};font-size:12px;font-weight:600;">'
        f'{html.escape(str(text))}</span>'
    )

def on_page_markdown(markdown,page,config,files):
    meta=page.meta or {}
    kt=meta.get("knowledge_type")
    status=meta.get("status")
    verified=meta.get("last_verified")
    sources=meta.get("official_sources")

    if not any([kt,status,verified,sources]):
        return markdown

    parts=[]
    if kt:
        fg,bg=COLORS.get(str(kt),("#374151","#f3f4f6"))
        parts.append(badge(kt,fg,bg))
    if status:
        fg,bg=COLORS.get(str(status),("#374151","#f3f4f6"))
        parts.append(badge(status,fg,bg))
    if verified:
        parts.append(badge(f"verified {verified}"))
    if isinstance(sources,list) and sources:
        parts.append(badge("sources: "+", ".join(map(str,sources))))
    elif sources:
        parts.append(badge("source: "+str(sources)))

    panel=(
        '<div style="margin:0 0 18px;padding:10px 12px;border:1px solid #e5e7eb;'
        'border-radius:10px;background:#fafafa;">'
        + "".join(parts)
        + '</div>\\n\\n'
    )
    return panel+markdown