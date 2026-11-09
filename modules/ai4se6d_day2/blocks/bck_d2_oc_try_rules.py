"""Slide — Demo 1 then try it: project rules (5 min)."""
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
    ("Goal", "a rule of yours changes the agent\u2019s answer"),
    ("Done when", "the proposal uses cents; git log shows your AGENTS.md commit"),
    ("Mid-point (2 min)", "the agent named the test command"),
    ("If stuck", "@tutor, then raise your hand"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Try It (5 min) — Rules", tag=t.div, toc_lvl="+1")
        st_write(bs.demo, "Demo first (3 min): /init on a copy vs the starter\u2019s AGENTS.md", tag=t.div)
        with st_zoom(85):
            with st_list(l_style=bs.step, li_style=bs.step, list_type=lt.ordered) as l:
                with l.item(): st_write(bs.step, (bs.keyword, "git switch mywork"), ", then ", (bs.keyword, "opencode"))
                with l.item(): st_write(bs.step, "Ask: \u201cWhich test command and folders must you use?\u201d")
                with l.item(): st_write(bs.step, "Add to AGENTS.md: ", (bs.keyword, "Amounts are integers in cents."))
                with l.item(): st_write(bs.step, (bs.keyword, "/new"), ", then: \u201cPropose formatAmount. Code only, no file.\u201d")
                with l.item(): st_write(bs.step, (bs.keyword, "git diff AGENTS.md"), ", then commit it")
        with st_zoom(85):
            with st_block(s.project.containers.callout):
                with st_grid(cols="auto 1fr", gap="4px 24px") as g:
                    for label, text in _SHEET:
                        with g.cell():
                            st_write(bs.label, label)
                        with g.cell():
                            st_write(bs.text, text)
