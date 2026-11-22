"""Slide — The Experience Gap: AI doesn't help everyone equally."""
# @guideline: maximize-viewport
# @pattern: ptn_stat_hero
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Experience Gap stat-hero styles."""
    heading = s.project.titles.slide_title + s.center_txt
    stat_junior = Style.create(
        s.giant + s.bold + s.project.colors.primary + s.center_txt,
        "ve_evidence_gap_junior",
    )
    stat_senior = Style.create(
        s.giant + s.bold + s.project.colors.muted + s.center_txt,
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

_NOTES = [
    ('The message',
     'AI does not help everyone equally: short-tenure developers gain +27–39%, long-tenure developers +8–13%.'),
    ('The study',
     'Cui et al. (2024): three field experiments, 4,867 developers in total, with access to an AI coding assistant in their real jobs.'),
    ('Reading it',
     'AI compensates for missing experience: it fills gaps in syntax, libraries and patterns. Experts gain less because those gaps are small for them.'),
    ('The trap',
     'Gaining speed is not gaining judgment: the junior who ships faster still needs to know what to check — AI cannot replace expert judgment.'),
    ('Link to the course',
     'This is why review (P5) and requirements (P1) matter most for those who gain most.'),
    ('Ask the room',
     '« Where does AI make you faster — and where would you not notice its mistakes? »'),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            # title and « i » on the same line, title smaller (NG, 2026-11-23)
            with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell(), st_zoom(80):
                    st_write(bs.heading, "The Experience Gap", tag=t.div, toc_lvl="1")
                with h.cell():
                    st_hover_tooltip(title="Trainer notes — The Experience Gap", entries=_NOTES,
                                     position="left", width="50vw")
            st_space("v", 4)

            with st_grid(
                cols="1fr 1fr",
                gap="32px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    st_write(bs.stat_junior, "+27\u201339%")
                    st_write(bs.label, "Short-tenure developers")

                with g.cell():
                    st_write(bs.stat_senior, "+8\u201313%")
                    st_write(bs.label, "Long-tenure developers")

            st_space("v", 1)
            with st_zoom(130):
                st_write(
                    bs.body,
                    (bs.keyword, "4,867"),
                    " developers \u2014 3 field experiments ",
                )
                # REF: Cui et al. 2024, SSRN 4945566
                st_write(bs.source, cite("cui-fieldexperiments2024"))

            st_space("v", 4)
            with st_zoom(150):
                st_write(
                    bs.closing,
                    "AI compensates for missing experience \u2014 but cannot replace expert judgment.",
                )
