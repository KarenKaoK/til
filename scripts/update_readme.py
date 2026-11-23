#!/usr/bin/env python3
"""Generate the category and article index in README.md."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
START_MARKER = "<!-- BEGIN GENERATED TIL INDEX -->"
END_MARKER = "<!-- END GENERATED TIL INDEX -->"
IGNORED_DIRECTORIES = {".git", ".github", "scripts"}
CATEGORY_LABELS = {
    "agent": "Agent",
    "leetcode": "LeetCode",
    "python": "Python",
    "testing": "Testing",
    "tool": "Tool",
}


def category_label(directory: Path) -> str:
    return CATEGORY_LABELS.get(directory.name, directory.name.replace("-", " ").title())


def article_title(path: Path) -> str:
    with path.open(encoding="utf-8") as article:
        for line in article:
            match = re.match(r"^#\s+(.+?)\s*$", line)
            if match:
                return match.group(1)
    return path.stem.replace("-", " ").replace("_", " ").title()


def markdown_text(text: str) -> str:
    return text.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")


def categories() -> list[tuple[str, str, list[Path]]]:
    result = []
    for directory in ROOT.iterdir():
        if not directory.is_dir() or directory.name.startswith("."):
            continue
        if directory.name in IGNORED_DIRECTORIES:
            continue

        articles = sorted(directory.rglob("*.md"))
        if articles:
            result.append((category_label(directory), directory.name, articles))

    return sorted(result, key=lambda category: category[0].casefold())


def render_index() -> str:
    found_categories = categories()
    lines = [START_MARKER, "", "### Categories", ""]

    for label, slug, _ in found_categories:
        lines.append(f"- [{markdown_text(label)}](#{slug})")

    for label, _, articles in found_categories:
        lines.extend(["", f"### {label}", ""])
        for article in articles:
            relative_path = article.relative_to(ROOT).as_posix()
            title = markdown_text(article_title(article))
            lines.append(f"- [{title}]({relative_path})")

    lines.extend(["", END_MARKER])
    return "\n".join(lines)


def update_readme() -> bool:
    original = README.read_text(encoding="utf-8")
    generated = render_index()

    if START_MARKER in original and END_MARKER in original:
        pattern = re.compile(
            rf"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}",
            re.DOTALL,
        )
        updated = pattern.sub(generated, original)
    else:
        categories_heading = re.search(r"^### Categories\s*$", original, re.MULTILINE)
        about_heading = re.search(r"^### About\s*$", original, re.MULTILINE)
        if not categories_heading or not about_heading:
            raise RuntimeError(
                "README.md must contain '### Categories' before '### About'."
            )
        updated = (
            original[: categories_heading.start()].rstrip()
            + "\n\n"
            + generated
            + "\n\n"
            + original[about_heading.start() :].lstrip()
        )

    if updated == original:
        return False

    README.write_text(updated, encoding="utf-8")
    return True


if __name__ == "__main__":
    changed = update_readme()
    print("Updated README.md" if changed else "README.md is already up to date")
