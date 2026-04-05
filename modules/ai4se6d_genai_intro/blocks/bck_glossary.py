"""Glossary — Key terms and abbreviations used in this presentation."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Glossary slide styles."""
    heading = s.project.titles.section_title + s.center_txt
    term = Style.create(
        s.project.colors.primary + s.bold + s.Large,
        "glossary_term",
    )
    definition = Style.create(
        s.Large,
        "glossary_def",
    )
    separator = Style.create(
        s.project.colors.muted + s.Large,
        "glossary_sep",
    )
bs = BlockStyles


# ── Glossary entries: (term, definition) ─────────────────────────────
_ENTRIES = [
    ("AI", "Artificial Intelligence — field of computer science focused on creating systems that perform tasks requiring human intelligence"),
    ("GenAI", "Generative AI — AI systems that create new content (text, images, code) rather than just classifying or predicting"),
    ("LLM", "Large Language Model — neural network trained on massive text corpora to understand and generate language (e.g. GPT, Claude, Gemini)"),
    ("GPT", "Generative Pre-trained Transformer — OpenAI's family of large language models"),
    ("NLU", "Natural Language Understanding — ability of a system to comprehend human language"),
    ("RLHF", "Reinforcement Learning from Human Feedback — training technique where human preferences guide model alignment"),
    ("HHH", "Helpful, Harmless, Honest — Anthropic's alignment principles for AI systems"),
    ("DALL-E", "OpenAI's image generation model that creates images from text descriptions"),
    ("RAG", "Retrieval-Augmented Generation — technique combining LLM generation with external knowledge retrieval"),
    ("Foundation model", "Model pretrained on very large datasets, adapted to many tasks (e.g. GPT-4, Claude, Gemini)"),
    ("VibeCoding", "Intent-driven development paradigm where AI acts as your pair programmer, generating code from natural language descriptions"),
    ("VibeEngineering", "Broader engineering discipline that integrates AI tools across the full software development lifecycle"),
]


def build():
    with st_block(s.center_txt):
        st_write(bs.heading, "Glossary", tag=t.div, toc_lvl="1")
        st_space("v", 1)

    for term, definition in _ENTRIES:
        st_write(
            bs.definition,
            (bs.term, term),
            (bs.separator, " — "),
            (bs.definition, definition.split(" — ", 1)[1] if " — " in definition else definition),
        )
        st_space("v", 0.5)
