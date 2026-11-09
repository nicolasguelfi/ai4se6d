"""Slide — Demo 3 then try it: plan with live docs (5 min)."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Try-it sheet styles."""
    heading = s.project.titles.heading
    step = s.project.titles.table_cell
    keyword = s.project.titles.table_label
    label = s.project.titles.table_label
    text = s.project.titles.table_cell
    demo = Style.create(s.project.titles.table_cell + s.project.colors.muted, "d2_try_demo")
bs = BlockStyles

_SHEET = [
    ("Goal", "a reviewed plan, no code"),
    ("Done when", "the plan names files and tests; a Context7 call appears"),
    ("Mid-point (2 min)", "context7 shows as connected"),
    ("If stuck", "@tutor, then raise your hand"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Try It (5 min) — Plan", tag=t.div, toc_lvl="+1")
        st_write(bs.demo, "Demo first (3 min): plan agent, todo list, a Context7 call", tag=t.div)
        with st_zoom(85):
            with st_list(l_style=bs.step, li_style=bs.step, list_type=lt.ordered) as l:
                with l.item(): st_write(bs.step, "No context7 in ", (bs.keyword, "opencode.json"), "? Add it, restart opencode")
                with l.item(): st_write(bs.step, (bs.keyword, "opencode mcp list"), " in a terminal: context7 connected?")
                with l.item(): st_write(bs.step, (bs.keyword, "Tab → plan"), ": \u201cPlan a /budgets page. Use context7 for React Router 7. Tests first.\u201d")
                with l.item(): st_write(bs.step, "Read the plan and its todo list, push back once")
                with l.item(): st_write(bs.step, (bs.keyword, "Do not build"), ": your real plan comes at 11:00")
        with st_zoom(85):
            with st_block(s.project.containers.callout):
                with st_grid(cols="auto 1fr", gap="4px 24px") as g:
                    for label, text in _SHEET:
                        with g.cell():
                            st_write(bs.label, label)
                        with g.cell():
                            st_write(bs.text, text)
