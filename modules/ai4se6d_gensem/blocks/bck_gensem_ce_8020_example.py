"""Slide — The 80/20 Rule: From Your Experience."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """80/20 rule slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    stat = s.project.titles.stat
    closing = s.project.titles.body + s.project.colors.highlight + s.bold

bs = BlockStyles


def build():
    st_marker("80/20 — From Your Experience")
    with st_block(s.project.containers.page_fill_top):
        with st_grid(
            cols="95% 5%",
            gap="0px",
            cell_styles=s.project.containers.grid_cell_centered,
        ) as g:
            with g.cell():
                st_write(bs.heading, "The 80/20 Rule \u2014 From Your Experience", tag=t.div, toc_lvl="+1")
            with g.cell():
                st_hover_tooltip(
                    title="80/20 Rule in GSE-One",
                    entries=[
                        ("Principle", "Invest ~80% in planning and review, ~20% in execution."),
                        ("Day 1 contrast", "FreeSelfApp spent ~90% coding -- the opposite ratio."),
                        ("GSE-One equivalent", "The /gse:plan and /gse:review phases embody this ratio."),
                    ],
                    scale="2vw", width="70vw", position="left",
                )

        with st_zoom(90):
            with st_block(s.project.containers.callout):
                st_write(
                    bs.body,
                    (bs.stat, "Day 1 FreeSelfApp: "),
                    "you spent ~90% coding, ~10% planning. Result? ",
                    (bs.keyword, "Tech debt"),
                    ", missing features, broken tests, ",
                    (bs.stat, "1h45 of chaos"),
                    ".",
                )

            st_space("v", 0.5)

            with st_block(s.project.containers.callout):
                st_write(
                    bs.body,
                    (bs.keyword, "GSE-One inverts this: "),
                    "~80% planning and review, ~20% execution. ",
                    "The AI handles the 20% in ",
                    (bs.stat, "minutes"),
                    ".",
                )

            st_space("v", 0.5)

            with st_block(s.project.containers.callout):
                st_write(
                    bs.closing,
                    "Your job shifts from WRITING code to DIRECTING the AI with precision.",
                )
