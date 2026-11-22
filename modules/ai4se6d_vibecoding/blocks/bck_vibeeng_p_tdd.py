"""Slide — P2: Test-Driven Generation."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """P2 slide styles."""
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    number = Style.create(
        s.Giant + s.bold + s.project.colors.highlight + s.center_txt,
        "ve_p2_number",
    )
bs = BlockStyles

# Text cell: vertically centred, left-aligned (NG, 2026-11-23: same recipes as the intro module)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"),
                          "ve_p_tdd_text_cell")

_NOTES = [
    ('The message',
     'Tests are written BEFORE the implementation and act as the contract: the AI must generate code that passes them.'),
    ('The idea explained',
     'The test turns « it seems to work » into a check anyone can re-run. When the agent changes the code later, the same tests tell you at once whether something broke.'),
    ('The analogy',
     'Taste at every step, not just when the plate is served.'),
    ('The trap',
     'Letting the agent write the tests AFTER its own code: the tests then confirm what the code does, not what you wanted.'),
    ('Link to the course',
     'Acceptance criteria written tomorrow become the tests the generated code must pass.'),
    ('Ask the room',
     '« Who checks the tests, if the AI wrote both the code and the tests? »'),
]

_PROMPT = (
    f"{_PREFIX} A test tube or verification checkmark icon in amber standing tall "
    "on the left, casting a protective shadow over code blocks in electric blue. "
    f"{_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            # title and « i » on the same line, title smaller (NG, 2026-11-23)
            with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell(), st_zoom(80):
                    st_write(bs.heading, "P2 — Test-Driven Generation", tag=t.div, toc_lvl="1")
                with h.cell():
                    st_hover_tooltip(title="Trainer notes — P2 — Test-Driven Generation", entries=_NOTES,
                                     position="left", width="50vw")

            with st_grid(cols="1.5fr 3.5fr", gap="3vw",
                         cell_styles=[s.project.containers.grid_cell_centered, _text_cell]) as g:
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="ve_p2_tdd",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    with st_zoom(70):   # the number smaller: more room for the text
                        st_write(bs.number, "2")
                    with st_zoom(125):
                        st_write(
                            bs.body,
                            "Tests defined ",
                            (bs.keyword, "BEFORE"),
                            " implementation.<br>",
                            "Tests define the ",
                            (bs.keyword, "contract"),
                            ". AI generates code that must pass.",
                        )
                        st_space("v", 1)
                        st_write(
                            bs.body,
                            (s.project.colors.muted, "Taste at every step, not just "
                            "when the plate is served."),
                        )
