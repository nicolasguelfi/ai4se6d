"""Slide — Tomorrow: VibeEngineering in Practice (framing for Day 2 CalcApp)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_LANDSCAPE as _SUFFIX

class BlockStyles:
    """Exercise VibeEngineering framing slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    watch_q = Style.create(
        s.Large + s.project.colors.accent,
        "ex_ve_watch_q",
    )
    transition = Style.create(
        s.large + s.italic + s.center_txt + s.project.colors.muted,
        "ex_ve_transition",
    )
bs = BlockStyles

_PROMPT = (
    f"{_PREFIX} A person at a desk with a glowing laptop, this time with a structured "
    "blueprint beside them and a checklist floating in the air. Code streams flow from "
    "the screen but pass through a filter/gate of teal light. Test tubes with green "
    f"checkmarks float nearby. Symbolizes disciplined AI-assisted development. {_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            st_write(bs.heading, "Tomorrow: VibeEngineering in Practice", tag=t.div, toc_lvl="1")
            st_write(bs.body, (bs.keyword, "CalcApp v0.1"), " \u2014 Day 2 with Tiago", tag=t.div)

            st_image(
                s.none,
                width="50%",
                editable=IS_EDITABLE,
                name="ex_vibeeng",
                prompt=_PROMPT,
                provider="openai",
                ai_size="1536x1024",
            )

            st_write(
                bs.body,
                "Tomorrow, you'll apply these 6 principles to a real project. "
                "Requirements first, acceptance criteria before generation, architecture declared.",
            )
            st_space("v", 1)

            st_write(bs.body, (bs.keyword_warn, "Compare Both Approaches"), tag=t.div)
            st_space("v", 0.5)
            with st_list(l_style=bs.watch_q, li_style=bs.watch_q, list_type=lt.unordered) as l:
                with l.item(): st_write(bs.watch_q, (bs.keyword, "Quality"), " \u2014 which result is more robust?")
                with l.item(): st_write(bs.watch_q, (bs.keyword, "Confidence"), " \u2014 which do you trust more?")
                with l.item(): st_write(bs.watch_q, (bs.keyword, "Speed"), " \u2014 was the overhead worth it?")
                with l.item(): st_write(bs.watch_q, (bs.keyword_warn, "Trade-off"), " \u2014 where is the sweet spot?")

            st_space("v", 1)
            st_write(
                bs.transition,
                "After today's FreeSelfApp and tomorrow's CalcApp \u2014 you'll have experienced both sides",
            )
