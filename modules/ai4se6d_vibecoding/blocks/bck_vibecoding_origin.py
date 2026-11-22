"""Slide — VibeCoding origin: Karpathy quotes."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """VibeCoding origin slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    subheading = s.project.titles.section_title + s.center_txt
    quote = Style.create(
        s.Large + s.italic + s.text.wrap.hyphens,
        "vc_origin_quote",
    )
    quote_part1 = Style.create(
        s.Large + s.italic + s.project.colors.muted,
        "vc_origin_quote_p1",
    )
    quote_part2 = Style.create(
        s.Large + s.italic + s.project.colors.accent,
        "vc_origin_quote_p2",
    )
    quote_part3 = Style.create(
        s.Large + s.italic,
        "vc_origin_quote_p3",
    )
    attribution = Style.create(
        s.project.citation + s.large,
        "vc_origin_attribution",
    )
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
bs = BlockStyles

# Text cell: vertically centred, left-aligned (NG, 2026-11-23: same recipes as the intro module)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"),
                          "vc_origin_text_cell")

_NOTES = [
    ("The message",
     "« Vibe coding » is not an academic concept: it is a word coined by Andrej Karpathy in a post of 2 February "
     "2025, and it spread so fast that Collins named it Word of the Year 2025."),
    ("Two quotes, two years apart",
     "January 2023: « The hottest new programming language is English » — natural language as the interface to "
     "code. February 2025: « vibe coding » — you give in to the vibes and forget that the code even exists."),
    ("Read the second quote closely",
     "« I just see stuff, say stuff, run stuff, and copy paste stuff, and it mostly works. » The key word is "
     "MOSTLY: Karpathy described it for throwaway weekend projects, not for production."),
    ("Link to the rest of the session",
     "The next slides turn the quote into a definition and four principles; then come the dangers, and "
     "VibeEngineering as the answer."),
    ("Ask the room",
     "« Who had heard the term before today? In which context — a joke, a job offer, a product? »"),
]

_PROMPT = (
    f"{_PREFIX} A relaxed developer lounging on a beanbag with headphones and a laptop, "
    "casually talking to a glowing AI chat bubble floating above the screen. "
    "Code streams flow autonomously from the chat bubble into the laptop. "
    "The developer is smiling, vibing, not typing — just speaking. "
    "Neon purple and electric blue ambient lighting, lo-fi aesthetic. "
    "A speech bubble from the developer says a single word in English. "
    f"Captures the essence of conversational programming and vibe coding. {_SUFFIX}"
)

def build():
    # Sub-slide 1: Karpathy quote + Collins badge
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "The Birth of VibeCoding", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — The Birth of VibeCoding", entries=_NOTES,
                                 position="left", width="50vw")

        with st_grid(cols="1.5fr 3.5fr", gap="3vw",
                     cell_styles=[s.project.containers.grid_cell_centered, _text_cell]) as g:
            with g.cell():
                st_image(
                    s.none,
                    width="80%",
                    editable=IS_EDITABLE,
                    name="vc_origin",
                    prompt=_PROMPT,
                    provider="openai",
                    ai_size="1024x1536",
                )

            with g.cell():
                with st_zoom(95):
                    # Quote 1: "The hottest new programming language is English"
                    # Tweet: Jan 24, 2023
                    st_write(
                        bs.quote_part3,
                        "\u201CThe hottest new programming language is English\u201D",
                    )
                    # REF: https://x.com/karpathy/status/1617979122625712128
                    st_write(bs.attribution, cite("karpathy2023english"))

                    st_space("v", "3vh")

                    # Quote 2: "Vibe coding" definition
                    # Tweet: Feb 2, 2025 (23:17 UTC)
                    st_write(
                        bs.quote,
                        (bs.quote_part1,
                        "\u201CThere\u2019s a new kind of coding<br/>"
                        "I call \u201Cvibe coding\u201D, "
                        "where you fully give in to the vibes (\u2026) "
                        "and forget that the code even exists."),
                        (bs.quote_part2,
                        " (\u2026) I just see stuff, say stuff, run stuff, "
                        "and copy paste stuff, and it mostly works.\u201D"),
                    )
                    # REF: https://x.com/karpathy/status/1886192184808149383
                    st_write(bs.attribution, cite("karpathy2025vibecoding"))

                    st_space("v", "3vh")
                    st_write(
                        bs.body,
                        (bs.keyword_accent, "Collins English Dictionary"),
                        " \u2014 Word of the Year 2025 ",
                        (bs.attribution, cite("collins-woty2025")),
                    )

    # Definition and paradigm shift are now in separate blocks:
    # bck_vibecoding_definition and bck_vibecoding_paradigm
