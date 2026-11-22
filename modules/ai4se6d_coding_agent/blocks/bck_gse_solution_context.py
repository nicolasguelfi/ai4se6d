"""Slide — CCSET05: how GSE-One manages the agent's context (concept only, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from gse_solution import gse_solution, CMD


class BlockStyles:
    """Layout and styles come from the shared gse_solution component."""
bs = BlockStyles


def build():
    gse_solution(
        cycle="CCSET05 · Driving an agent: context engineering",
        label="GSE-One solution — context",
        problem="The agent only knows what is in its context. Re-explaining "
                "your project at every session wastes time and tokens.",
        solution=[
            ("GSE-One is itself a standing prompt: its orchestrator is an ", (CMD, "AGENTS.md"),
             " loaded at every session."),
            ("Each activity is a command (", (CMD, "/gse-plan"), ", ", (CMD, "/gse-tests"),
             ", …) that loads only what it needs."),
            "Specialised agents bring one point of view each: architect, code reviewer, "
            "security auditor, test strategist…",
            "The project state lives in files: the context is rebuilt from them, not from the chat.",
        ],
    )
