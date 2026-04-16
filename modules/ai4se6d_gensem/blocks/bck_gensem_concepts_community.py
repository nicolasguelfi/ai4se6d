"""Slide — The Community Ecosystem: stats on plugins, rules, MCP."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Community ecosystem styles."""
    heading = s.project.titles.heading
    stat_hero = Style.create(
        s.project.colors.highlight + s.bold + s.Huge + s.center_txt,
        "gs_comm_hero",
    )
    hero_label = s.project.titles.body + s.center_txt
    hero_sub = s.project.titles.caption + s.center_txt
    takeaway = s.project.titles.body_accent + s.center_txt

bs = BlockStyles


_STATS = [
    ("9,000+", "Claude Code plugins", "128+ curated"),
    ("800+", "cursor.directory rules", "shared by community"),
    ("16,670+", "MCP servers", "in the registry"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, "The Community Ecosystem", tag=t.div, toc_lvl="1")
        st_space("v", 1)

        with st_grid(
            cols="repeat(auto-fit, minmax(280px, 1fr))",
            gap="24px",
            cell_styles=s.project.containers.cell_primary_bg
            + s.project.containers.cell_pad_md,
        ) as g:
            for number, label, sub in _STATS:
                with g.cell():
                    st_write(bs.stat_hero, number, tag=t.div)
                    st_write(bs.hero_label, label)
                    st_write(bs.hero_sub, sub)

        st_space("v", 2)
        st_write(
            bs.takeaway,
            "The ecosystem is building methodology infrastructure, not just tools.",
        )
