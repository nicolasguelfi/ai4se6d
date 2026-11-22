"""Slide — CCSET03: GSE-One is a plugin for several coding agents (concept only, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from gse_solution import gse_solution, CMD


class BlockStyles:
    """Layout and styles come from the shared gse_solution component."""
bs = BlockStyles


_NOTES = [
    ("The message",
     "Every coding agent has its own settings and commands; rules set in one are lost in the next. GSE-One is a "
     "plugin: the method moves with you from one agent to another."),
    ("Which agents",
     "The same rules, commands and specialised agents for opencode, Claude Code, Cursor, Codex CLI and Gemini CLI."),
    ("In opencode",
     "Its rules live in AGENTS.md (the project rules seen on « opencode — Our Tool ») and its commands start with "
     "/gse-."),
    ("Guardrails",
     "They act before the agent does: a commit straight on main is blocked, a force push is intercepted."),
    ("When",
     "Installed this afternoon, used from day 3. This slide is the concept only: no demo yet."),
]


def build():
    gse_solution(
        cycle="CCSET03 · The tools ecosystem, the AI Act, practical rules",
        label="GSE-One solution — one method, many agents",
        problem="Every coding agent has its own settings and commands, "
                "and the rules you set in one are lost in the next.",
        solution=[
            "GSE-One is a plugin: the same rules, commands and specialised agents "
            "for opencode, Claude Code, Cursor, Codex CLI and Gemini CLI.",
            ("In opencode, its rules live in ", (CMD, "AGENTS.md"), " and its commands start with ",
             (CMD, "/gse-"), "."),
            "Its guardrails act before the agent does: a commit straight on main is blocked, "
            "a force push is intercepted.",
        ],
        foot="You install it this afternoon. You use it from day 3.",
        notes=_NOTES,
        zoom=82,   # fills the slide (default 60 left the lower half empty) — NG, 2026-11-23
    )
