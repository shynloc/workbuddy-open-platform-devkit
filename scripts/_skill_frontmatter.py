"""Shared YAML semantics for Skill validation and release metadata."""
import re
from pathlib import Path
import yaml


def parse_frontmatter(text):
    match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
    if not match:
        return None, "missing or unterminated YAML frontmatter"
    try:
        value = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return None, f"invalid YAML frontmatter: {exc}"
    if not isinstance(value, dict):
        return None, "frontmatter must be a YAML mapping"
    return value, None


def read_frontmatter(path):
    value, error = parse_frontmatter(Path(path).read_text(encoding="utf-8"))
    if error:
        raise ValueError(error)
    return value


def skill_identity(path):
    value = read_frontmatter(path)
    for key in ("name", "version"):
        if not isinstance(value.get(key), str) or not value[key].strip():
            raise ValueError(f"{key} must be a non-empty string")
    return value["name"], value["version"]
