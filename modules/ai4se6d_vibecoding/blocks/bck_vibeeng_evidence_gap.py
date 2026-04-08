"""Slide — The Experience Gap: AI doesn't help everyone equally."""
# @guideline: maximize-viewport
# @pattern: stat-hero
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s

class BlockStyles:
    """Experience Gap stat-hero styles."""
    heading = s.project.titles.slide_title + s.center_txt
    stat_junior = Style.create(
        s.GIANT + s.bold + s.project.colors.primary + s.center_txt,
        "ve_evidence_gap_junior",
    )
    stat_senior = Style.create(
        s.GIANT + s.bold + s.project.colors.muted + s.center_txt,
        "ve_evidence_gap_senior",
    )
    label = Style.create(
        s.Large + s.bold + s.center_txt,
        "ve_evidence_gap_label",
    )
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    source = s.project.citation + s.large + s.center_txt
    closing = Style.create(
        s.Large + s.bold + s.center_txt + s.project.colors.accent,
        "ve_evidence_gap_closing",
    )
bs = BlockStyles


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "The Experience Gap", tag=t.div, toc_lvl="1")
            st_space("v", 1)

            with st_grid(
                cols="1fr 1fr",
                gap="32px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    st_write(bs.stat_junior, "+27\u201339%")
                    st_write(bs.label, "Junior developers")

                with g.cell():
                    st_write(bs.stat_senior, "+8\u201313%")
                    st_write(bs.label, "Senior developers")

            st_space("v", 1)
            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword, "4,867"),
                        " developers across Microsoft, Accenture, Fortune 100",
                    )
                with l.item():
                    st_write(
                        bs.body,
                        "3 independent field experiments combined",
                    )
                with l.item():
                    st_write(
                        bs.body,
                        "Overall: ",
                        (bs.keyword, "+26%"),
                        " increase in completed tasks",
                    )

            st_space("v", 0.5)
            # REF: Cui et al. 2024, SSRN 4945566
            st_write(bs.source, cite("cui-fieldexperiments2024"))
            st_space("v", 1)

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered) as l:
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword, "Juniors benefit most"),
                        " \u2014 AI compensates for missing experience",
                    )
                with l.item():
                    st_write(
                        bs.body,
                        (bs.keyword_accent, "Seniors gain less"),
                        " \u2014 their expertise is harder to replicate",
                    )

            st_space("v", 1)
            st_write(
                bs.closing,
                "This is why VibeEngineering matters: structure what AI can\u2019t infer",
            )
