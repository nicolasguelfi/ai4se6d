"""Slide — Exercise 3: Redo with Discipline (8 min)."""
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
    "page_fill_ex_vibeeng",
)

_page_fill_center = ns(
    "display:flex;flex-direction:column;justify-content:center;"
    "align-items:center;min-height:85vh;gap:1.5rem;",
    "page_fill_ex_vibeeng_center",
)


class BlockStyles:
    """Exercise VibeEngineering slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    subheading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    timer = Style.create(
        s.GIANT + s.bold + s.center_txt + s.project.colors.highlight,
        "ex_ve_timer",
    )
    debrief_q = Style.create(
        s.Large + s.project.colors.accent,
        "ex_ve_debrief_q",
    )
bs = BlockStyles


_PROMPT = (
    f"{_PREFIX} A person at a desk with a glowing laptop, this time with a structured "
    "blueprint beside them and a checklist floating in the air. Code streams flow from "
    "the screen but pass through a filter/gate of teal light. Test tubes with green "
    f"checkmarks float nearby. Symbolizes disciplined AI-assisted development. {_SUFFIX}"
)


def build():
    # Sub-slide 1: Exercise instructions
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.heading, "Exercise 3: Redo with Discipline", tag=t.div, toc_lvl="1")
            st_write(bs.body, (bs.keyword_warn, "8 minutes"), tag=t.div)

            st_image(
                s.none,
                width="60%",
                editable=IS_EDITABLE,
                name="ex_vibeeng",
                prompt=_PROMPT,
                provider="openai",
                ai_size="1536x1024",
            )

            st_write(bs.body, "Take the ", (bs.keyword_warn, "SAME tool"), " from Exercise 2:", tag=t.div)

            with st_list(l_style=bs.body, li_style=bs.body, list_type=lt.ordered) as l:
                with l.item(): st_write(bs.body, "Write ", (bs.keyword, "3 requirements"), " first")
                with l.item(): st_write(bs.body, "Ask AI to generate ", (bs.keyword_accent, "tests BEFORE"), " implementation")
                with l.item(): st_write(bs.body, "Ask for implementation ", (bs.keyword, "passing tests"))
                with l.item(): st_write(bs.body, (bs.keyword_accent, "Review"), " test results")

    st_slide_break()

    # Sub-slide 2: Timer
    with st_block(_page_fill_center):
        st_write(bs.timer, "8:00", tag=t.div)

    st_slide_break()

    # Sub-slide 3: Debrief
    with st_block(_page_fill):
        with st_block(s.center_txt):
            st_write(bs.subheading, "Compare Both Approaches", tag=t.div)
            st_space("v", 1)

            with st_list(l_style=bs.debrief_q, li_style=bs.debrief_q, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.debrief_q, (bs.keyword, "Quality"), " \u2014 which result is more robust?")
                with l.item(): st_write(bs.debrief_q, (bs.keyword, "Confidence"), " \u2014 which do you trust more?")
                with l.item(): st_write(bs.debrief_q, (bs.keyword, "Speed"), " \u2014 was the overhead worth it?")
                with l.item(): st_write(bs.debrief_q, (bs.keyword_warn, "Trade-off"), " \u2014 where is the sweet spot?")
