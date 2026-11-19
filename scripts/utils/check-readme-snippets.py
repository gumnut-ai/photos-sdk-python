"""Type-check the Python code blocks in README.md, so a broken example fails lint.

Each block is checked as its own module with ty. A block may use `client` without creating
it, as README fragments do. Mark a block that can't be checked on its own, such as one using a
placeholder value, by putting `<!-- readme-snippet-check: skip -->` before it.
"""

import re
import ast
import sys
import tempfile
import subprocess
from pathlib import Path

SKIP_MARKER = "<!-- readme-snippet-check: skip -->"
LANGUAGES = {"python", "py"}
# Prepended to a block that doesn't create the client itself.
PRELUDE = [
    "import gumnut as _readme_sdk",
    "client = _readme_sdk.Gumnut()",
]

root = Path(__file__).resolve().parents[2]
lines = (root / "README.md").read_text().split("\n")


def preceded_by_skip_marker(fence: int) -> bool:
    """Look back over the blank lines and HTML comments above a fence."""
    j = fence - 1
    while j >= 0 and re.fullmatch(r"(<!--.*-->)?\s*", lines[j]):
        if lines[j].strip() == SKIP_MARKER:
            return True
        j -= 1
    return False


def binds_client(code: str) -> bool:
    return any(
        isinstance(node, ast.Name) and node.id == "client" and isinstance(node.ctx, ast.Store)
        for node in ast.walk(ast.parse(code))
    )


blocks: list[tuple[int, str]] = []
skipped = 0
i = 0
while i < len(lines):
    fence = re.fullmatch(r"```(\S*)\s*", lines[i])
    if fence and fence.group(1):
        end = next((j for j in range(i + 1, len(lines)) if re.fullmatch(r"```\s*", lines[j])), None)
        if end is None:
            sys.exit(f"README.md:{i + 1}: unclosed code block")
        if fence.group(1) in LANGUAGES:
            if preceded_by_skip_marker(i):
                skipped += 1
            else:
                blocks.append((i + 2, "\n".join(lines[i + 1 : end])))
        i = end
    i += 1

if not blocks:
    sys.exit("No Python code blocks found in README.md")

with tempfile.TemporaryDirectory(prefix="readme-snippets-") as tmp:
    files = []
    offsets = []
    for index, (_, code) in enumerate(blocks):
        prelude = [] if binds_client(code) else PRELUDE
        file = Path(tmp) / f"snippet_{index}.py"
        file.write_text("\n".join([*prelude, code, ""]))
        files.append(str(file))
        offsets.append(len(prelude))

    result = subprocess.run(
        ["ty", "check", "--output-format", "concise", "--error-on-warning", *files],
        cwd=root,
        capture_output=True,
        text=True,
    )


def to_readme_location(match: re.Match[str]) -> str:
    index = int(match.group(1))
    return f"README.md:{blocks[index][0] + int(match.group(2)) - offsets[index] - 1}:"


print(re.sub(r"\S*snippet_(\d+)\.py:(\d+):", to_readme_location, result.stdout + result.stderr), end="")
if result.returncode != 0:
    sys.exit(result.returncode)
print(f"Type-checked {len(blocks)} README code blocks ({skipped} skipped)")
