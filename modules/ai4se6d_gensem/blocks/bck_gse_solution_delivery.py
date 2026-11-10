"""Slide — CCSET14: how GSE-One delivers and capitalises (concept only, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from gse_solution import gse_solution, CMD


class BlockStyles:
    """Layout and styles come from the shared gse_solution component."""
bs = BlockStyles


def build():
    gse_solution(
        cycle="CCSET14 · Delivery, maintenance, capitalisation",
        label="GSE-One solution — delivery and learning",
        problem="Delivery is rushed, nobody knows what was shipped, and the lessons vanish with the session.",
        solution=[
            ((CMD, "/gse-fix"), " fixes the findings you keep, test first, each on its branch."),
            ((CMD, "/gse-deliver"), ": the merge strategy is a Gate; a tag, a change log; "
             "no delivery over an open HIGH finding or untested requirement without your decision."),
            ((CMD, "/gse-compound"), " captures lessons on three axes: the project, the method, your competencies."),
            ((CMD, "/gse-pause"), " and ", (CMD, "/gse-resume"), " keep the thread between sessions; ",
             (CMD, "/gse-backlog"), " keeps ideas for later."),
        ],
        foot="Now: exercise E16.",
    )
