"""Slide — Exercise sheet — task 1 of your own plan (goal and steps)."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Exercise sheet — task 1 of your own plan (goal and steps) — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "build_ex_steps_body")
    label = s.project.titles.label
    keyword = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "build_ex_steps_cmd")
    timer = Style.create(s.project.titles.stat + s.center_txt, "build_ex_steps_timer")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "build_ex_steps_foot")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, 'Exercise — Task 1 of YOUR Plan', tag=t.div, toc_lvl='+1')
            st_write(bs.timer, '11:45 → 12:10 · 25 min', tag=t.div)
            st_write(
                bs.body,
                (bs.label, 'Goal: '),
                'deliver the first task of ',
                (bs.cmd, 'docs/plan.md'),
                ', test first, on its own branch.',
                tag=t.div,
            )
            with st_list(list_type=lt.ordered, l_style=bs.body, li_style=bs.body) as l:
                with l.item():
                    st_write(bs.body, (bs.cmd, 'git switch -c feat/&lt;task-1-name&gt;'))
                with l.item():
                    st_write(
                        bs.body,
                        'RED prompt → ',
                        (bs.keyword, 'read the test'),
                        ' → commit ',
                        (bs.cmd, 'test: …'),
                    )
                with l.item():
                    st_write(
                        bs.body,
                        'GREEN prompt → ',
                        (bs.cmd, 'npm run test:run'),
                        ' green → commit ',
                        (bs.cmd, 'feat: …'),
                    )
                with l.item():
                    st_write(bs.body, 'Mutant check, then undo the sabotage')
                with l.item():
                    st_write(
                        bs.body,
                        (bs.cmd, 'git switch mywork'),
                        ' → ',
                        (bs.cmd, 'git merge feat/&lt;task-1-name&gt;'),
                    )
            st_write(
                bs.foot,
                'mywork is your main line since this morning: every finished task is merged into it.',
                tag=t.div,
            )
