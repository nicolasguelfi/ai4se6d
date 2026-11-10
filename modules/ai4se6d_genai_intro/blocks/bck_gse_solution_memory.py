"""Slide — CCSET01: how GSE-One solves the "no memory" problem (concept only, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from gse_solution import gse_solution, CMD


class BlockStyles:
    """Layout and styles come from the shared gse_solution component."""
bs = BlockStyles


def build():
    gse_solution(
        cycle="CCSET01 · Generative AI: from LLM to agent",
        label="GSE-One solution — project memory",
        problem="The model has no memory: every new session starts from zero, "
                "and a long session overflows the context window.",
        solution=[
            ("The project memory is written in files, in the ", (CMD, ".gse/"),
             " folder: status, plan, decisions, backlog."),
            "Every new session reads them back and continues where you stopped.",
            ("A profile (", (CMD, "profile.yaml"), ") tells the agent who you are and how to talk to you."),
            "These files are committed with the code: the memory travels with the project, not with the chat.",
        ],
    )
