"""Slide — VibeCoding Principle 2: Trust in Output."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Principle 2 slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    number = Style.create(
        s.Giant + s.bold + s.project.colors.highlight + s.center_txt,
        "vc_trust_number",
    )
bs = BlockStyles

# Text cell: vertically centred, left-aligned (NG, 2026-11-23: same recipes as the intro module)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"),
                          "vc_trust_text_cell")

_NOTES = [
    ("The message",
     "Second principle: the code is judged by its behaviour, not by reading it. If the app runs and the screen looks "
     "right, the developer accepts it."),
    ("The idea explained",
     "« Works » is checked by trying the happy path once. Correct, efficient and maintainable are different "
     "questions: they need the code to be read, or tests to be run."),
    ("The trap",
     "« It works on my demo » hides what is not visible on screen: security, edge cases, error handling, structure. "
     "The next slides (dangers) show what this costs."),
    ("Link to the rest of the course",
     "VibeEngineering replaces « it works » with evidence: tests written before generation (P2) and human review at "
     "the boundaries (P5)."),
    ("Ask the room",
     "« How do you know that a piece of code you did not read is correct? »"),
]

_PROMPT = (
    f"{_PREFIX} A glowing checkmark in amber hovering over a code window outline in "
    "electric blue. The code lines inside are blurred and abstract, completely unread. "
    "The checkmark is crisp and confident. Represents accepting output without reading "
    f"the code, trusting the result over the implementation. {_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Trust in Output", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Trust in Output", entries=_NOTES,
                                 position="left", width="50vw")

        with st_grid(cols="1.5fr 3.5fr", gap="3vw",
                     cell_styles=[s.project.containers.grid_cell_centered, _text_cell]) as g:
            with g.cell():
                st_image(
                    s.none,
                    width="80%",
                    editable=IS_EDITABLE,
                    name="vc_trust",
                    prompt=_PROMPT,
                    provider="openai",
                    ai_size="1024x1536",
                )

            with g.cell():
                st_write(bs.number, "2")
                st_space("v", 1)
                with st_zoom(112):
                    st_write(
                        bs.body,
                        (bs.keyword, "If it works = good enough."),
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        "The developer accepts generated code based on whether "
                        "the application works, not on whether the code is correct, "
                        "efficient, or maintainable.",
                    )
                    st_space("v", 1)
                    st_write(
                        bs.body,
                        "The code itself is not read.",
                    )
