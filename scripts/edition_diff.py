"""Edition diff report: what a branch changes in the books compared with a reference tag.

For each module, compares the blocks used by the books (book.py and sequence_*.py) at the
reference (default: tag ``edition1-final``) and at the target (default: ``HEAD``):

- added      : used at target, not at reference
- disabled   : used at reference, no longer used at target (file kept)
- modified   : used at target, edition-1 block file changed (may also be listed as added)
- DELETED    : block file of the reference removed at target (forbidden by the edition-2 rules)

Usage: uv run python scripts/edition_diff.py [--ref edition1-final] [--target HEAD] [--out report.md]
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys

REF_RE = re.compile(r"\bblocks\.([A-Za-z_]\w*)")


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], check=True, capture_output=True, text=True
    ).stdout


def files_at(rev: str) -> set[str]:
    return set(git("ls-tree", "-r", "--name-only", rev, "modules").splitlines())


def used_blocks(rev: str, module: str, files: set[str]) -> set[str]:
    used: set[str] = set()
    for path in sorted(files):
        name = path.rsplit("/", 1)[-1]
        if not path.startswith(f"modules/{module}/") or path.count("/") != 2:
            continue
        if name != "book.py" and not (
            name.startswith("sequence") and name.endswith(".py")
        ):
            continue
        for line in git("show", f"{rev}:{path}").splitlines():
            code = line.split("#", 1)[0]
            used.update(REF_RE.findall(code))
    return used


def block_path(module: str, block: str, files: set[str]) -> str | None:
    for candidate in (
        f"modules/{module}/blocks/{block}.py",
        f"modules/shared-blocks/blocks/{block}.py",
    ):
        if candidate in files:
            return candidate
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--ref", default="edition1-final")
    parser.add_argument("--target", default="HEAD")
    parser.add_argument("--out")
    args = parser.parse_args()

    ref_files, tgt_files = files_at(args.ref), files_at(args.target)
    changed = set(
        git("diff", "--name-only", args.ref, args.target, "--", "modules").splitlines()
    )
    modules = sorted(
        {p.split("/")[1] for p in ref_files | tgt_files if p.count("/") >= 2}
    )

    out = [f"# Edition diff — `{args.ref}` → `{args.target}`", ""]
    reported: set[str] = set()
    for module in modules:
        if module == "shared-blocks":
            continue
        ref_used = used_blocks(args.ref, module, ref_files)
        tgt_used = used_blocks(args.target, module, tgt_files)
        added = sorted(tgt_used - ref_used)
        disabled = sorted(ref_used - tgt_used)
        modified = sorted(
            b
            for b in tgt_used
            if (p := block_path(module, b, tgt_files))
            and p in changed
            and p in ref_files
        )
        reported.update(p for b in modified if (p := block_path(module, b, tgt_files)))
        if not (added or disabled or modified):
            out += [f"## {module} — unchanged ({len(tgt_used)} blocks used)", ""]
            continue
        out += [
            f"## {module}",
            "",
            f"Blocks used: {len(ref_used)} → {len(tgt_used)} · added {len(added)} · "
            f"disabled {len(disabled)} · modified {len(modified)}",
            "",
        ]
        for label, items in (
            ("Added", added),
            ("Disabled (file kept)", disabled),
            ("Modified edition-1 block", modified),
        ):
            if items:
                out += [f"**{label}**: " + ", ".join(f"`{b}`" for b in items), ""]

    modified_files = set(
        git(
            "diff",
            "--name-only",
            "--diff-filter=M",
            args.ref,
            args.target,
            "--",
            "modules",
        ).splitlines()
    )
    other = sorted(
        p for p in modified_files - reported if p.endswith(".py") and "/blocks/" in p
    )
    out += [
        "## Other edition-1 block files modified (not used by the edition-2 books)",
        "",
    ]
    out += [f"- `{p}`" for p in other] if other else ["None."]
    out += [""]

    deleted = sorted(
        p for p in ref_files - tgt_files if "/blocks/" in p or "/static/" in p
    )
    deleted_total = len(deleted)
    out += ["## Deleted edition-1 files", ""]
    out += [f"- `{p}`" for p in deleted] if deleted else ["None."]
    report = "\n".join(out) + "\n"

    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(report)
    else:
        sys.stdout.write(report)
    return 1 if deleted_total else 0


if __name__ == "__main__":
    raise SystemExit(main())
