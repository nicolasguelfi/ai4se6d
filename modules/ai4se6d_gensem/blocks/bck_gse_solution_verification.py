"""Slide — CCSET12: how GSE-One handles verification and validation (concept only, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from gse_solution import gse_solution, CMD


class BlockStyles:
    """Layout and styles come from the shared gse_solution component."""
bs = BlockStyles


def build():
    gse_solution(
        cycle="CCSET12 · Verification and validation",
        label="GSE-One solution — verification and validation",
        problem="Tests written after the code, by the same agent, check what was built — not what was asked.",
        solution=[
            ((CMD, "/gse-tests"), " derives a test strategy from the requirements first: "
             "verification and validation, level by level."),
            "Validation tests trace to the requirements, verification tests to the design.",
            "Test runs leave evidence; delivery is blocked while a requirement's tests have not passed.",
            ((CMD, "/gse-review"), " is the static side: several reviewers, findings ranked HIGH / MEDIUM / LOW."),
        ],
        foot="Tomorrow morning: exercise E14.",
    )
