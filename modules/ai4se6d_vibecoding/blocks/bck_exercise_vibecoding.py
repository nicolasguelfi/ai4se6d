"""Slide — This Afternoon: Pure VibeCoding (framing for FreeSelfApp workshop)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_LANDSCAPE as _SUFFIX

class BlockStyles:
    """Exercise VibeCoding framing slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_warn = s.bold + s.project.colors.highlight
    watch_q = Style.create(
        s.Large + s.project.colors.accent,
        "ex_vc_watch_q",
    )
    transition = Style.create(
        s.large + s.italic + s.center_txt + s.project.colors.muted,
        "ex_vc_transition",
    )
bs = BlockStyles

_PROMPT = (
    f"{_PREFIX} A person sitting at a desk with a glowing laptop, hands off the keyboard, "
    "speaking to the screen. Code streams flow from the screen autonomously. The person's "
    "expression is relaxed and trusting. Electric blue code, teal desk lamp, amber speech "
    f"bubbles. Symbolizes hands-off coding by conversation. {_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "This Afternoon: Pure VibeCoding", tag=t.div, toc_lvl="1")
            st_write(bs.body, (bs.keyword, "FreeSelfApp Workshop"), " \u2014 1h45 with Tiago", tag=t.div)

            st_image(
                s.none,
                width="50%",
                editable=IS_EDITABLE,
                name="ex_vibecoding",
                prompt=_PROMPT,
                provider="openai",
                ai_size="1536x1024",
            )

            st_write(
                bs.body,
                "This afternoon, you will experience pure VibeCoding first-hand. "
                "You'll describe a project in natural language and let Cursor generate everything.",
            )
            st_space("v", 1)

            st_write(bs.body, (bs.keyword_warn, "What to Watch For"), tag=t.div)
            st_space("v", 0.5)
            with st_list(l_style=bs.watch_q, li_style=bs.watch_q, list_type=lt.ordered) as l:
                with l.item(): st_write(bs.watch_q, "Does the result actually work?")
                with l.item(): st_write(bs.watch_q, "Do you trust code you haven't read?")
                with l.item(): st_write(bs.watch_q, "Would you ship this to production?")
                with l.item(): st_write(bs.watch_q, "What risks are hiding in the generated code?")
                with l.item(): st_write(bs.watch_q, "How does it feel to give up control?")

            st_space("v", 1)
            st_write(
                bs.transition,
                "Keep these questions in mind \u2014 we'll debrief at 4:30 PM",
            )
