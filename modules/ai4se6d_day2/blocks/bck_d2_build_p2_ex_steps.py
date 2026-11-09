"""Slide — Exercise sheet — next tasks of your plan (goal and steps)."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Exercise sheet — next tasks of your plan (goal and steps) — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "d2_build_p2_ex_steps_body")
    label = s.project.titles.label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "d2_build_p2_ex_steps_cmd")
    timer = Style.create(s.project.titles.stat + s.center_txt, "d2_build_p2_ex_steps_timer")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "d2_build_p2_ex_steps_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, 'Exercise — Your Next Tasks', tag=t.div, toc_lvl='+1')
            st_write(bs.timer, '13:30 → 14:20 · 50 min', tag=t.div)
            st_write(
                bs.body,
                (bs.label, 'Goal: '),
                "deliver your plan's next tasks (routing, data, UI), one branch each, test first.",
                tag=t.div,
            )
            with st_list(list_type=lt.ordered, l_style=bs.body, li_style=bs.body) as l:
                with l.item():
                    st_write(bs.body, 'One task = one branch ', (bs.cmd, 'feat/&lt;task-name&gt;'))
                with l.item():
                    st_write(bs.body, 'RED → review → commit ', (bs.cmd, 'test: …'))
                with l.item():
                    st_write(bs.body, 'GREEN → review checklist → commit ', (bs.cmd, 'feat: …'))
                with l.item():
                    st_write(bs.body, 'Merge into ', (bs.cmd, 'mywork'), ' when green, next task')
            st_write(
                bs.foot,
                "Your plan's wording is unclear? Use the prompts of the previous slides.",
                tag=t.div,
            )
