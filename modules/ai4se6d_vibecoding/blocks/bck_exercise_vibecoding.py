"""Slide — This Afternoon: Pure VibeCoding (framing for FreeSelfApp workshop)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_LANDSCAPE as _SUFFIX
from shared_widgets import st_hover_tooltip

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

# Text cell: vertically centred, left-aligned (NG, 2026-11-23: same recipes as the intro module)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"),
                          "ex_vc_text_cell")

_NOTES = [
    ("The message",
     "Framing of this afternoon's workshop: you will practise pure VibeCoding yourselves, on purpose, before we "
     "look at its dangers."),
    ("What participants do",
     "Describe a project in natural language and let opencode — the coding agent installed after lunch — "
     "generate everything."),
    ("Why first-hand",
     "The dangers in the next slides are more convincing when everyone has their own vibe-coded app on screen: "
     "« We'll see yours soon! »"),
    ("Link to tomorrow",
     "Day 2 applies VibeEngineering to the same kind of work, so participants can compare the two ways."),
    ("Ask the room",
     "« What app would you build this afternoon if it cost you nothing? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "This Afternoon: Pure VibeCoding", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — This Afternoon: Pure VibeCoding", entries=_NOTES,
                                 position="left", width="50vw")

        with st_grid(cols="1.5fr 3.5fr", gap="3vw",
                     cell_styles=[s.project.containers.grid_cell_centered, _text_cell]) as g:
            with g.cell():
                st_image(
                    s.none,
                    width="100%",
                    editable=IS_EDITABLE,
                    name="ex_vibecoding",
                    prompt=_PROMPT,
                    provider="openai",
                    ai_size="1536x1024",
                )

            with g.cell(), st_zoom(130):
                st_write(bs.body + bs.keyword, "FreeSelfApp Workshop", tag=t.div)
                st_space("v", 1)
                st_write(
                    bs.body,
                    "This afternoon, you will practice self-generated code with VibeCoding first-hand. "
                    "You'll describe a project in natural language and let opencode, the coding agent you install after lunch, generate everything.",
                )
