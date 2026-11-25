"""Slide — CCSET06: how GSE-One plans the work (concept only, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from gse_solution import gse_solution, CMD


class BlockStyles:
    """Layout and styles come from the shared gse_solution component."""
bs = BlockStyles


_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Concept only: show how GSE-One plans (/gse-reqs, /gse-plan); learners "
     "use GSE-One from day 3."),
    ("The message",
     "A vague request gives a vague result. Without a written plan of small, testable tasks, the agent decides "
     "the scope for you. GSE-One makes planning a step of its own."),
    ("Requirements",
     "/gse-reqs starts with a conversation, then writes requirements with testable acceptance criteria "
     "(Given / When / Then) — the same idea as your « Accepted when » with the plan agent, written in three "
     "fixed parts."),
    ("Given / When / Then — the three parts",
     "First time in the course: define them. One acceptance criterion = one concrete scenario. Given = the "
     "starting situation (what is already true before the action). When = the one action the user does. Then = "
     "the result we can observe and check. Comes from Behaviour-Driven Development (BDD); each scenario becomes "
     "one acceptance test (this afternoon, and day 4)."),
    ("Given / When / Then — CalcApp, task 1",
     "Given the Add page is open and no expense is saved, When I enter an amount of 0 and click Add, Then an error "
     "message is shown and the list stays empty. A second scenario covers the valid case: Given the Add page is "
     "open, When I enter 25.50 in Food and click Add, Then the list shows one expense of 25.50."),
    ("Plan",
     "/gse-plan turns them into a sprint of tasks, each sized in complexity points, within a budget."),
    ("Gate and backlog",
     "The plan is a Gate: nothing is built before you validate it. Ideas that do not fit go to the backlog, "
     "not into the code."),
    ("Ask the room",
     "« Compare with your docs/plan.md: what would a Gate have changed? »"),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Commands — /gse-reqs, /gse-plan",
     "GSE-One commands, typed in the agent's prompt box like /new: /gse-reqs = write the requirements, /gse-plan ="
     " turn them into tasks. Used from day 3 — nothing to type today."),
]


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
        notes=_NOTES,
        zoom=92,   # fills the slide (default 60 left the lower half empty) — NG, 2026-11-23
    )
