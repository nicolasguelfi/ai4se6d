"""Slide — Enterprise Transformation Data: 10% vs 25-30%."""
# @guideline: maximize-viewport
# @pattern: stat-hero
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    stat_warn = Style.create(
        s.GIANT + s.bold + s.project.colors.highlight + s.center_txt,
        "gs_ev_ent_warn",
    )
    stat_ok = Style.create(
        s.GIANT + s.bold + s.project.colors.success + s.center_txt,
        "gs_ev_ent_ok",
    )
    body = s.project.titles.body
    label_warn = Style.create(
        s.Large + s.bold + s.project.colors.highlight + s.center_txt,
        "gs_ev_ent_lbl_warn",
    )
    label_ok = Style.create(
        s.Large + s.bold + s.project.colors.success + s.center_txt,
        "gs_ev_ent_lbl_ok",
    )
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(
                bs.heading,
                "Enterprise Transformation Data",
                tag=t.div, toc_lvl="1",
            )
            st_space("v", 1)

        with st_grid(
            cols=s.project.containers.responsive_2col,
            gap="32px",
            cell_styles=s.project.containers.cell_primary_bg
            + s.project.containers.cell_pad_md
            + s.project.containers.grid_cell_centered,
        ) as g:
            with g.cell():
                st_write(bs.stat_warn, "10%")
                st_write(bs.label_warn, "Tools alone (Bain)")

            with g.cell():
                st_write(bs.stat_ok, "25\u201330%")
                st_write(bs.label_ok, "End-to-end transformation (Bain)")

        st_space("v", 2)
        st_write(
            bs.body,
            "McKinsey: Redesign processes AND redirect saved time "
            "to higher-value work.",
        )

        st_space("v", 1)
        st_write(
            bs.source,
            cite("bain2025"), ", ",
            cite("mckinsey-aieng2025"),
        )
