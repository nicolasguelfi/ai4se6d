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
        with st_grid(cols="95% 5%", gap="0px", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell():
                with st_zoom(90):
                    st_write(bs.heading, "Review: N-Version Verification", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(
                    title="N-Version Verification",
                    entries=[
                        ("Origin", "Borrowed from safety-critical systems (aviation, medical) where N independent implementations are compared."),
                        ("In GSE-One", "Multiple independent review perspectives -- correctness, security, requirements, architecture, test implementation, UX, adversarial self-review -- catch different classes of defects."),
                        ("Speed advantage", "Like having 6 expert reviewers (plus a devil's advocate) on every PR, but automated in 2 minutes instead of 2 days."),
                    ],
                    position="left", width="50vw",
                )

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
                " \u2014 correctness, security, requirements, architecture, test implementation, UX, adversarial self-review.",
            )

            st_space("v", 1)

            with st_block(s.project.containers.callout):
                st_write(
                    bs.closing,
                    "Like having 6 expert reviewers (plus a devil's advocate) on every PR \u2014 "
                    "but it takes 2 minutes, not 2 days.",
                )
