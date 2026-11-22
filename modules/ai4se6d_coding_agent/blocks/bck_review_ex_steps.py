"""Slide — Exercise sheet — review today's diff (goal and steps)."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    """Exercise sheet — review today's diff (goal and steps) — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "review_ex_steps_body")
    label = s.project.titles.label
    keyword = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "review_ex_steps_cmd")
    timer = Style.create(s.project.titles.stat + s.center_txt, "review_ex_steps_timer")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, "Exercise — Review Today's Diff", tag=t.div, toc_lvl='1', label='Review Practice (15:15)')
            st_write(bs.timer, '15:15 → 15:50 · 35 min', tag=t.div)
            st_write(
                bs.body,
                (bs.label, 'Goal: '),
                'review everything you changed today, triage it, fix what matters.',
                tag=t.div,
            )
            with st_list(list_type=lt.ordered, l_style=bs.body, li_style=bs.body) as l:
                with l.item():
                    st_write(
                        bs.body,
                        (bs.cmd, 'git switch mywork'),
                        ' → ',
                        (bs.cmd, 'git diff j2-start --stat'),
                    )
                with l.item():
                    st_write(
                        bs.body,
                        'Shift+Tab → ',
                        (bs.keyword, 'plan'),
                        ' agent (read-only): run the review prompt',
                    )
                with l.item():
                    st_write(bs.body, 'Write the triage in ', (bs.cmd, 'docs/review.md'))
                with l.item():
                    st_write(
                        bs.body,
                        (bs.cmd, 'git switch -c fix/review'),
                        ': fix 2-3 HIGH/MEDIUM, test first',
                    )
                with l.item():
                    st_write(
                        bs.body,
                        'Refuse at least ',
                        (bs.keyword, 'one'),
                        ' finding, with a written reason',
                    )
