"""Slide — P3: Architectural Intent."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """P3 slide styles."""
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    accent = s.bold + s.project.colors.accent
    number = Style.create(
        s.Giant + s.bold + s.project.colors.highlight + s.center_txt,
        "ve_p3_number",
    )
bs = BlockStyles

# Text cell: vertically centred, left-aligned (NG, 2026-11-23: same recipes as the intro module)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"),
                          "ve_p_architecture_text_cell")

_NOTES = [
    ('The message',
     'Design decisions (patterns, components, boundaries) are taken BEFORE generation, by the humans.'),
    ('The idea explained',
     'Context files carry these decisions to the agent at every session: AGENTS.md (the shared standard), CLAUDE.md or Cursor rules in other tools. The agent then generates inside the architecture instead of inventing one.'),
    ('The analogy',
     'The menu is designed before the kitchen opens.'),
    ('The trap',
     'Letting each prompt decide the structure: every session adds its own patterns and the code base drifts.'),
    ('Link to the course',
     'AGENTS.md comes back on day 2; opencode drafts one with /init.'),
    ('Ask the room',
     '« Which architecture decision would you never let an agent take alone? »'),
]

_PROMPT = (
    f"{_PREFIX} A blueprint wireframe of a building in electric blue with project "
    "rule cards floating nearby in teal. An amber compass indicates direction. "
    f"{_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            # title and « i » on the same line, title smaller (NG, 2026-11-23)
            with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell(), st_zoom(80):
                    st_write(bs.heading, "P3 — Architectural Intent", tag=t.div, toc_lvl="1")
                with h.cell():
                    st_hover_tooltip(title="Trainer notes — P3 — Architectural Intent", entries=_NOTES,
                                     position="left", width="50vw")

            with st_grid(cols="1.5fr 3.5fr", gap="3vw",
                         cell_styles=[s.project.containers.grid_cell_centered, _text_cell]) as g:
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="ve_p3_architecture",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    with st_zoom(70):   # the number smaller: more room for the text
                        st_write(bs.number, "3")
                    with st_zoom(100):
                        st_write(
                            bs.body,
                            (bs.keyword, "Design decisions BEFORE generation"),
                            " \u2014 patterns, components, boundaries.",
                        )
                        st_space("v", 1)
                        st_write(
                            bs.body,
                            "Context files (",
                            (bs.accent, "AGENTS.md"),
                            "; CLAUDE.md, Cursor rules elsewhere"
                            ") communicate these constraints to the AI.",
                        )
                        st_space("v", 1)
                        st_write(
                            bs.body,
                            (s.project.colors.muted, "The menu is designed before "
                            "the kitchen opens."),
                        )
