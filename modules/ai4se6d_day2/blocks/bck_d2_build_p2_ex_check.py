"""Slide — Exercise sheet — Part 2: done when, mid-point, if stuck."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Exercise sheet — Part 2: done when, mid-point, if stuck — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "d2_build_p2_ex_check_body")
    label = s.project.titles.label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "d2_build_p2_ex_check_cmd")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "d2_build_p2_ex_check_done")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(80):
            st_write(bs.heading, 'Part 2 — Am I Done?', tag=t.div, toc_lvl='+1')
            with st_block(bs.done_box):
                st_write(
                    bs.body,
                    (bs.done_label, 'Done when: '),
                    (bs.cmd, 'npm run test:run'),
                    ' shows 4+ passing tests; the app has two pages; an added expense survives a browser refresh.',
                )
            st_write(
                bs.body,
                (bs.label, 'Mid-point (13:55): '),
                'routing merged into ',
                (bs.cmd, 'mywork'),
                '. Not there? Ask now.',
                tag=t.div,
            )
            st_write(
                bs.body,
                (bs.label, 'If stuck: '),
                '1. ',
                'your tutor window',
                '  2. recovery tag ',
                (bs.cmd, 'j2-part1'),
                '  3. raise your hand',
                tag=t.div,
            )
            st_write(
                bs.body,
                (bs.label, 'Ahead? '),
                'delete an expense (',
                (bs.cmd, 'onDelete'),
                ') — same loop.',
                tag=t.div,
            )
