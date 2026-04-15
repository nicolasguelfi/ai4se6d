"""P5 — Requirements & Design on CalcApp — 3 scenarios by IT expertise."""
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
    body = Style.create(s.Large + s.text.wrap.hyphens, "p5_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "p5_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "p5_acc")
    timer = Style.create(s.Huge + s.bold + s.project.colors.highlight + s.center_txt, "p5_timer")
bs = BlockStyles

_left = Style("text-align: left;", "p5_left")


def _scenario_slide(level_label, cell_style, steps, question):
    mid = (len(steps) + 1) // 2
    left_steps = steps[:mid]
    right_steps = steps[mid:]

    with st_block(_pf):
        with st_block(s.center_txt):
            st_write(bs.heading, f"P5: Requirements & Design \u2014 {level_label}", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title=f"P5 {level_label} \u2014 What to do",
                entries=[
                    ("Goal", f"Execute REQS \u2192 DESIGN \u2192 PREVIEW on CalcApp. Adapted for {level_label} IT expertise."),
                    ("Time", "45 minutes."),
                    ("Deliverable", "reqs.md with FR + NFR, design.md with DEC- decisions, preview validated."),
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
    st_slide_break(marker_label="P5: Requirements & Design")

    _scenario_slide(
        level_label="Beginner",
        cell_style=_cell,
        steps=[
            "Run /gse:reqs \u2014 the agent asks you questions, answer in plain language",
            "Observe the FR generated \u2014 do you understand the acceptance criteria?",
            "Run /gse:preview \u2014 compare with what you imagined",
            "Run /gse:status \u2014 can you see the links between artifacts?",
        ],
        question="Question: Does the preview match your idea of what CalcApp should do?",
    )

    st_slide_break(marker_label="P5: Intermediate")

    _scenario_slide(
        level_label="Intermediate",
        cell_style=_cell_acc,
        steps=[
            "Run /gse:reqs for FR-001 (budget per category) + NFR-001 (perf <200ms)",
            "Run /gse:design \u2014 validate the architecture proposal (Gate decision)",
            "Run /gse:preview \u2014 check wireframe and API contract",
            "Run /gse:status \u2014 verify the traceability chain REQ \u2192 DES \u2192 TASK",
        ],
        question="Question: Is the design consistent with the requirements? Any missing links?",
    )

    st_slide_break(marker_label="P5: Advanced / Expert")

    _scenario_slide(
        level_label="Advanced / Expert",
        cell_style=_cell_act,
        steps=[
            "Write a complex FR manually (multi-device sync) with Given/When/Then criteria",
            "Run /gse:reqs \u2014 compare your version with the agent\u2019s output",
            "Run /gse:design \u2014 challenge localStorage vs API backend with consequence analysis",
            "Verify DEC- artifact structure: does it have context, options, choice, consequences?",
        ],
        question="Question: Where is the agent right and where is it wrong compared to your expertise?",
    )
