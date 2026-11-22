"""Slide — P1: Requirements Before Prompts."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """P1 slide styles."""
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    number = Style.create(
        s.Giant + s.bold + s.project.colors.highlight + s.center_txt,
        "ve_p1_number",
    )
bs = BlockStyles

# Text cell: vertically centred, left-aligned (NG, 2026-11-23: same recipes as the intro module)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"),
                          "ve_p_requirements_text_cell")

_NOTES = [
    ('The message',
     'First principle of VibeEngineering: write down WHAT the system must do (functional requirements) and HOW WELL (non-functional: performance, security, usability…) before the first prompt to the agent.'),
    ('The idea explained',
     'A prompt is not a specification. Everything the requirements leave out is decided by the model, silently; written requirements turn those hidden choices into explicit ones you can check.'),
    ('The analogy',
     "The client's order (allergies, preferences, occasion) is given before the kitchen starts, not after the dish is served."),
    ('The trap',
     'Writing requirements AFTER the code, to describe what the AI produced: they then document the result instead of steering it.'),
    ('Link to the course',
     'Tomorrow on CalcApp: requirements and acceptance criteria first, then generation.'),
    ('Ask the room',
     "« In this afternoon's FreeSelfApp, which requirement did you only discover once you saw the result? »"),
]

_PROMPT = (
    f"{_PREFIX} A solid foundation block in amber at the base, with a requirements "
    "checklist outline above it in electric blue. A faint chat prompt bubble waits "
    f"above. {_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            # title and « i » on the same line, title smaller (NG, 2026-11-23)
            with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell(), st_zoom(80):
                    st_write(bs.heading, "P1 — Requirements Before Prompts", tag=t.div, toc_lvl="1")
                with h.cell():
                    st_hover_tooltip(title="Trainer notes — P1 — Requirements Before Prompts", entries=_NOTES,
                                     position="left", width="50vw")

            with st_grid(cols="1.5fr 3.5fr", gap="3vw",
                         cell_styles=[s.project.containers.grid_cell_centered, _text_cell]) as g:
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="ve_p1_requirements",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    with st_zoom(70):   # the number smaller: more room for the text
                        st_write(bs.number, "1")
                    with st_zoom(125):
                        st_write(
                            bs.body,
                            (bs.keyword, "Functional and non-functional requirements"),
                            " are explicitly defined ",
                            (bs.keyword, "before"),
                            " engaging the AI agent.",
                        )
                        st_space("v", 1)
                        st_write(
                            bs.body,
                            (s.project.colors.muted, "The client's order — allergies, "
                            "preferences, occasion — before the kitchen starts."),
                        )
