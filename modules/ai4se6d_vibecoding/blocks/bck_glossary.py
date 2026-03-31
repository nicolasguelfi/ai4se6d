"""Glossary — Key terms and abbreviations used in this presentation."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t
from custom.styles import Styles as s


# Viewport-filling container
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:flex-start;"
    "min-height:85vh;gap:1rem;",
    "page_fill_vc_glossary",
)


class BlockStyles:
    """Glossary slide styles."""
    heading = s.project.titles.section_title + s.center_txt
    term = Style.create(
        s.project.colors.primary + s.bold + s.Large,
        "vc_glossary_term",
    )
    definition = Style.create(
        s.Large,
        "vc_glossary_def",
    )
    separator = Style.create(
        s.project.colors.muted + s.Large,
        "vc_glossary_sep",
    )
bs = BlockStyles


# ── Glossary entries: (term, definition) ─────────────────────────────
_ENTRIES = [
    ("AI", "Artificial Intelligence"),
    ("GenAI", "Generative AI"),
    ("LLM", "Large Language Model"),
    ("GPT", "Generative Pre-trained Transformer"),
    ("NLU", "Natural Language Understanding"),
    ("RLHF", "Reinforcement Learning from Human Feedback"),
    ("HHH", "Helpful, Harmless, Honest"),
    ("DALL-E", "OpenAI\u2019s image generation model"),
    ("RAG", "Retrieval-Augmented Generation"),
    ("Foundation model", "Model pretrained on very large datasets"),
    ("VibeCoding", "Intent-driven development with AI as pair programmer"),
    ("VibeEngineering", "Engineering discipline integrating AI across the full SDLC"),
    ("TDD", "Test-Driven Development"),
    ("BDD", "Behavior-Driven Development"),
    ("CI/CD", "Continuous Integration / Continuous Deployment"),
    ("Context Engineering", "Systematic management of information fed to AI tools, beyond clever prompting"),
    ("NFR", "Non-Functional Requirement — quality attribute such as performance, security, maintainability"),
    ("V&V", "Verification and Validation — ensuring software meets specs (verification) and user needs (validation)"),
    ("MCP", "Model Context Protocol — standard for integrating external tools with AI agents"),
]


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Glossary", tag=t.div, toc_lvl="1")
            st_space("v", 1)

    with st_block(_page_fill):
        for term, definition in _ENTRIES:
            st_write(
                bs.definition,
                (bs.term, term),
                (bs.separator, " \u2014 "),
                (bs.definition, definition),
            )
            st_space("v", 0.5)
