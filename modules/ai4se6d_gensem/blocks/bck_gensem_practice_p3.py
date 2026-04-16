"""P3 — Sprint Planning on CalcApp — 3 scenarios by IT expertise."""
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
    body = Style.create(s.Large + s.text.wrap.hyphens, "p3_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "p3_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "p3_acc")
    timer = Style.create(s.Huge + s.bold + s.project.colors.highlight + s.center_txt, "p3_timer")
bs = BlockStyles

_left = Style("text-align: left;", "p3_left")


def _scenario_slide(level_label, cell_style, steps, question):
    mid = (len(steps) + 1) // 2
    left_steps = steps[:mid]
    right_steps = steps[mid:]

    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, f"P3: Sprint Planning \u2014 {level_label}", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title=f"P3 {level_label} \u2014 What to do",
                        entries=[
                            ("Goal", f"Execute the LC01 discovery pipeline (COLLECT \u2192 ASSESS \u2192 PLAN) on CalcApp. Adapted for {level_label} IT expertise."),
                            ("Time", "45 minutes."),
                            ("Deliverable", "A validated .gse/plan.yaml with complexity budget and TASK- items."),
                        ],
                        scale="2vw", width="70vw", position="left",
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
    st_slide_break(marker_label="P3: Sprint Planning")

    _scenario_slide(
        level_label="Beginner",
        cell_style=_cell,
        steps=[
            "Run /gse:go \u2014 let the agent guide you through COLLECT \u2192 ASSESS \u2192 PLAN",
            "Read .gse/plan.yaml generated \u2014 count the tasks",
            "Note the total complexity points",
            "Validate the plan when the agent asks (Gate decision)",
        ],
        question="Question: Does the plan seem realistic? How many points does it use?",
    )

    st_slide_break(marker_label="P3: Intermediate")

    _scenario_slide(
        level_label="Intermediate",
        cell_style=_cell_acc,
        steps=[
            "Run /gse:collect \u2014 examine sources.yaml and reusability assessments",
            "Run /gse:assess \u2014 review the gap analysis (\u2713 / \u25d0 / \u2717 / \u26a0)",
            "Run /gse:plan \u2014 validate the sprint plan (Gate)",
            "Open .gse/plan.yaml \u2014 verify tasks[], branches, and complexity costs",
        ],
        question="Question: Is any task under-estimated? Would you reorder the priorities?",
    )

    st_slide_break(marker_label="P3: Advanced / Expert")

    _scenario_slide(
        level_label="Advanced / Expert",
        cell_style=_cell_act,
        steps=[
            "Run the LC01 pipeline manually with a tight budget (5 pts instead of 10)",
            "Observe the agent\u2019s trade-offs under budget pressure",
            "Add a spike: /gse:task --spike to evaluate an external dependency",
            "Compare the spike DEC- artifact with the plan \u2014 does the spike change anything?",
        ],
        question="Question: How does a constrained budget change the plan? What did the spike reveal?",
    )
