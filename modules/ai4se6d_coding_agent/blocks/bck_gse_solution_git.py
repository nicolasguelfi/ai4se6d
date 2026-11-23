"""Slide — CCSET04: how GSE-One uses git as a safety net (concept only, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from gse_solution import gse_solution, CMD


class BlockStyles:
    """Layout and styles come from the shared gse_solution component."""
bs = BlockStyles


_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Concept only: show how GSE-One automates the three Git habits; learners "
     "use GSE-One from day 3."),
    ("The message",
     "The three Git habits of this session — one branch per task, a checkpoint before a risky change, names that "
     "tell the story — are what GSE-One applies for you."),
    ("Branch per task",
     "The agent never works directly on main: each task gets its own branch, and a guardrail blocks a commit "
     "straight on main."),
    ("Safety tag",
     "Before a risky operation, a tag gse-backup/… marks where to go back — the checkpoint commit, automated."),
    ("Convention",
     "Commit messages follow one convention, so the history tells the story."),
    ("Ask the room",
     "« Which of the three habits are you most likely to forget without a tool? »"),
]


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
        notes=_NOTES,
        zoom=95,   # fills the slide (default 60 left the lower half empty) — NG, 2026-11-23
    )
