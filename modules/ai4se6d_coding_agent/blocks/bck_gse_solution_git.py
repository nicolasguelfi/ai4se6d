"""Slide — CCSET04: how GSE-One uses git as a safety net (concept only, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from gse_solution import gse_solution, CMD


class BlockStyles:
    """Layout and styles come from the shared gse_solution component."""
bs = BlockStyles


def build():
    gse_solution(
        cycle="CCSET04 · Configuration management: git as a safety net",
        label="GSE-One solution — git",
        problem="An agent edits many files at once. Without git, a bad change "
                "is hard to see and harder to undo.",
        solution=[
            "One branch per task: the agent never works directly on main.",
            ("Before a risky operation, a safety tag ", (CMD, "gse-backup/…"), " marks where to go back."),
            "A guardrail blocks a commit straight on main.",
            "Commit messages follow one convention, so the history tells the story.",
        ],
    )
