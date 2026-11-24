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
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Symbol — /gse-… commands",
     "Typed in opencode's input box, not in the terminal: a message starting with / runs a command; the GSE-One "
     "plugin adds the /gse-… ones (typing / shows the list). Each accepts --help for its options."),
    ("Command — /gse-review (GSE-One, day 3)",
     "Reviews the current sprint's work on its branches: numbered findings RVW-…, ranked HIGH / MEDIUM / LOW, "
     "then a devil's advocate pass. --task TASK-ID = one task; --severity HIGH = only the serious ones."),
    ("Command — /gse-fix (GSE-One, day 3)",
     "Fixes the review findings on a separate branch. --finding RVW-001 = one finding; --severity HIGH = only the"
     " serious ones; --dry-run = show the fix plan without changing anything."),
    ("Command — /gse-deliver (GSE-One, day 3)",
     "Merges the finished task branches, tags the release, cleans up the branches (after creating backup tags). "
     "It first checks for open HIGH findings and stops for your decision. --dry-run shows the plan; --skip-tag "
     "skips the tag."),
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
