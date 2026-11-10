"""Slide — CCSET13: how GSE-One measures quality (concept only, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from gse_solution import gse_solution, CMD


class BlockStyles:
    """Layout and styles come from the shared gse_solution component."""
bs = BlockStyles


def build():
    gse_solution(
        cycle="CCSET13 · Measuring quality",
        label="GSE-One solution — health",
        problem="The agent says \"done\"; nothing says how healthy the project is.",
        solution=[
            ((CMD, "/gse-health"), " scores the project on up to 8 dimensions: tests passing, "
             "review findings, git hygiene, requirements coverage, traceability…"),
            "In Lightweight mode it keeps 3 of them: tests, review findings, git hygiene.",
            "Tests leave evidence; the review reads the results of your tools, not the agent's word.",
        ],
        foot="Now: exercise E15.",
    )
