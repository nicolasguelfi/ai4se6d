"""Slide — Try it: write and commit docs/plan.md (steps)."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Exercise steps styles."""
    heading = s.project.titles.heading
    timer = Style.create(s.project.titles.stat + s.center_txt, "d2_plan_ex_timer")
    step = s.project.titles.table_cell
    keyword = s.project.titles.table_label
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Try It: Your docs/plan.md", tag=t.div, toc_lvl="+1")
        st_write(bs.timer, "20 min · goal: a committed plan", tag=t.div)
        st_space("v", 0.5)
        with st_list(l_style=bs.step, li_style=bs.step, list_type=lt.ordered) as l:
            with l.item(): st_write(bs.step, (bs.keyword, "git switch mywork"), ", ", (bs.keyword, "opencode"), ", ", (bs.keyword, "Tab → plan"))
            with l.item(): st_write(bs.step, "Paste the elicitation prompt, answer its questions")
            with l.item(): st_write(bs.step, "“Split into 5-8 atomic tasks, tests first, with acceptance criteria.”")
            with l.item(): st_write(bs.step, "Push back at least once: too big? not testable?")
            with l.item(): st_write(bs.step, (bs.keyword, "Tab → build"), ": “Write docs/plan.md in the slide format.”")
            with l.item(): st_write(bs.step, "Edit, mark T1 ", (bs.keyword, "[next]"), ", ", (bs.keyword, "git add"), " it, ", (bs.keyword, "git diff --staged"))
            with l.item(): st_write(bs.step, (bs.keyword, "git commit -m \"docs: v0.1 plan\""))
