"""Slide — CCSET11: how GSE-One handles non-functional requirements (concept only, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from gse_solution import gse_solution, CMD


class BlockStyles:
    """Layout and styles come from the shared gse_solution component."""
bs = BlockStyles


def build():
    gse_solution(
        cycle="CCSET11 · Non-functional requirements",
        label="GSE-One solution — qualities",
        problem="Qualities nobody asked for are not built, and not tested.",
        solution=[
            ((CMD, "/gse-reqs"), " asks for the qualities too, and writes them as requirements with a measure."),
            "It ends with a checklist inspired by ISO 25010: are the qualities complete and measurable?",
            ((CMD, "/gse-design"), " records each design decision with its reason and the qualities it serves."),
            "The review checks them again: performance, security, accessibility.",
        ],
        foot="This afternoon: exercise E13.",
    )
