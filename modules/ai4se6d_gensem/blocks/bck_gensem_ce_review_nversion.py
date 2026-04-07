"""Slide — Review: N-Version Verification."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """N-version review slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    label = s.project.titles.label
    closing = s.project.titles.body + s.project.colors.highlight + s.bold

bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "Review: N-Version Verification", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_block(s.project.containers.callout):
            st_write(
                bs.body,
                (bs.label, "Analogy: "),
                "In safety-critical systems (aviation, medical), ",
                (bs.keyword, "N independent implementations"),
                " are compared to catch defects.",
            )

        st_space("v", 0.5)

        st_write(
            bs.body,
            "CE applies the same principle: ",
            (bs.keyword, "N independent review perspectives"),
            " \u2014 correctness, security, architecture, learning.",
        )

        st_space("v", 1)

        with st_block(s.project.containers.callout):
            st_write(
                bs.closing,
                "Like having 3 expert reviewers on every PR \u2014 "
                "but it takes 2 minutes, not 2 days.",
            )
