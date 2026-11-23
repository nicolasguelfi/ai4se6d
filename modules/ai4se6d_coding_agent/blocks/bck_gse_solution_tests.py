"""Slide — CCSET07: how GSE-One handles tests (concept only, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from gse_solution import gse_solution, CMD


class BlockStyles:
    """Layout and styles come from the shared gse_solution component."""
bs = BlockStyles


_NOTES = [
    ("The message",
     "An agent can write code that looks right, and tests that prove nothing. GSE-One makes tests a step with "
     "its own evidence."),
    ("Strategy first",
     "/gse-tests sets a test strategy from the requirements before any code: which levels, which cases."),
    ("Production",
     "/gse-produce builds each task on its own branch and runs the tests; the results are kept as evidence — "
     "one branch per task, as in the demo."),
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
             "which levels, which cases."),
            ((CMD, "/gse-produce"), " builds each task on its own branch and runs the tests; "
             "the results are kept as evidence."),
            "Delivery is blocked while a requirement's tests have not been run and passed.",
        ],
        notes=_NOTES,
        zoom=92,   # fills the slide (default 60 left the lower half empty) — NG, 2026-11-23
    )
