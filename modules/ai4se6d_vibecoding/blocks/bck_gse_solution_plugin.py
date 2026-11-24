"""Slide — CCSET03: GSE-One is a plugin for several coding agents (concept only, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from gse_solution import gse_solution, CMD


class BlockStyles:
    """Layout and styles come from the shared gse_solution component."""
bs = BlockStyles


_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Concept only: learners install GSE-One this afternoon (step 5 of the installation) and use it from day 3."),
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
    # Command recap: every command shown on the slide, in plain words (NG, 2026-11-24)
    ("Text — AGENTS.md",
     "Not a command: the project-rules file at the root of the project, read by opencode at the start of every "
     "session. GSE-One writes its rules there; /init (an opencode command) drafts a first version."),
    ("Prompt — /gse- (prefix)",
     "Not a full command: the start shared by all GSE-One commands, typed in opencode's chat (e.g. /gse-status, "
     "« where are we? »). The slash marks a command rather than a request in plain words; typing /gse- shows the "
     "list of GSE-One commands to choose from. They exist only once GSE-One is installed."),
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
