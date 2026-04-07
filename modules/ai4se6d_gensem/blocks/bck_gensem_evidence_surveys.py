"""Slide — Five Developer Surveys overview."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    header = s.project.titles.table_header
    cell = s.project.titles.table_cell
    label = s.project.titles.table_label
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles

_SURVEYS = [
    ("Stack Overflow 2025", "65K", "84% AI use, trust fell to 29%"),
    ("JetBrains 2025", "24.5K", "85% AI use, Cursor usage 17x YoY"),
    ("GitLab DevSecOps", "3.3K", "7h/week lost to AI inefficiencies"),
    ("Pragmatic Engineer", "2.6K", "85% AI use, agents overtaking autocomplete"),
    ("GitHub Octoverse", "\u2014", "98% increase in new AI projects"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Five Developer Surveys", tag=t.div, toc_lvl="1")
            st_space("v", 1)

        # Header row
        with st_grid(
            cols="30% 15% 55%",
            gap="8px",
            cell_styles=s.project.containers.table_header_cell,
        ) as g:
            with g.cell():
                st_write(bs.header, "Survey")
            with g.cell():
                st_write(bs.header, "N")
            with g.cell():
                st_write(bs.header, "Key Finding")

        # Data rows
        for survey_name, n, finding in _SURVEYS:
            with st_grid(
                cols="30% 15% 55%",
                gap="8px",
                cell_styles=s.project.containers.table_normal_cell,
            ) as g:
                with g.cell():
                    st_write(bs.label, survey_name)
                with g.cell():
                    st_write(bs.cell, n)
                with g.cell():
                    st_write(bs.cell, finding)

        st_space("v", 1)
        st_write(
            bs.source,
            cite("stackoverflow-survey2025"), ", ",
            cite("jetbrains-survey2025"), ", ",
            cite("gitlab-devsecops2025"),
        )
