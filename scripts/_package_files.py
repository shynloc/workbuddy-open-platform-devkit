"""WB-OPDK packaging exclusions; hidden plugin manifests are included."""
SKIP_NAMES = {".DS_Store", "Thumbs.db", "release-manifest.json"}
SKIP_PARTS = {"__pycache__", ".git", ".idea", ".vscode"}
SKIP_SUFFIX = {".pyc", ".log"}


def include(path, root):
    relative = path.relative_to(root)
    return (path.is_file() and not any(x in SKIP_PARTS for x in relative.parts)
            and path.name not in SKIP_NAMES and path.suffix not in SKIP_SUFFIX
            and not path.name.startswith(".env"))
