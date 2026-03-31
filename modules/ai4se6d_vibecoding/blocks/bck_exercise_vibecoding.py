"""Slide — Exercise 2: Pure VibeCoding (10 min)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.styles import Style as ns
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_LANDSCAPE as _SUFFIX


# Viewport-filling containers
_page_fill = ns(
    "display:flex;flex-direction:column;justify-content:flex-start;"
    "min-height:85vh;gap:1.5rem;",
    "page_fill_ex_vibecoding",
)

_page_fill_center = ns(
    "display:flex;flex-direction:column;justify-content:center;"
    "align-items:center;min-height:85vh;gap:1.5rem;",
    "page_fill_ex_vibecoding_center",
)


class BlockStyles:
    """Exercise VibeCoding slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    subheading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_warn = s.bold + s.project.colors.highlight
    timer = Style.create(
        s.GIANT + s.bold + s.center_txt + s.project.colors.highlight,
        "ex_vc_timer",
    )
    debrief_q = Style.create(
        s.Large + s.project.colors.accent,
        "ex_vc_debrief_q",
    )
bs = BlockStyles


_PROMPT = (
    f"{_PREFIX} A person sitting at a desk with a glowing laptop, hands off the keyboard, "
    "speaking to the screen. Code streams flow from the screen autonomously. The person's "
    "expression is relaxed and trusting. Electric blue code, teal desk lamp, amber speech "
    f"bubbles. Symbolizes hands-off coding by conversation. {_SUFFIX}"
)


def build():
    # Sub-slide 1: Exercise instructions
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Exercise 2: Pure VibeCoding", tag=t.div, toc_lvl="1")
            st_write(bs.body, (bs.keyword_warn, "10 minutes"), tag=t.div)

            st_image(
                s.none,
                width="60%",
                editable=IS_EDITABLE,
                name="ex_vibecoding",
                prompt=_PROMPT,
                provider="openai",
                ai_size="1536x1024",
            )

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
                with l.item(): st_write(bs.body, "Open ", (bs.keyword, "Cursor"))
                with l.item(): st_write(bs.body, "Describe a small utility in ", (bs.keyword, "natural language"))
                with l.item(): st_write(bs.body, (bs.keyword_warn, "Accept ALL"), " generated code without reading it")
                with l.item(): st_write(bs.body, "Only test if it ", (bs.keyword, "works"))
                with l.item(): st_write(bs.body, (bs.keyword_warn, "DO NOT"), " look at the code")

    st_slide_break()

    # Sub-slide 2: Timer
    with st_block(_page_fill_center):
        st_write(bs.timer, "10:00", tag=t.div)

    st_slide_break()

    # Sub-slide 3: Debrief
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.subheading, "Debrief", tag=t.div)
            st_space("v", 1)

            with st_list(l_style=bs.debrief_q, li_style=bs.debrief_q, list_type=lt.ordered) as l:
                with l.item(): st_write(bs.debrief_q, "Does it work?")
                with l.item(): st_write(bs.debrief_q, "Do you trust it?")
                with l.item(): st_write(bs.debrief_q, "Would you ship it to production?")
                with l.item(): st_write(bs.debrief_q, "What could go wrong?")
                with l.item(): st_write(bs.debrief_q, "How did it feel not reading the code?")
