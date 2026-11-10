"""Slide — CCSET06: how GSE-One plans the work (concept only, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from gse_solution import gse_solution, CMD


class BlockStyles:
    """Layout and styles come from the shared gse_solution component."""
bs = BlockStyles


def build():
    gse_solution(
        cycle="CCSET06 · Technical planning",
        label="GSE-One solution — planning",
        problem="A vague request gives a vague result. Without a written plan of small, "
                "testable tasks, the agent decides the scope for you.",
        solution=[
            ((CMD, "/gse-reqs"), " starts with a conversation, then writes requirements "
             "with testable acceptance criteria (Given / When / Then)."),
            ((CMD, "/gse-plan"), " turns them into a sprint of tasks, each sized in complexity points, "
             "within a budget."),
            "The plan is a Gate: nothing is built before you validate it.",
            "Ideas that do not fit go to the backlog, not into the code.",
        ],
    )
