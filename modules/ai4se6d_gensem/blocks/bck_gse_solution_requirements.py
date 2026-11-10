"""Slide — CCSET10: how GSE-One elicits requirements (concept only, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from gse_solution import gse_solution, CMD


class BlockStyles:
    """Layout and styles come from the shared gse_solution component."""
bs = BlockStyles


def build():
    gse_solution(
        cycle="CCSET10 · Requirements elicitation",
        label="GSE-One solution — requirements",
        problem="Requirements left implicit are decided by the agent, and nobody can check them later.",
        solution=[
            ((CMD, "/gse-reqs"), " starts with a conversation in plain language, before any formal writing."),
            "Each requirement gets an identifier (REQ-…) and testable acceptance criteria (Given / When / Then).",
            "Every requirement is linked to the tasks and tests that cover it: that link is traceability.",
            "The requirements are validated at a Gate before design starts.",
        ],
        foot="This afternoon: exercise E13.",
    )
