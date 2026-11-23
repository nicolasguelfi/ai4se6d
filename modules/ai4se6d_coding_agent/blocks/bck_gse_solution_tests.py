"""Slide — CCSET07: how GSE-One handles tests (concept only, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from gse_solution import gse_solution, CMD


class BlockStyles:
    """Layout and styles come from the shared gse_solution component."""
bs = BlockStyles


_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Concept only (CCSET07): learners use /gse-tests and /gse-produce"
     " from day 3."),
    ("The message",
     "An agent can write code that looks right, and tests that prove nothing. GSE-One makes tests a step with "
     "its own evidence."),
    ("Strategy first",
     "/gse-tests sets a test strategy from the requirements before any code: which levels, which cases, one "
     "acceptance (validation) test per Given/When/Then criterion."),
    ("Production",
     "/gse-produce builds each code task on its own branch as in the demo: the acceptance test first, run and "
     "seen failing, committed; then the code until it passes. The results are kept as evidence."),
    ("Delivery is blocked",
     "While a requirement's tests have not been run and passed, delivery is blocked."),
    ("Ask the room",
     "« In the demo, what proved that the task was done? »"),
]


def build():
    gse_solution(
        cycle="CCSET07 · Testing with AI",
        label="GSE-One solution — tests",
        problem="An agent can write code that looks right, and tests that prove nothing.",
        solution=[
            ((CMD, "/gse-tests"), " sets a test strategy from the requirements before any code: "
             "which levels, which acceptance tests."),
            ((CMD, "/gse-produce"), ", for each code task: the acceptance test first, seen failing, "
             "then the code — on its own branch, results kept as evidence."),
            "Delivery is blocked while a requirement's tests have not been run and passed.",
        ],
        notes=_NOTES,
        zoom=92,   # fills the slide (default 60 left the lower half empty) — NG, 2026-11-23
    )
