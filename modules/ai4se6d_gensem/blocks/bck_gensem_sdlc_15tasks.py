"""Slides 3-6 — 15 Core Tasks in 4 slides: NEW, ELEVATED, TRANSFORMED (1/2), TRANSFORMED (2/2)."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: task-card
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_page_fill = s.project.containers.page_fill_top

# Emoji marker for tasks specific to generative SE
_GEN = "\U0001f6e1\ufe0f"  # shield emoji


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    sub_new = Style.create(
        s.project.colors.highlight + s.bold + s.Large + s.center_txt,
        "tasks_sub_new",
    )
    sub_elev = Style.create(
        s.project.colors.accent + s.bold + s.Large + s.center_txt,
        "tasks_sub_elev",
    )
    sub_trans = Style.create(
        s.project.colors.primary + s.bold + s.Large + s.center_txt,
        "tasks_sub_trans",
    )
    label_new = Style.create(
        s.project.colors.highlight + s.bold + s.Large, "tasks_lbl_new",
    )
    label_elev = Style.create(
        s.project.colors.accent + s.bold + s.Large, "tasks_lbl_elev",
    )
    label_trans = Style.create(
        s.project.colors.primary + s.bold + s.Large, "tasks_lbl_trans",
    )
    body = Style.create(s.Large + s.text.wrap.hyphens, "tasks_body")
bs = BlockStyles

# Outer cell: card border/radius
_cell_new = s.project.containers.cell_active_bg + s.center_txt
_cell_elev = s.project.containers.cell_accent_bg + s.center_txt
_cell_trans = s.project.containers.cell_primary_bg + s.center_txt

# Header row inside each card: stronger background
_hdr_new = Style.create(
    s.project.containers.cell_active_bg + s.project.containers.cell_pad_sm
    + s.center_txt + Style("background-color: rgba(243,156,18,0.25);", "_hdr_new_bg"),
    "task_hdr_new",
)
_hdr_elev = Style.create(
    s.project.containers.cell_accent_bg + s.project.containers.cell_pad_sm
    + s.center_txt + Style("background-color: rgba(46,196,182,0.30);", "_hdr_elev_bg"),
    "task_hdr_elev",
)
_hdr_trans = Style.create(
    s.project.containers.cell_primary_bg + s.project.containers.cell_pad_sm
    + s.center_txt + Style("background-color: rgba(122,184,245,0.18);", "_hdr_trans_bg"),
    "task_hdr_trans",
)

_desc_cell = s.project.containers.cell_pad_sm + s.center_txt

# Tasks marked with shield are specific to generative SE
_TASKS_NEW = [
    ("T1", "Intent Specification", "Formulate WHAT to build, not HOW", True),
    ("T2", "Context Engineering", "Build the knowledge context for AI agents", True),
    ("T13", "Agent Supervision", "Coordinate and oversee autonomous agents", True),
    ("T14", "Knowledge Curation", "Capitalize and organize acquired knowledge", True),
]

_TASKS_ELEVATED = [
    ("T5", "Code Review & Validation", "Was periodic — now continuous at every generation", True),
    ("T6", "Test Strategy & Generation", "AI generates tests but strategy needs human judgment", False),
    ("T12", "Version Control & Branching", "Multi-file agent changes require structured branching", True),
    ("T15", "Requirements Elicitation", "Conversational elicitation replaces static forms", True),
]

_TASKS_TRANSFORMED = [
    ("T3", "Architecture & Design", "AI proposes, human validates and decides", False),
    ("T4", "Code Gen Orchestration", "Direct multi-agent code production", True),
    ("T7", "Debugging & Diagnosis", "AI identifies root causes, human confirms", False),
    ("T8", "Refactoring & Improvement", "AI refactors but quality must be verified", False),
    ("T9", "Documentation Generation", "Largely automated, human curates", False),
    ("T10", "Dependency & Security Mgmt", "AI detects, human prioritizes remediation", False),
    ("T11", "CI/CD Pipeline Integration", "AI-triggered builds and deployments", False),
]


def _render_group(tasks, cell_style, hdr_style, label_style,zoom=100):
    """Render task cards with 2-row layout: header (colored) + description."""
    with st_grid(
        cols="repeat(auto-fit, minmax(350px, 1fr))",
        gap="16px",
        cell_styles=cell_style,
    ) as g:
        for tid, name, desc, is_gen in tasks:
            with st_zoom(zoom):
                with g.cell():
                    with st_block(hdr_style):
                        prefix = f"{_GEN} {tid}  " if is_gen else f"{tid}  "
                        st_write(
                            bs.body,
                            (label_style, prefix),
                            (bs.body, name),
                        )
                    with st_block(_desc_cell):
                        st_write(bs.body, desc)


def build():
    # Anti-scroll: invisible marker before first content
    st_slide_break(marker_label="15 Core Tasks")

    # ── Slide 3: 4 NEW tasks ───────────────────────────────────────
    with st_block(_page_fill+s.center_txt):
        with st_zoom(90):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    st_write(bs.heading, "15 Core Tasks", tag=t.div, toc_lvl="+1")
                    st_write(bs.sub_new, "4 NEW \u2014 Did not exist before GenAI")
                with g.cell():
                    st_hover_tooltip(
                        title="4 NEW Tasks \u2014 Why they didn't exist before",
                        entries=[
                            ("What changed", "Generative AI created entirely new developer activities that have no equivalent in traditional software engineering."),
                            ("T1 + T2", "Before GenAI, developers coded directly. Now, formulating precise intent (T1) and building the right context for agents (T2) are the primary skills."),
                            ("T13 + T14", "As AI agents become autonomous workers, someone must supervise them (T13) and capture what they learn (T14) \u2014 these roles simply didn't exist."),
                            (_GEN + " Shield icon", "Marks tasks that are specific to generative software engineering."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
        st_space("v", 0)
        _render_group(_TASKS_NEW, _cell_new, _hdr_new, bs.label_new,zoom=90)

    st_slide_break(marker_label="4 ELEVATED Tasks")

    # ── Slide 4: 4 ELEVATED tasks ──────────────────────────────────
    with st_block(_page_fill):
        with st_block(s.center_txt):
            with st_zoom(90):
                with st_grid(
                    cols="95% 5%",
                    gap="0px",
                    cell_styles=s.project.containers.grid_cell_centered,
                ) as g:
                    with g.cell():
                        st_write(bs.heading, "15 Core Tasks", tag=t.div, toc_lvl="+1")
                        st_write(bs.sub_elev, "4 ELEVATED \u2014 Importance dramatically increased")
                    with g.cell():
                        st_hover_tooltip(
                            title="4 ELEVATED Tasks \u2014 Why they became critical",
                            entries=[
                                ("What changed", "These tasks existed before but their frequency and importance have surged because AI-generated code requires much more verification."),
                                ("T5 \u2014 Code Review", "AI-generated code has a 12-65% vulnerability rate (SOTA Section 7.1), making continuous review essential \u2014 not just once per pull request."),
                                ("T12 \u2014 Version Control", "When agents modify 10+ files at once, structured branching and worktree isolation become mandatory to prevent conflicts."),
                                ("T15 \u2014 Requirements", "AI-driven conversational elicitation produces requirements faster but they need careful human validation to avoid hallucinated criteria."),
                            ],
                            scale="2vw", width="70vw", position="left",
                        )
            st_space("v", 2)
            _render_group(_TASKS_ELEVATED, _cell_elev, _hdr_elev, bs.label_elev,zoom=90)

    st_slide_break(marker_label="7 TRANSFORMED Tasks (1/2)")

    # ── Slide 5: TRANSFORMED tasks (1/2) — T3, T4, T7, T8 ─────────
    with st_block(_page_fill):
        with st_block(s.center_txt):
            with st_zoom(90):
                with st_grid(
                    cols="95% 5%",
                    gap="0px",
                    cell_styles=s.project.containers.grid_cell_centered,
                ) as g:
                    with g.cell():
                        st_write(bs.heading, "15 Core Tasks", tag=t.div, toc_lvl="+1")
                        st_write(bs.sub_trans, "7 TRANSFORMED \u2014 Traditional tasks, new nature (1/2)")
                    with g.cell():
                        st_hover_tooltip(
                            title="7 TRANSFORMED Tasks (1/2) \u2014 How the role changed",
                            entries=[
                                ("What changed", "These traditional SE tasks still exist, but the human role shifted from doing the work to validating and deciding on AI-produced output."),
                                ("T3 \u2014 Architecture", "AI proposes design options with trade-offs; the developer chooses and takes responsibility for the decision."),
                                ("T4 \u2014 Code Generation", "Instead of writing code line by line, the developer orchestrates multi-agent code production and verifies the result."),
                                ("T7-T8", "AI identifies bugs and refactoring opportunities; the developer confirms the diagnosis and validates the fix."),
                            ],
                            scale="2vw", width="70vw", position="left",
                        )
            st_space("v", 2)
            _render_group(_TASKS_TRANSFORMED[:4], _cell_trans, _hdr_trans, bs.label_trans)

    st_slide_break(marker_label="7 TRANSFORMED Tasks (2/2)")

    # ── Slide 6: TRANSFORMED tasks (2/2) — T9, T10, T11 ─────────
    with st_block(_page_fill+s.center_txt):
        with st_zoom(90):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    st_write(bs.heading, "15 Core Tasks", tag=t.div, toc_lvl="+1")
                    st_write(bs.sub_trans, "7 TRANSFORMED \u2014 Traditional tasks, new nature (2/2)")
                with g.cell():
                    st_hover_tooltip(
                        title="7 TRANSFORMED Tasks (2/2) \u2014 Automation with oversight",
                        entries=[
                            ("T9 \u2014 Documentation", "AI generates docs automatically from code; the developer curates quality and accuracy instead of writing from scratch."),
                            ("T10 \u2014 Security", "AI scans dependencies and detects vulnerabilities; the developer prioritizes which ones to fix based on risk assessment."),
                            ("T11 \u2014 CI/CD", "AI-triggered builds and deployments become standard; the developer defines the pipeline, AI executes and monitors it."),
                            ("Common thread", "In all 7 transformed tasks, the pattern is the same: AI does the heavy lifting, the human validates, decides, and takes responsibility."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
        st_space("v", 2)
        _render_group(_TASKS_TRANSFORMED[4:], _cell_trans, _hdr_trans, bs.label_trans)

    st_space("v", "30vh")