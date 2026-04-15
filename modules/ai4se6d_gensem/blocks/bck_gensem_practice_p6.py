"""P6 — Produce + Tests + Review on CalcApp — 3 scenarios by IT expertise."""
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
    body = Style.create(s.Large + s.text.wrap.hyphens, "p6_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "p6_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "p6_acc")
    timer = Style.create(s.Huge + s.bold + s.project.colors.highlight + s.center_txt, "p6_timer")
bs = BlockStyles

_left = Style("text-align: left;", "p6_left")


def _scenario_slide(level_label, cell_style, steps, question):
    mid = (len(steps) + 1) // 2
    left_steps = steps[:mid]
    right_steps = steps[mid:]

    with st_block(_pf):
        with st_block(s.center_txt):
            st_write(bs.heading, f"P6: Produce, Test, Review \u2014 {level_label}", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title=f"P6 {level_label} \u2014 What to do",
                entries=[
                    ("Goal", f"Execute the core engineering cycle PRODUCE \u2192 TESTS \u2192 REVIEW on CalcApp. Adapted for {level_label} IT expertise."),
                    ("Time", "45 minutes."),
                    ("Deliverable", "Implemented feature, passing tests, review.md with classified findings."),
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
    st_slide_break(marker_label="P6: Produce, Test, Review")

    _scenario_slide(
        level_label="Beginner",
        cell_style=_cell,
        steps=[
            "Run /gse:produce \u2014 observe the code generated (you don\u2019t need to understand it)",
            "Run /gse:tests \u2014 how many tests pass? How many fail?",
            "Run /gse:review \u2014 read the 3 most critical findings",
            "Look at review.md \u2014 do you agree with the agent\u2019s assessment?",
        ],
        question="Question: Did the review find issues you would not have noticed? Do you agree?",
    )

    st_slide_break(marker_label="P6: Intermediate")

    _scenario_slide(
        level_label="Intermediate",
        cell_style=_cell_acc,
        steps=[
            "Run /gse:produce \u2192 /gse:tests \u2192 /gse:review in sequence",
            "Analyze the test pyramid: how many unit vs integration vs E2E tests?",
            "Classify review findings by severity (HIGH / MEDIUM / LOW)",
            "Identify which finding you would fix first and why",
        ],
        question="Question: Is the test pyramid appropriate for a web frontend? Which finding is most urgent?",
    )

    st_slide_break(marker_label="P6: Advanced / Expert")

    _scenario_slide(
        level_label="Advanced / Expert",
        cell_style=_cell_act,
        steps=[
            "Run /gse:produce \u2014 read the generated code critically",
            "Before /gse:tests, write your own test strategy \u2014 then compare with the agent\u2019s",
            "Run /gse:review \u2014 identify a finding you disagree with",
            "Argue with the agent (P16 devil\u2019s advocate) \u2014 document the outcome",
        ],
        question="Question: Where did the agent surprise you? Did devil\u2019s advocate (P16) catch something real?",
    )
