"""Slide — The review prompt for the plan agent."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """The review prompt for the plan agent — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "review_ex_prompt_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "review_ex_prompt_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "review_ex_prompt_foot")
bs = BlockStyles


_DIFF = """\
!git diff j2-start"""

_REVIEW = """\
Review this diff of CalcApp v0.1 against @docs/plan.md. Focus: bugs and
runtime errors, missing error handling, user input reaching storage
unvalidated, tests that prove nothing. For each finding: RVW-n,
HIGH/MEDIUM/LOW, file, why it matters, suggested fix. Edit nothing."""


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(70):
            st_write(bs.heading, 'The Review Prompt', tag=t.div, toc_lvl='+1')
            st_write(
                bs.body,
                'First, put the diff into the conversation — ',
                (bs.cmd, '!'),
                ' runs a shell command:',
                tag=t.div,
            )
            st_code(s.none, code=_DIFF, language='text', line_numbers=False, font_size="36pt")
            st_write(bs.body, 'Then:', tag=t.div)
            st_code(s.none, code=_REVIEW, language='text', line_numbers=False, font_size="36pt")
            st_write(
                bs.foot,
                'Diff too long? One task at a time: !git diff j2-start -- src/utils/',
                tag=t.div,
            )
