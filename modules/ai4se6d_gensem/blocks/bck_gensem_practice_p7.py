"""P7 — Full cycle: FIX → DELIVER → COMPOUND — 3 scenarios by IT expertise."""
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
    body = Style.create(s.Large + s.text.wrap.hyphens, "p7_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "p7_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "p7_acc")
    timer = Style.create(s.Huge + s.bold + s.project.colors.highlight + s.center_txt, "p7_timer")
bs = BlockStyles

_left = Style("text-align: left;", "p7_left")


def _scenario_slide(level_label, cell_style, steps, question):
    mid = (len(steps) + 1) // 2
    left_steps = steps[:mid]
    right_steps = steps[mid:]

    with st_block(_pf):
        with st_block(s.center_txt):
            st_write(bs.heading, f"P7: Complete Cycle \u2014 {level_label}", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title=f"P7 {level_label} \u2014 What to do",
                entries=[
                    ("Goal", f"Close the loop: FIX \u2192 DELIVER \u2192 COMPOUND \u2192 HEALTH. Adapted for {level_label} IT expertise."),
                    ("Time", "45 minutes."),
                    ("Deliverable", "Findings fixed, feature merged to main, compound.md with patterns, improved health score."),
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
    st_slide_break(marker_label="P7: Complete Cycle")

    _scenario_slide(
        level_label="Beginner",
        cell_style=_cell,
        steps=[
            "Run /gse:fix \u2014 the agent corrects findings automatically",
            "Run /gse:deliver \u2014 choose \u201cClean summary\u201d when asked about merge strategy",
            "Run /gse:compound \u2014 read the patterns the agent captured",
            "Run /gse:health \u2014 compare the score with what you saw in P2",
        ],
        question="Question: Did the health score improve? What patterns did COMPOUND capture?",
    )

    st_slide_break(marker_label="P7: Intermediate")

    _scenario_slide(
        level_label="Intermediate",
        cell_style=_cell_acc,
        steps=[
            "Fix 2 review findings with the agent\u2019s guidance",
            "Choose your merge strategy (squash vs merge) \u2014 justify your choice",
            "Run /gse:compound \u2014 add a pattern you observed during the sprint",
            "Check /gse:health \u2014 which dimensions improved?",
        ],
        question="Question: Why did you choose that merge strategy? What pattern would you add to compound.md?",
    )

    st_slide_break(marker_label="P7: Advanced / Expert")

    _scenario_slide(
        level_label="Advanced / Expert",
        cell_style=_cell_act,
        steps=[
            "Fix all HIGH findings \u2014 re-run /gse:review to verify the fixes",
            "Choose rebase as merge strategy \u2014 justify the implications for history",
            "Run /gse:compound \u2014 write a methodology feedback (Axe 2: what GSE-One could do better)",
            "Run /gse:integrate \u2014 choose which integrations to execute and which to skip",
        ],
        question="Question: What feedback would you give on the methodology itself? Where should patterns be routed?",
    )
