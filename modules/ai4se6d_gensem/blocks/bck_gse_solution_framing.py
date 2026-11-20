"""Slide — CCSET15: how GSE-One fits the method to a small project (concept only, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from gse_solution import gse_solution, CMD


class BlockStyles:
    """Layout and styles come from the shared gse_solution component."""
bs = BlockStyles


def build():
    gse_solution(
        cycle="CCSET15 · Framing a project",
        label="GSE-One solution — sizing the method",
        problem="A full method on a one-day project costs more than it gives; no method lets the scope explode.",
        solution=[
            ("The ", (CMD, "Lightweight"), " mode runs a shorter cycle with fewer Gates: "
             "plan → requirements → production → delivery — no review, fix or capitalisation step."),
            ("Its net: ", (CMD, "/gse-deliver"), " runs a minimal integrity check (devil's advocate, at most 5 "
             "findings); a HIGH finding stops the merge until you decide."),
            "The sprint has a complexity budget: what does not fit goes to the backlog.",
            ((CMD, "/gse-go --adopt"), " brings an existing project under GSE-One without starting again."),
        ],
        foot="Now: exercises E17 and E18.",
    )
