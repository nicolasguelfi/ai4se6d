"""Slide — CCSET02: how GSE-One keeps the human in the loop (concept only, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from gse_solution import gse_solution, CMD


class BlockStyles:
    """Layout and styles come from the shared gse_solution component."""
bs = BlockStyles


def build():
    gse_solution(
        cycle="CCSET02 · From VibeCoding to VibeEngineering",
        label="GSE-One solution — human in the loop",
        problem="Vibe coding hands every decision to the agent: insecure code, "
                "hallucinated packages, technical debt, found out too late.",
        solution=[
            ("Each decision is classified: ", (CMD, "Auto"), " (the agent acts), ",
             (CMD, "Inform"), " (it acts and tells you) or ", (CMD, "Gate"), " (it stops and waits for you)."),
            "Risky decisions are always Gates: the agent shows the options and their consequences, you choose.",
            "Guardrails block dangerous actions before they happen.",
            "The six VibeEngineering principles become the steps of one lifecycle: "
            "requirements, design, tests, production, review, delivery.",
        ],
    )
