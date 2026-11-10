"""Slide — Demo 2 then try it: context and @file (5 min)."""
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
    demo = Style.create(s.project.titles.table_cell + s.project.colors.muted, "try_demo")
bs = BlockStyles

_SHEET = [
    ("Goal", "compare a vague prompt with a precise one"),
    ("Done when", "it quotes the test command and folder from the files"),
    ("Mid-point (2 min)", "the vague answer is noted"),
    ("If stuck", "your tutor window, then raise your hand"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Try It (5 min) — Context", tag=t.div, toc_lvl="+1")
        st_write(bs.demo, "Demo first (3 min): the same question, vague then with @files", tag=t.div)
        with st_zoom(85):
            with st_list(l_style=bs.step, li_style=bs.step, list_type=lt.ordered) as l:
                with l.item(): st_write(bs.step, (bs.keyword, "/new"), " \u201cHow are tests organised here?\u201d Note the answer")
                with l.item(): st_write(bs.step, (bs.keyword, "/new"), " \u201cFrom ", (bs.keyword, "@package.json"), " and ", (bs.keyword, "@AGENTS.md"), ": test command, folder, naming?\u201d")
                with l.item(): st_write(bs.step, (bs.keyword, "!npm run test:run"), " — the output joins the conversation")
                with l.item(): st_write(bs.step, "\u201cSummarise the test results in two lines.\u201d")
        with st_zoom(85):
            with st_block(s.project.containers.callout):
                with st_grid(cols="auto 1fr", gap="4px 24px") as g:
                    for label, text in _SHEET:
                        with g.cell():
                            st_write(bs.label, label)
                        with g.cell():
                            st_write(bs.text, text)
