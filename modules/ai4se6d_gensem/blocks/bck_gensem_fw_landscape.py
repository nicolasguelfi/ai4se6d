"""Slide — The Methodological Landscape: visual overview of 3 framework categories."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


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
    st_marker("Framework Landscape: 3 Categories")
    with st_block(s.project.containers.page_fill_top):
        with st_grid(
            cols="95% 5%",
            gap="0px",
            cell_styles=s.project.containers.grid_cell_centered,
        ) as g:
            with g.cell():
                with st_zoom(90):
                    st_write(bs.heading, "The Methodological Landscape", tag=t.div, toc_lvl="+1")
            with g.cell():
                st_hover_tooltip(
                    title="3 Categories of GenSE Frameworks",
                    entries=[
                        ("Adaptations", "Existing agile/DevOps methods extended with AI capabilities. Familiar but limited in scope."),
                        ("AI-Native", "Methods designed from scratch for AI-augmented development. Ambitious but mostly theoretical."),
                        ("Process Plugins", "Composable methodology plugins that work across tools. GSE-One fills gaps others leave open."),
                    ],
                    scale="2vw", width="70vw", position="left",
                )
        with st_zoom(90):
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
                    cols="repeat(auto-fit, minmax(280px, 1fr))",
                    gap="12px",
                    cell_styles=s.project.containers.cell_primary_bg + s.project.containers.cell_pad_sm,
                ) as g:
                    with g.cell():
                        st_write(bs.body, (bs.keyword, "Compound Engineering (CE)"))
                    with g.cell():
                        st_write(bs.body, (bs.keyword, "GSE-One"))

            st_space("v", 2)
            st_write(
                bs.message,
                "We\u2019ll survey each, then deep-dive into GSE-One.",
            )
