"""Slide — VibeCoding Principle 3: Conversational Iteration."""
# @guideline: maximize-viewport

from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Principle 3 slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    number = Style.create(
        s.Giant + s.bold + s.project.colors.highlight + s.center_txt,
        "vc_conversation_number",
    )
bs = BlockStyles

# Text cell: vertically centred, left-aligned (NG, 2026-11-23: same recipes as the intro module)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"),
                          "vc_conversation_text_cell")

_NOTES = [
    ("The message",
     "Third principle: when something breaks, the developer does not open the code. They describe the symptom "
     "(« the button does nothing ») and ask the model to fix it."),
    ("The idea explained",
     "Debugging becomes a conversation: prompt, run, describe what is wrong, prompt again. The loop is fast and "
     "needs no knowledge of the implementation."),
    ("The trap",
     "Each fix is made without understanding the cause: the model may patch the symptom, break something else, or "
     "go round in circles. The codebase grows by layers nobody has read."),
    ("Link to the rest of the course",
     "VibeEngineering keeps the conversation but plans it: iterations with a defined scope, acceptance criteria and "
     "review gates (P4)."),
    ("Ask the room",
     "« After five rounds of “it still doesn’t work”, what do you do? »"),
]

_PROMPT = (
    f"{_PREFIX} A spiral conversation pattern: alternating speech bubbles in electric "
    "blue (human) and teal (AI), spiraling inward toward a solution point in amber at "
    "the center. Each iteration is closer to the center. Represents debugging by "
    f"describing symptoms rather than reading code. {_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Conversational Iteration", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Conversational Iteration", entries=_NOTES,
                                 position="left", width="50vw")

        with st_grid(cols="1.5fr 3.5fr", gap="3vw",
                     cell_styles=[s.project.containers.grid_cell_centered, _text_cell]) as g:
            with g.cell():
                st_image(
                    s.none,
                    width="80%",
                    editable=IS_EDITABLE,
                    name="vc_conversation",
                    prompt=_PROMPT,
                    provider="openai",
                    ai_size="1024x1536",
                )

            with g.cell():
                st_write(bs.number, "3")
                st_space("v", 1)
                with st_zoom(100):
                    st_write(
                        bs.body,
                        (bs.keyword, "Bug? Describe the symptom.\nThe AI fixes it."),
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        (s.project.colors.muted,
                        "Errors are addressed by describing the problem back "
                        "to the LLM rather than by reading and debugging "
                        "the code directly."),
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        "No need to understand the implementation.",
                    )
