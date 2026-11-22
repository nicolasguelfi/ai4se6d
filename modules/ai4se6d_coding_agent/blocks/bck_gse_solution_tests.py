"""Slide — CCSET07: how GSE-One handles tests (concept only, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from gse_solution import gse_solution, CMD


class BlockStyles:
    """Layout and styles come from the shared gse_solution component."""
bs = BlockStyles


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
    )
