"""Slide — Exercise: Your First Compound."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Compound exercise slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    stat = s.project.titles.stat
    closing = s.project.titles.body + s.project.colors.highlight + s.bold

bs = BlockStyles

_RULES_EXAMPLE = """\
## Rules learned from CalcApp v0.3

1. Always write acceptance tests BEFORE implementing a feature
2. Use Given/When/Then format for all test scenarios
3. [Your rule here based on what you learned today]"""


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Exercise: Your First Compound", tag=t.div, toc_lvl="1")
        st_space("v", 0.5)

        st_write(
            bs.body,
            (bs.stat, "Hands-on 10 min"),
            " \u2014 Based on your CalcApp v0.3 work today, write ",
            (bs.keyword, "3 rules"),
            " you would add to .cursor/rules/project.mdc:",
        )
        st_space("v", 0.5)

        st_code(s.none, code=_RULES_EXAMPLE, language="markdown")

        st_space("v", 1)

        with st_block(s.project.containers.callout):
            st_write(
                bs.closing,
                "Share with your neighbor. Compare rules. "
                "The best ones become team knowledge.",
            )
