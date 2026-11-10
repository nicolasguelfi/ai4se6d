"""Slide — CCSET09: the GenSEM chosen for this course, GSE-One (concept only, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from gse_solution import gse_solution, CMD


class BlockStyles:
    """Layout and styles come from the shared gse_solution component."""
bs = BlockStyles


def build():
    gse_solution(
        cycle="CCSET09 · Software engineering concepts, defining your GenSEM",
        label="GSE-One solution — the method",
        problem="Without an explicit method, every session reinvents the lifecycle, "
                "and the agent decides what you forgot to decide.",
        solution=[
            "16 principles, among them: artefacts are everything, the human in the loop, "
            "risk classification, agent fallibility.",
            "One lifecycle per sprint: collect → assess → plan → requirements → design → preview → tests → "
            "production → review → fix → delivery → capitalisation.",
            ("Three modes sized to the project: ", (CMD, "Full"), " (CalcApp), ",
             (CMD, "Lightweight"), " (your mini-project), ", (CMD, "Micro"), "."),
            "Gates where you decide, with a 3-question grid — next slide.",
        ],
        foot="This afternoon you use it on your CalcApp.",
    )
