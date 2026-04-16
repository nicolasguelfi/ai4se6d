"""Slide — The Productivity Paradox: contrasting Cui vs METR."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    col_ok = Style.create(
        s.Large + s.bold + s.project.colors.success + s.center_txt,
        "gs_ev_par_ok",
    )
    col_warn = Style.create(
        s.Large + s.bold + s.project.colors.highlight + s.center_txt,
        "gs_ev_par_warn",
    )
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    label = s.project.titles.label
    takeaway = Style.create(
        s.project.titles.body_accent + s.center_txt,
        "gs_ev_par_takeaway",
    )
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_zoom(90):
                st_write(bs.heading, "The Productivity Paradox", tag=t.div, toc_lvl="1")
            st_space("v", 1)

        with st_grid(
            cols=s.project.containers.responsive_2col,
            gap="32px",
            cell_styles=s.project.containers.cell_primary_bg
            + s.project.containers.cell_pad_md,
        ) as g:
            with g.cell():
                st_write(bs.col_ok, "Cui et al. \u2014 Gains", tag=t.div)
                st_space("v", 0.5)
                st_write(bs.body, "4,867 developers, enterprise setting, structured tasks.")
                st_write(
                    bs.body,
                    (s.bold + s.project.colors.success, "+26%"),
                    " completed tasks.",
                )

            with g.cell():
                st_write(bs.col_warn, "METR \u2014 Slowdown", tag=t.div)
                st_space("v", 0.5)
                st_write(bs.body, "16 developers, OSS, familiar codebases.")
                st_write(
                    bs.body,
                    (s.bold + s.project.colors.highlight, "\u221219%"),
                    " actual speed.",
                )

        st_space("v", 1)
        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
            with l.item():
                st_write(bs.body, (bs.label, "1. "), "Prompt engineering overhead on familiar code")
            with l.item():
                st_write(bs.body, (bs.label, "2. "), "AI disrupts established mental models")
            with l.item():
                st_write(bs.body, (bs.label, "3. "), "Context-switching between AI and manual work")

        st_space("v", 1)
        st_write(
            bs.takeaway,
            "Scale, context, and expertise level determine whether AI helps or hinders.",
        )
