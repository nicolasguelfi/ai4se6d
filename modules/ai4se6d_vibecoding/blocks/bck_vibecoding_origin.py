"""Slide — VibeCoding origin: Karpathy quotes."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX

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
    attribution_orange = Style.create(
        s.large + s.italic + s.project.colors.highlight,
        "vc_origin_attr_orange",
    )
    attribution = Style.create(
        s.project.titles.caption,
        "vc_origin_attribution",
    )
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
bs = BlockStyles

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
        with st_block(s.center_txt):
            st_write(bs.heading, "The Birth of VibeCoding", tag=t.div, toc_lvl="1")

            with st_grid(
                cols="2fr 3fr",
                gap="24px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
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
                    # Quote 1: "The hottest new programming language is English"
                    # Tweet: Jan 24, 2023
                    st_write(
                        bs.quote_part3,
                        "\u201CThe hottest new programming language is English\u201D",
                    )
                    # REF: https://x.com/karpathy/status/1617979122625712128
                    st_write(bs.attribution_orange, cite("karpathy2023english"))

                    st_space("h", "1.5rem")

                    # Quote 2: "Vibe coding" definition
                    # Tweet: Feb 3, 2025
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
                    st_write(bs.attribution_orange, cite("karpathy2025vibecoding"))

    # Definition and paradigm shift are now in separate blocks:
    # bck_vibecoding_definition and bck_vibecoding_paradigm
