"""P2 — Debrief + .gse/ exploration — 3 scenarios by IT expertise."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: exercise-flow
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_cell = s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_acc = s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_act = s.project.containers.cell_active_bg + s.project.containers.cell_pad_md + s.center_txt


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.text.wrap.hyphens, "p2_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "p2_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "p2_acc")
    highlight = Style.create(s.Large + s.bold + s.project.colors.highlight + s.center_txt, "p2_hl")
    timer = Style.create(s.Huge + s.bold + s.project.colors.highlight + s.center_txt, "p2_timer")
bs = BlockStyles

_left = Style("text-align: left;", "p2_left")


def _scenario_slide(title, level_label, cell_style, steps, question):
    """Render one scenario slide for a given IT expertise level."""
    mid = (len(steps) + 1) // 2
    left_steps = steps[:mid]
    right_steps = steps[mid:]

    with st_block(_pf):
        with st_block(s.center_txt):
            st_write(bs.heading, f"P2: Explore .gse/ \u2014 {level_label}", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title=f"P2 {level_label} \u2014 What to do",
                entries=[
                    ("Goal", f"Explore the .gse/ directory and understand what GSE-One produced during P1. Scenario adapted for {level_label} IT expertise."),
                    ("Time", "45 minutes."),
                    ("Deliverable", "Answers to the reflection question and a mental model of the .gse/ structure."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

            with st_grid(
                cols="1fr 1fr",
                gap="16px",
                cell_styles=s.project.containers.cell_pad_sm,
            ) as g:
                with g.cell():
                    with st_block(cell_style + _left):
                        with st_list(l_style=bs.body + _left, li_style=bs.body + _left, list_type=lt.unordered) as l:
                            for i, step in enumerate(left_steps, 1):
                                with l.item():
                                    st_write(bs.body + _left, (bs.keyword, f"{i}. "), step)
                with g.cell():
                    with st_block(cell_style + _left):
                        with st_list(l_style=bs.body + _left, li_style=bs.body + _left, list_type=lt.unordered) as l:
                            for i, step in enumerate(right_steps, mid + 1):
                                with l.item():
                                    st_write(bs.body + _left, (bs.keyword, f"{i}. "), step)

            st_space("v", 1)
            st_write(bs.accent, question)
            st_space("v", 1)
            st_write(bs.timer, "45 minutes")


def build():
    st_slide_break(marker_label="P2: Explore .gse/")

    # ── Beginner ────────────────────────────────────────────────────
    _scenario_slide(
        title="P2 Beginner",
        level_label="Beginner",
        cell_style=_cell,
        steps=[
            "Open the .gse/ folder with the trainer\u2019s help",
            "Find your profile in profile.yaml \u2014 do you recognize yourself?",
            "Run /gse:health \u2014 note the overall score",
            "Browse status.yaml \u2014 what sprint are you on?",
        ],
        question="Question: Which terms in these files do you not understand?",
    )

    st_slide_break(marker_label="P2: Intermediate")

    # ── Intermediate ────────────────────────────────────────────────
    _scenario_slide(
        title="P2 Intermediate",
        level_label="Intermediate",
        cell_style=_cell_acc,
        steps=[
            "Explore .gse/ autonomously: config.yaml, profile.yaml, status.yaml, backlog.yaml",
            "Run /gse:health \u2014 identify the 2 weakest dimensions",
            "Run /gse:status \u2014 compare with what you see in the files",
            "Read backlog.yaml \u2014 how are TASK- items structured?",
        ],
        question="Question: How would you improve the weakest health dimensions?",
    )

    st_slide_break(marker_label="P2: Advanced / Expert")

    # ── Advanced / Expert ───────────────────────────────────────────
    _scenario_slide(
        title="P2 Advanced",
        level_label="Advanced / Expert",
        cell_style=_cell_act,
        steps=[
            "Explore .gse/ \u2014 analyze YAML structure and cross-file references",
            "Edit config.yaml: change lifecycle.mode to Full",
            "Run /gse:status then /gse:health \u2014 analyze the impact",
            "Identify which guardrails activated and why",
        ],
        question="Question: What changed when you switched to Full mode? Which guardrails fired?",
    )
