"""Slide — Exercise sheet — review: done when, mid-point, if stuck."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Exercise sheet — review: done when, mid-point, if stuck — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "review_ex_check_body")
    label = s.project.titles.label
    keyword = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "review_ex_check_cmd")
    done_box = s.project.containers.callout
    done_label = Style.create(s.bold + s.project.colors.success, "review_ex_check_done")
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, 'Review — Am I Done?', tag=t.div, toc_lvl='+1')
            with st_block(bs.done_box):
                st_write(
                    bs.body,
                    (bs.done_label, 'Done when: '),
                    (bs.cmd, 'docs/review.md'),
                    ' lists your findings with severities; 2+ are ',
                    (bs.keyword, 'fixed'),
                    ' with a test; 1+ is ',
                    (bs.keyword, 'refused'),
                    ' with a reason; ',
                    (bs.cmd, 'npm run test:run'),
                    ' green on ',
                    (bs.cmd, 'fix/review'),
                    '.',
                )
            st_write(
                bs.body,
                (bs.label, 'Mid-point (15:35): '),
                "triage written. Not yet? Review one task's diff only.",
                tag=t.div,
            )
            st_write(
                bs.body,
                (bs.label, 'If stuck: '),
                '1. ',
                'your tutor window',
                '  2. recovery tag ',
                (bs.cmd, 'j2-v0.1'),
                '  3. raise your hand (review the reference code)',
                tag=t.div,
            )
            st_write(bs.body, (bs.label, 'Next (15:50): '), 'README 80/20.', tag=t.div)
