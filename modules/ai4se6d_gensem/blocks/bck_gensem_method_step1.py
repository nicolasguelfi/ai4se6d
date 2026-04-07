"""Slide — Step 1: Requirements - Before Any Code."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Step 1 slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.accent
    label = s.bold + s.project.colors.primary
    callout_text = s.project.titles.body + s.project.colors.highlight
    timing = s.bold + s.project.colors.highlight
bs = BlockStyles

_PLAN_PROMPT = """\
I need to build [project description].
Help me define 5-8 functional requirements using
Given/When/Then acceptance criteria.
Also define 3-4 non-functional requirements."""


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Step 1: Requirements \u2014 Before Any Code", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        st_write(bs.body, (bs.label, "Plan Mode prompt:"))
        st_space("v", 0.5)
        st_code(s.none, code=_PLAN_PROMPT, language="text")

        st_space("v", 1)
        st_write(
            bs.body,
            (bs.label, "Output: "),
            "docs/requirements.md with ",
            (bs.keyword, "FR-001"),
            " through ",
            (bs.keyword, "FR-008"),
            " + ",
            (bs.keyword, "NFR-001"),
            " through ",
            (bs.keyword, "NFR-004"),
            ".",
        )

        st_space("v", 1)
        with st_block(s.project.containers.callout):
            st_write(
                bs.callout_text,
                "AgileGen principle: Gherkin format ensures consistency "
                "between ask and output.",
            )

        st_space("v", 1)
        st_write(
            bs.body,
            (bs.timing, "Time budget: 30 min."),
            " If more, you\u2019re over-engineering for 1.5 days.",
        )
