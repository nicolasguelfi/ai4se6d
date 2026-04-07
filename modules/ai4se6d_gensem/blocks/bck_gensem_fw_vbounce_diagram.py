"""Slide — V-Bounce: The Diagram (text-grid V-shape layout)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """V-Bounce diagram styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    label = s.project.titles.label
    stat = s.project.titles.stat
    human = Style.create(
        s.bold + s.project.colors.primary + Style("font-size: 48pt;", "_gs_vbd_pt48"),
        "gs_vbd_human",
    )
    ai_engine = Style.create(
        s.bold + s.project.colors.highlight + Style("font-size: 48pt;", "_gs_vbd_pt48b"),
        "gs_vbd_ai_engine",
    )
    arrow = Style.create(
        s.project.colors.accent + Style("font-size: 48pt;", "_gs_vbd_pt48c"),
        "gs_vbd_arrow",
    )
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "V-Bounce: The Diagram", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        # V-shape as 3-column grid: left descending, center AI, right ascending
        with st_grid(
            cols="1fr 1fr 1fr",
            gap="16px",
            cell_styles=s.project.containers.grid_cell_centered,
        ) as g:
            # Row 1 — top of V
            with g.cell():
                with st_block(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_sm):
                    st_write(bs.human, "\u2193 Requirements")
                    st_write(bs.body, "\u2714 Human validation")
            with g.cell():
                st_write(bs.arrow, "\u21c4")
            with g.cell():
                with st_block(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_sm):
                    st_write(bs.human, "Acceptance \u2191")
                    st_write(bs.body, "\u2714 Human validation")

            # Row 2 — middle of V
            with g.cell():
                with st_block(s.project.containers.cell_accent_bg + s.project.containers.cell_pad_sm):
                    st_write(bs.human, "\u2193 Architecture")
                    st_write(bs.body, "\u2714 Human validation")
            with g.cell():
                st_write(bs.arrow, "\u21c4")
            with g.cell():
                with st_block(s.project.containers.cell_accent_bg + s.project.containers.cell_pad_sm):
                    st_write(bs.human, "Integration \u2191")
                    st_write(bs.body, "\u2714 Human validation")

            # Row 3 — middle-low of V
            with g.cell():
                with st_block(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_sm):
                    st_write(bs.human, "\u2193 Design")
                    st_write(bs.body, "\u2714 Human validation")
            with g.cell():
                st_write(bs.arrow, "\u21c4")
            with g.cell():
                with st_block(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_sm):
                    st_write(bs.human, "Unit Tests \u2191")
                    st_write(bs.body, "\u2714 Human validation")

        # Bottom — AI Implementation Engine
        st_space("v", 1)
        with st_block(
            s.project.containers.cell_active_bg
            + s.project.containers.cell_pad_md
            + s.center_txt,
        ):
            st_write(bs.ai_engine, "\u2699 AI Implementation Engine")
            st_write(bs.body, "Bounce arrows connect each human checkpoint to the AI execution zone")
