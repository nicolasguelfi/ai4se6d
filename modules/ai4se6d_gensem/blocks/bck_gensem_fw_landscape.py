"""Slide — The Methodological Landscape: visual overview of 3 framework categories."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Landscape overview styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    label = s.project.titles.label
    cat_label = Style.create(
        s.Large + s.bold + s.project.colors.highlight,
        "gs_fwl_cat_label",
    )
    message = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "gs_fwl_message",
    )
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        st_write(bs.heading, "The Methodological Landscape", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        # Row 1 — Adaptations (primary bg)
        with st_block(
            s.project.containers.cell_primary_bg
            + s.project.containers.cell_pad_md
            + Style("margin-bottom: 12px;", "gs_fwl_row_mb"),
        ):
            st_write(bs.label, "Adaptations", tag=t.div)
            st_space("v", 0.5)
            with st_grid(
                cols="repeat(auto-fit, minmax(280px, 1fr))",
                gap="12px",
                cell_styles=s.project.containers.cell_accent_bg + s.project.containers.cell_pad_sm,
            ) as g:
                with g.cell():
                    st_write(bs.body, (bs.keyword, "AgileGen"))
                with g.cell():
                    st_write(bs.body, (bs.keyword, "Agentic DevOps"))

        # Row 2 — AI-Native (accent bg)
        with st_block(
            s.project.containers.cell_accent_bg
            + s.project.containers.cell_pad_md
            + Style("margin-bottom: 12px;", "gs_fwl_row_mb2"),
        ):
            st_write(bs.cat_label, "AI-Native", tag=t.div)
            st_space("v", 0.5)
            with st_grid(
                cols="repeat(auto-fit, minmax(220px, 1fr))",
                gap="12px",
                cell_styles=s.project.containers.cell_primary_bg + s.project.containers.cell_pad_sm,
            ) as g:
                for name in ("SE 3.0", "V-Bounce", "Promptware Eng.", "MAISTRO"):
                    with g.cell():
                        st_write(bs.body, (bs.keyword, name))

        # Row 3 — Process Plugins (active/highlight bg)
        with st_block(
            s.project.containers.cell_active_bg
            + s.project.containers.cell_pad_md,
        ):
            st_write(bs.cat_label, "Process Plugins", tag=t.div)
            st_space("v", 0.5)
            with st_grid(
                cols="1fr",
                gap="12px",
                cell_styles=s.project.containers.cell_primary_bg + s.project.containers.cell_pad_sm,
            ) as g:
                with g.cell():
                    st_write(bs.body, (bs.keyword, "Compound Engineering"))

        st_space("v", 2)
        st_write(
            bs.message,
            "We\u2019ll survey each, then deep-dive into Compound Engineering.",
        )
