"""Slide — Technical debt iceberg (balanced layout)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX

class BlockStyles:
    """Tech debt iceberg slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.highlight
    keyword_ok = s.bold + s.project.colors.accent
    quote = Style.create(
        s.Large + s.italic + s.project.colors.primary,
        "vc_danger_debt_quote",
    )
    source = s.project.citation + s.large
bs = BlockStyles

# Text cell: vertically centred, left-aligned (NG, 2026-11-23: recipes of the intro module)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"), "vc_danger_debt_text_cell")

_PROMPT = (
    f"{_PREFIX} An iceberg: small clean tip visible above a waterline in electric blue. "
    "Massive hidden mass below the surface in teal with amber cracks running through "
    "the submerged portion. The visible part is shiny and polished, the hidden part "
    f"is chaotic with broken connections and warning symbols. {_SUFFIX}"
)

_NOTES = [
    ("The message",
     "A vibe-coded prototype that works is only the tip: what you do not see is unmaintainable code, missing error handling, no tests and a brittle architecture."),
    ("The figures",
     "GitClear analysed 211 million changed lines (2020–2024): moved (refactored) lines fell from 25% to under 10%, copy/pasted lines rose from 8.3% to 12.3%; in 2024 copy/paste exceeded refactoring for the first time."),
    ("Why it matters",
     "Copy/paste instead of refactoring means the same logic duplicated in several places: every later fix must be made several times, and one copy is always forgotten. That is technical debt."),
    ("The trap",
     "The debt is invisible at demo time: the prototype runs. It shows up weeks later, when changing one feature breaks three others."),
    ("Link to the course",
     "VibeEngineering answers with tests before generation (P2), architectural intent (P3) and human review (P5)."),
    ("Ask the room",
     "« Who has ever inherited code that worked but that nobody dared to touch? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            # title and « i » on the same line, title smaller (NG, 2026-11-23)
            with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell(), st_zoom(80):
                    st_write(bs.heading+"zoom:1.3;", "The Iceberg", tag=t.div, toc_lvl="1")
                with h.cell():
                    st_hover_tooltip(title="Trainer notes — The Iceberg", entries=_NOTES,
                                     position="left", width="50vw")

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
                        name="vc_danger_debt",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    with st_zoom(105):   # text cell fills the slide (NG, 2026-11-23)
                        with st_zoom(100):
                            st_write(
                                bs.body,
                                (bs.keyword_ok, "What you see: "),
                                "working prototype.",
                            )
                            st_space("v", "2vh")
                            st_write(
                                bs.body,
                                (bs.keyword, "What\u2019s hidden: "),
                                "unmaintainable code, missing error handling, "
                                "no tests, brittle architecture.",
                            )
                            st_space("v", 2)
                            st_write(
                                bs.quote,
                                "211M changed lines, 2020\u20132024: refactored code fell "
                                "from 25% to under 10%, copy/paste rose from 8.3% to 12.3%"
                                " \u2014 copy/paste now exceeds refactoring.",
                            )
                            # REF: https://www.gitclear.com/ai_assistant_code_quality_2025_research
                            st_write(bs.source, cite("gitclear-quality2025"))
