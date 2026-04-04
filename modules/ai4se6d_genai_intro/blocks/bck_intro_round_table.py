"""Slide — Participant(s): individual presentations round table."""
# @guideline: maximize-viewport
# @pattern: table-roadmap
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


_page_fill = s.project.containers.page_fill_top

# Cell style: semi-transparent bordered (table-roadmap pattern)
_cell = Style.create(
    s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md
    + s.container.layouts.vertical_center_layout
    + s.center_txt,
    "round_table_cell",
)


class BlockStyles:
    """Slide: Round Table — maximize-viewport archetype: structured grid."""
    heading = s.project.titles.slide_title + s.center_txt
    subtitle = Style.create(
        s.project.colors.accent + s.Large + s.center_txt,
        "round_table_subtitle",
    )
    label = Style.create(
        s.Large + s.text.wrap.hyphens,
        "round_table_label",
    )
    keyword = Style.create(
        s.Large + s.bold + s.project.colors.highlight + s.text.wrap.hyphens,
        "round_table_keyword",
    )
    keyword_accent = Style.create(
        s.Large + s.bold + s.project.colors.accent + s.text.wrap.hyphens,
        "round_table_keyword_accent",
    )
bs = BlockStyles


def build():
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Participant(s)", tag=t.div, toc_lvl="1")
            st_write(bs.subtitle, "Individual presentations", tag=t.div)

            with st_grid(
                cols="1fr 1fr",
                gap="16px",
                cell_styles=_cell,
            ) as g:
                with g.cell():
                    st_write(bs.label, "First name")
                    st_write(bs.label, "Main activities")
                    st_write(
                        bs.label,
                        (bs.keyword, "Motivations"),
                        (bs.label, " for participating"),
                    )

                with g.cell():
                    st_write(bs.label, "Experience (if any)")
                    st_write(
                        bs.label,
                        (bs.keyword_accent, "Artificial Intelligence"),
                    )
                    st_write(bs.keyword, "VibeCoding")
                    st_write(bs.label, "Software Engineering")
                    st_write(bs.label, "Past trainings")
