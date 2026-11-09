"""Slide — Exercise sheet — task 1: done when, mid-point, if stuck."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Exercise sheet — task 1: done when, mid-point, if stuck — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "d2_build_ex_check_body")
    label = s.project.titles.label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "d2_build_ex_check_cmd")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "d2_build_ex_check_done")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, 'Task 1 — Am I Done?', tag=t.div, toc_lvl='+1')
            with st_block(bs.done_box):
                st_write(
                    bs.body,
                    (bs.done_label, 'Done when: '),
                    (bs.cmd, 'npm run test:run'),
                    ' shows your new test passing, and ',
                    (bs.cmd, 'git log --oneline'),
                    ' shows ',
                    (bs.cmd, 'test:'),
                    ' before ',
                    (bs.cmd, 'feat:'),
                    '.',
                )
            st_write(
                bs.body,
                (bs.label, 'Mid-point (12:00): '),
                'your RED test is committed. Not yet? Ask now.',
                tag=t.div,
            )
            st_write(
                bs.body,
                (bs.label, 'Plan unclear? '),
                'use the fallback prompts: ExpenseItem, then ExpenseForm.',
                tag=t.div,
            )
            st_write(
                bs.body,
                (bs.label, 'If stuck: '),
                '1. ',
                'your tutor window',
                '  2. recovery tag ',
                (bs.cmd, 'j2-start'),
                '  3. raise your hand',
                tag=t.div,
            )
            st_write(bs.body, (bs.label, 'Ahead? '), 'task 2 of your plan, same loop.', tag=t.div)
