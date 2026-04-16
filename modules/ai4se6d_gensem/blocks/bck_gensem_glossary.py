"""Glossary — Comprehensive glossary of key terms used across all training modules."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


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
    ("CHOP", "Chat-Oriented Programming \u2014 multi-turn conversational interaction with LLMs (33-37% of interactions)"),
    ("CI/CD", "Continuous Integration / Continuous Deployment"),
    ("Complexity Budget", "Sprint capacity measured in points \u2014 utility dep 1pt, framework 2-3pts, architectural 3-5pts. Warn at 80%, Gate at 100%"),
    ("Context Engineering", "Systematic management of all information fed to AI: rules, memory, tools, code. Replaces 'prompt engineering'"),
    ("Foundation Model", "Model pre-trained on very large datasets, adapted via fine-tuning or prompting"),
    ("Gate", "High-risk decision requiring full analysis and human validation before proceeding"),
    ("GenAI", "Generative Artificial Intelligence \u2014 AI that creates new content rather than classifying existing data"),
    ("GenSEM", "Generative Software Engineering Methods \u2014 SE methodologies adapted for AI-assisted development"),
    ("GPT", "Generative Pre-trained Transformer"),
    ("GSE-One", "Generative Software Engineering One \u2014 complete methodology with 16 principles, 4 lifecycle stages, 23 commands, 9 agents"),
    ("Hallucination", "AI generating plausible but incorrect output \u2014 includes package hallucinations (5.2-21.7%)"),
    ("Health Dashboard", "8-dimension quality monitor: REQ Coverage, Test Pass, Design Debt, Findings, Budget, Traceability, Git Hygiene, AI Integrity"),
    ("HHH", "Helpful, Harmless, Honest \u2014 alignment criteria for LLMs"),
    ("Homogenization", "LLM-assisted solutions converging toward similar patterns, reducing diversity"),
    ("Hooks", "Event-triggered commands in AI tools for process enforcement (pre-commit checks, quality gates)"),
    ("HUG", "Human Understanding Gathering \u2014 /gse:hug captures developer profile across 11 dimensions"),
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
    ("Worktree", "Git worktree providing isolated working directory per task \u2014 main always stays stable"),
]


def build():
    st_marker("Glossary")
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "Glossary", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Glossary",
                        entries=[
                            ("Scope", "Covers all key terms from GenAI fundamentals through VibeCoding to GSE-One methodology."),
                            ("Usage", "Reference this glossary when encountering unfamiliar acronyms or concepts in the training."),
                            ("New in GSE-One", "Terms like Gate, Complexity Budget, Health Dashboard, HUG, and Worktree are GSE-One specific."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
        st_space("v", 1)

        with st_zoom(120):
            for term, definition in _ENTRIES:
                st_write(
                    bs.definition,
                    (bs.term, term),
                    (bs.separator, " \u2014 "),
                    (bs.definition, definition),
                )
                st_space("v", 0.5)
