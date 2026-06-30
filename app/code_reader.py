from pathlib import Path

IGNORE = {
    ".git",
    "venv",
    "__pycache__",
    "node_modules",
    ".next"
}

EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".json",
    ".md",
    ".yml",
    ".yaml"
}


def read_codebase(repo_path: str, max_chars: int = 80000):

    repo = Path(repo_path)
    chunks = []

    for path in repo.rglob("*"):

        if any(part in IGNORE for part in path.parts):
            continue

        if path.is_file() and path.suffix in EXTENSIONS:

            try:
                text = path.read_text(errors="ignore")

                chunks.append(
                    f"\n\n===== FILE: {path.relative_to(repo)} =====\n{text}"
                )

            except Exception:
                pass

    return "".join(chunks)[:max_chars]