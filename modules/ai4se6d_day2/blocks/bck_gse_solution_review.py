"""Slide — CCSET08: how GSE-One handles review and delivery (concept only, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from gse_solution import gse_solution, CMD


class BlockStyles:
    """Layout and styles come from the shared gse_solution component."""
bs = BlockStyles


def build():
    gse_solution(
        cycle="CCSET08 · Code review, living documentation, delivery",
        label="GSE-One solution — review and delivery",
        problem="AI review is fast but uneven: it misses some problems, invents others, "
                "and nobody decides what to do with its findings.",
        solution=[
            ((CMD, "/gse-review"), " numbers each finding (RVW-…) and ranks it HIGH, MEDIUM or LOW: "
             "the scale you use today."),
            "Several specialised reviewers read the same change: code, architecture, security, "
            "tests, requirements, devil's advocate.",
            ((CMD, "/gse-fix"), " fixes the findings you keep; you refuse the others with a reason."),
            ((CMD, "/gse-deliver"), " will not merge over an open HIGH finding without your explicit decision."),
        ],
    )
