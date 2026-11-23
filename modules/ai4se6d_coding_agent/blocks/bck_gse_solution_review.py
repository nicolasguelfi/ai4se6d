"""Slide — CCSET08: how GSE-One handles review and delivery (concept only, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from gse_solution import gse_solution, CMD


class BlockStyles:
    """Layout and styles come from the shared gse_solution component."""
bs = BlockStyles


_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Concept only (CCSET08): learners use /gse-review and /gse-fix "
     "from day 3."),
    ("The message",
     "AI review is fast but uneven: it misses some problems, invents others, and nobody decides what to do with "
     "its findings. GSE-One turns the review into numbered findings that you decide on."),
    ("/gse-review",
     "Numbers each finding (RVW-…) and ranks it HIGH, MEDIUM or LOW — the scale used in today's review exercise. "
     "Several specialised reviewers read the same change: code, architecture, security, tests, requirements, "
     "devil's advocate."),
    ("/gse-fix and /gse-deliver",
     "/gse-fix fixes the findings you keep; you refuse the others with a reason. /gse-deliver will not merge over "
     "an open HIGH finding without your explicit decision."),
    ("Link to Day 3",
     "This is the same loop you run by hand this afternoon: review, triage, fix test first, refuse with a reason, "
     "ship."),
    ("Ask the room",
     "« Which reviewer of the list would have caught the problem you missed today? »"),
]


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
        notes=_NOTES,
        zoom=82,   # fills the slide (default 60 left the lower half empty) — NG, 2026-11-23
    )
