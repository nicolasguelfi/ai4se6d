"""Slide — Review: N-Version Verification."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """N-version review slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    label = s.project.titles.label
    closing = s.project.titles.body + s.project.colors.highlight + s.bold

bs = BlockStyles


def build():
    st_marker("N-Version Verification")
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, "Review: N-Version Verification", tag=t.div, toc_lvl="+1")
        st_hover_tooltip(
            title="N-Version Verification",
            entries=[
                ("Origin", "Borrowed from safety-critical systems (aviation, medical) where N independent implementations are compared."),
                ("In GSE-One", "Multiple independent review perspectives -- correctness, security, architecture, learning -- catch different classes of defects."),
                ("Speed advantage", "Like having 3 expert reviewers on every PR, but automated in 2 minutes instead of 2 days."),
            ],
            scale="2vw", width="70vw", position="center",
        )
        st_space("v", 1)

        with st_zoom(120):
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
                "GSE-One applies the same principle: ",
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
