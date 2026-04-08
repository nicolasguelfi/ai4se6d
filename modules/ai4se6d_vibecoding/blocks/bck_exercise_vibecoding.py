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
            st_write(bs.body, "FreeSelfApp Workshop", tag=t.div)

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
                "This afternoon, you will practice self-generated code with VibeCoding first-hand. "
                "You'll describe a project in natural language and let Cursor generate everything.",
            )
