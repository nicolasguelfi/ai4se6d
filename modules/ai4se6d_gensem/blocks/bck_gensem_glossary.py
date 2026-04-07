"""Glossary — Comprehensive glossary of key terms used across all training modules."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Glossary slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    term = Style.create(
        s.project.colors.primary + s.bold + s.Large,
        "gs_glossary_term",
    )
    definition = Style.create(
        s.Large,
        "gs_glossary_def",
    )
    separator = Style.create(
        s.project.colors.muted + s.Large,
        "gs_glossary_sep",
    )
bs = BlockStyles

# Comprehensive glossary — sorted alphabetically, covers all modules
_ENTRIES = [
    ("ACI", "Agent-Computer Interface \u2014 structured protocols for AI agents to interact with tools and environments"),
    ("Agent Mode", "IDE mode where AI autonomously executes multi-step tasks (file edits, terminal, tool calls)"),
    ("AGENTS.md", "Linux Foundation standard for tool-agnostic project rules, enabling cross-tool portability"),
    ("AgileGen", "Framework formalizing agile for AI-augmented development using Gherkin as semantic bridge"),
    ("AI", "Artificial Intelligence"),
    ("Automation Bias", "Tendency to over-rely on AI output, reducing critical review \u2014 especially risky for novices"),
    ("BDD", "Behavior-Driven Development \u2014 specifying behavior in Given/When/Then format"),
    ("CE", "Compound Engineering \u2014 5-phase composable workflow (Brainstorm, Plan, Work, Review, Compound)"),
    ("CHOP", "Chat-Oriented Programming \u2014 multi-turn conversational interaction with LLMs (33-37% of interactions)"),
    ("CI/CD", "Continuous Integration / Continuous Deployment"),
    ("Context Engineering", "Systematic management of all information fed to AI: rules, memory, tools, code. Replaces 'prompt engineering'"),
    ("Foundation Model", "Model pre-trained on very large datasets, adapted via fine-tuning or prompting"),
    ("GenAI", "Generative Artificial Intelligence \u2014 AI that creates new content rather than classifying existing data"),
    ("GenSEM", "Generative Software Engineering Methods \u2014 SE methodologies adapted for AI-assisted development"),
    ("GenSEMOne", "Lightweight, Cursor-native GenSEM variant mapping CE principles to native IDE features"),
    ("GPT", "Generative Pre-trained Transformer"),
    ("Hallucination", "AI generating plausible but incorrect output \u2014 includes package hallucinations (5.2-21.7%)"),
    ("HHH", "Helpful, Harmless, Honest \u2014 alignment criteria for LLMs"),
    ("Homogenization", "LLM-assisted solutions converging toward similar patterns, reducing diversity"),
    ("Hooks", "Event-triggered commands in AI tools for process enforcement (pre-commit checks, quality gates)"),
    ("LLM", "Large Language Model \u2014 neural network trained on text to generate human-like language"),
    ("MAS", "Multi-Agent System \u2014 multiple AI agents collaborating on SE tasks"),
    ("MCP", "Model Context Protocol \u2014 open protocol connecting AI agents to external tools and data sources"),
    ("NFR", "Non-Functional Requirement \u2014 quality attribute (performance, security, accessibility)"),
    ("Promptware Eng.", "Applying SE lifecycle practices to prompt-based systems (Chen et al.)"),
    ("RAG", "Retrieval-Augmented Generation \u2014 combining LLMs with external knowledge retrieval"),
    ("RLHF", "Reinforcement Learning from Human Feedback"),
    ("SDLC", "Software Development Life Cycle"),
    ("SE 3.0", "Intent-centric, conversation-oriented SE paradigm (Hassan et al.)"),
    ("SOP", "Standard Operating Procedure \u2014 encoded workflow discipline in multi-agent systems"),
    ("TDD", "Test-Driven Development \u2014 write tests before implementation (Red-Green-Refactor)"),
    ("Traceability", "Linking every artifact (requirement, test, code, review) to its origin and verification"),
    ("V-Bounce", "AI-native SDLC: humans validate at V-model checkpoints, AI implements between them"),
    ("V&V", "Verification and Validation \u2014 ensuring software meets specs and user needs"),
    ("VibeCoding", "Developers describe intent to AI, accept generated code without close review (Karpathy, 2025)"),
    ("VibeEngineering", "Reintroducing systematic SE practices (requirements, TDD, architecture) to AI-assisted dev"),
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
