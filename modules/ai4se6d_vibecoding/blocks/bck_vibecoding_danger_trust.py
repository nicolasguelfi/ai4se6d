"""Slide — The Trust Crisis: developer confidence in AI is falling."""
# @guideline: maximize-viewport
# @pattern: ptn_stat_hero
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Trust Crisis stat-hero styles."""
    heading = s.project.titles.slide_title + s.center_txt
    stat = s.project.titles.stat_hero
    sub_stat = Style.create(
        s.Large + s.project.colors.muted,
        "vc_danger_trust_sub",
    )
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_warn = s.bold + s.project.colors.highlight
    source = s.project.citation + s.large
    closing = Style.create(
        s.Large + s.bold + s.project.colors.accent,
        "vc_danger_trust_closing",
    )
bs = BlockStyles

# Text cell: vertically centred, left-aligned (NG, 2026-11-23: recipes of the intro module)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"), "vc_danger_trust_text_cell")

_PROMPT = (
    f"{_PREFIX} A large downward-trending graph line in amber, starting high on the left "
    "and dropping sharply to the right. A broken trust icon (handshake with a crack "
    "through it) in electric blue at the bottom of the curve. "
    "Represents declining developer confidence "
    f"in AI accuracy over time. {_SUFFIX}"
)


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            with st_grid(cols="95% 5%", gap="0px", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell(), st_zoom(80):   # one-line title
                    st_write(bs.heading, "The Trust Crisis", tag=t.div, toc_lvl="1")
                with h.cell():
                    st_hover_tooltip(
                        title="Trainer notes \u2014 The Trust Crisis",
                        entries=[
                            (
                                "33% trust (2025)",
                                "33% of developers trust the accuracy of AI "
                                "output (2024: 43%), while AI use rose from "
                                "76% to 84%. Only 3% trust it highly.",
                            ),
                            (
                                "46% distrust",
                                "More developers distrust AI accuracy "
                                "(46%, up from 31% in 2024) than trust it.",
                            ),
                            (
                                "66% frustrated",
                                "Top frustration: AI solutions that are "
                                "\"almost right, but not quite\".",
                            ),
                            (
                                "45% debugging",
                                "Debugging AI-generated code is more "
                                "time-consuming (2nd frustration).",
                            ),
                            (
                                "2026 survey",
                                "Question reworded: 48% trust AI output only "
                                "when they can easily verify it "
                                "(published 6 Oct 2026).",
                            ),
                        ],
                        position="left", width="50vw",
                    )

            with st_grid(
                cols="1.5fr 3.5fr",
                gap="3vw",
                cell_styles=[s.project.containers.grid_cell_centered, _text_cell],
            ) as g:
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="vc_danger_trust",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    with st_zoom(85):   # text cell fills the slide (NG, 2026-11-23)
                        with st_zoom(60):
                            st_write(bs.stat, "33%")
                        st_write(
                            bs.sub_stat,
                            "of developers trust AI output accuracy (2025)",
                        )
                        st_write(
                            bs.sub_stat,
                            "down from 43% in 2024",
                        )
                        st_space("v", 0.5)

                        with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.unordered, text_align="left", item_gap=0.6) as l:
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword_warn, "46%"),
                                    " ",
                                    (bs.keyword_warn, "distrust"),
                                    " the accuracy of AI output",
                                )
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword_warn, "66%"),
                                    " top frustration: ",
                                    "\u201calmost right, but not quite\u201d",
                                )
                            with l.item():
                                st_write(
                                    bs.body,
                                    (bs.keyword, "45%"),
                                    ": ",
                                    (bs.keyword_warn, "debugging AI code"),
    " takes longer",
                                )

                        st_space("v", 0.5)
                        # REF: Stack Overflow Developer Surveys 2024, 2025, 2026
                        st_write(
                            bs.source,
                            cite("so-survey2025"), " · ", cite("so-survey2026"),
                        )
                        st_space("v", 0.5)
                        st_write(
                            bs.closing,
                            "Adoption is rising. Trust is falling. Verify before you trust.",
                        )
