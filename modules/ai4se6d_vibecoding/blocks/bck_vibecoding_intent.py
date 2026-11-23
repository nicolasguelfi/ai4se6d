"""Slide — VibeCoding Principle 1: Intent over Implementation."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Principle 1 slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    number = Style.create(
        s.Giant + s.bold + s.project.colors.highlight + s.center_txt,
        "vc_intent_number",
    )
bs = BlockStyles

# Text cell: vertically centred, left-aligned (NG, 2026-11-23: same recipes as the intro module)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"),
                          "vc_intent_text_cell")

_NOTES = [
    ("The message",
     "The first principle of VibeCoding: the developer states the GOAL (« a page that lists my expenses by month ») "
     "and lets the model choose the code. The unit of work becomes the intent, not the line of code."),
    ("Why it is attractive",
     "No syntax, no framework to learn first: anyone who can describe the result gets a running program in minutes."),
    ("The catch",
     "Every decision you do not state (data model, error handling, security, libraries) is taken by the model, "
     "silently. You get A solution, not necessarily YOURS."),
    ("Link to the next days",
     "VibeEngineering keeps the intent but writes it down first: requirements and acceptance criteria (P1) before "
     "the prompt."),
    ("Ask the room",
     "« Last time you asked an AI for code, which decisions did it take for you without telling you? »"),
]

_PROMPT = (
    f"{_PREFIX} A thought bubble in amber floating above, connected by a beam of light "
    "down to a code block in electric blue below. The thought bubble is large and "
    "prominent, the code block smaller and subordinate. Represents intent driving "
    f"implementation, not the other way around. {_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Intent over Implementation", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Intent over Implementation", entries=_NOTES,
                                 position="left", width="50vw")

        with st_grid(cols="1.5fr 3.5fr", gap="3vw",
                     cell_styles=[s.project.containers.grid_cell_centered, _text_cell]) as g:
            with g.cell():
                st_image(
                    s.none,
                    width="80%",
                    editable=IS_EDITABLE,
                    name="vc_intent",
                    prompt=_PROMPT,
                    provider="openai",
                    ai_size="1024x1536",
                )

            with g.cell():
                st_write(bs.number, "1")
                st_space("v", "2vh")
                with st_zoom(120):
                    st_write(
                        bs.body,
                        (bs.keyword, "Describe WHAT you want,<br> "),
                        "not HOW to build it.",
                    )
                    st_space("v", "2vh")
                    st_write(
                        bs.body,
                        (s.project.colors.muted, "You specify the goal. The AI determines the implementation."),
                        "<br>The shift: from writing code to expressing intent.",
                    )
