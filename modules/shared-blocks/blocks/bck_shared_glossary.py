"""Glossary — Comprehensive glossary shared across all training modules.

This block is designed to be included at the end of any module via shared-blocks.
It covers terms from all modules: genai_intro, vibecoding, gensem.
"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Glossary slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    term = Style.create(
        s.project.colors.primary + s.bold + s.Large,
        "shared_glossary_term",
    )
    definition = Style.create(
        s.Large,
        "shared_glossary_def",
    )
    separator = Style.create(
        s.project.colors.muted + s.Large,
        "shared_glossary_sep",
    )
bs = BlockStyles


# ── Glossary entries: (term, definition) ─────────────────────────────
# Sorted alphabetically. Covers all modules.
_ENTRIES = [
    ("ACI", "Agent-Computer Interface \u2014 structured protocols for AI agents to interact with development tools and environments"),
    ("Agent Mode", "IDE mode where AI autonomously executes multi-step tasks (file edits, terminal commands, tool calls)"),
    ("AGENTS.md", "Linux Foundation standard for tool-agnostic project rules, enabling cross-tool portability"),
    ("AgileGen", "Framework formalizing agile for AI-augmented development using Gherkin as semantic bridge"),
    ("AI", "Artificial Intelligence"),
    ("Automation Bias", "Tendency to over-rely on AI output, reducing critical review \u2014 especially risky for novice developers"),
    ("BDD", "Behavior-Driven Development \u2014 specifying behavior in Given/When/Then format before implementation"),
    ("CE", "Compound Engineering \u2014 5-phase composable workflow (Brainstorm, Plan, Work, Review, Compound)"),
    ("CHOP", "Chat-Oriented Programming \u2014 multi-turn conversational interaction with LLMs for code generation (33-37% of interactions)"),
    ("CI/CD", "Continuous Integration / Continuous Deployment"),
    ("Context Engineering", "Systematic management of all information fed to AI: project rules, memory, tools, relevant code. Replaces 'prompt engineering'"),
    ("DALL-E", "OpenAI\u2019s image generation model"),
    ("Foundation Model", "Model pre-trained on very large datasets, adapted to specific tasks via fine-tuning or prompting"),
    ("GenAI", "Generative Artificial Intelligence \u2014 AI that creates new content (text, code, images) rather than classifying existing data"),
    ("GenSEM", "Generative Software Engineering Methods \u2014 the study of SE methodologies adapted for AI-assisted development"),
    ("GenSEMOne", "Lightweight, Cursor-native GenSEM variant mapping CE principles to native IDE features"),
    ("GPT", "Generative Pre-trained Transformer"),
    ("Hallucination", "AI generating plausible but incorrect output \u2014 includes code hallucinations and package hallucinations (5.2-21.7%)"),
    ("HHH", "Helpful, Harmless, Honest \u2014 alignment criteria for LLMs"),
    ("Hooks", "Event-triggered shell commands in AI coding tools for process enforcement (e.g., pre-commit checks, quality gates)"),
    ("Homogenization Effect", "LLM-assisted solutions converging toward similar patterns, reducing solution diversity"),
    ("LLM", "Large Language Model \u2014 neural network trained on text to generate human-like language"),
    ("MAS", "Multi-Agent System \u2014 architecture where multiple AI agents collaborate on SE tasks"),
    ("MCP", "Model Context Protocol \u2014 open protocol connecting AI agents to external tools and data sources"),
    ("NFR", "Non-Functional Requirement \u2014 quality attribute such as performance, security, accessibility, maintainability"),
    ("NLU", "Natural Language Understanding"),
    ("Promptware Engineering", "Applying SE lifecycle practices (requirements, testing, maintenance) to prompt-based systems"),
    ("RAG", "Retrieval-Augmented Generation \u2014 combining LLMs with external knowledge retrieval for more accurate output"),
    ("RLHF", "Reinforcement Learning from Human Feedback"),
    ("SDLC", "Software Development Life Cycle"),
    ("SE 3.0", "Intent-centric, conversation-oriented software development paradigm (Hassan et al.)"),
    ("SOP", "Standard Operating Procedure \u2014 encoded workflow discipline in multi-agent systems (e.g., MetaGPT)"),
    ("TDD", "Test-Driven Development \u2014 write tests before implementation (Red-Green-Refactor)"),
    ("Traceability", "Ability to link every artifact (requirement, test, code, review) back to its origin and forward to its verification"),
    ("V-Bounce", "AI-native SDLC model where humans validate at V-model checkpoints while AI implements between them"),
    ("V&V", "Verification and Validation \u2014 ensuring software meets specs (verification) and user needs (validation)"),
    ("VibeCoding", "Development where developers describe intent to AI and accept generated code without closely reviewing it (Karpathy, 2025)"),
    ("VibeEngineering", "Engineering discipline reintroducing systematic SE practices (requirements, TDD, architecture) to AI-assisted development"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Glossary", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        for term, definition in _ENTRIES:
            st_write(
                bs.definition,
                (bs.term, term),
                (bs.separator, " \u2014 "),
                (bs.definition, definition),
            )
            st_space("v", 0.5)
