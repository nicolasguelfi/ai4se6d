"""Slide — P6: Context Engineering (skippable)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """P6 slide styles."""
    heading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    accent = s.bold + s.project.colors.accent
    number = Style.create(
        s.Giant + s.bold + s.project.colors.highlight + s.center_txt,
        "ve_p6_number",
    )
bs = BlockStyles

# Text cell: vertically centred, left-aligned (NG, 2026-11-23: same recipes as the intro module)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"),
                          "ve_p_context_text_cell")

_NOTES = [
    ('The message',
     'Systematically managing the information fed to AI agents: project rules, memory and tool configurations.'),
    ('The idea explained',
     'Not clever prompting: the quality of the answer depends on what the agent sees. Project rules, MCP servers and memory systems decide that — the agent sees what you curate.'),
    ('The analogy',
     'Your pantry, your prep, your standards — maintained every day, not just on opening night.'),
    ('The trap',
     'Too much context is also a problem: the longer the context, the less reliable the model (see the intro module) — curate, do not dump.'),
    ('Link to the course',
     'AGENTS.md, MCP and the project memory come back in the tools part and on day 2.'),
    ('Ask the room',
     '« What does the agent need to know about your project that is written nowhere today? »'),
]

_PROMPT = (
    f"{_PREFIX} A central hub circle in amber surrounded by orbiting information "
    "spheres in electric blue and teal — documents, rules, tools. Lines connect "
    f"everything. {_SUFFIX}"
)

def build():
    with st_block(s.project.containers.page_fill_top):
        with st_block(s.center_txt):
            # title and « i » on the same line, title smaller (NG, 2026-11-23)
            with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
                with h.cell(), st_zoom(100):
                    st_write(bs.heading, "P6 — Context Engineering", tag=t.div, toc_lvl="1")
                with h.cell():
                    st_hover_tooltip(title="Trainer notes — P6 — Context Engineering", entries=_NOTES,
                                     position="left", width="50vw")

            with st_grid(cols="1.5fr 3.5fr", gap="3vw",
                         cell_styles=[s.project.containers.grid_cell_centered, _text_cell]) as g:
                with g.cell():
                    st_image(
                        s.none,
                        width="80%",
                        editable=IS_EDITABLE,
                        name="ve_p6_context",
                        prompt=_PROMPT,
                        provider="openai",
                        ai_size="1024x1536",
                    )

                with g.cell():
                    with st_zoom(70):   # the number smaller: more room for the text
                        st_write(bs.number, "6")
                    with st_zoom(88):
                        st_write(
                            bs.body,
                            (bs.keyword, "Systematically managing"),
                            " the information fed to AI agents.",
                        )
                        st_space("v", "2vh")
                        # NG, 2026-11-23: one paragraph; accent = the idea, blue = the three levers, muted = the example
                        st_write(
                            bs.body,
                            "An agent\u2019s ",
                            (bs.accent, "context goes beyond the prompt"),
                            ". You shape it through ",
                            (bs.keyword, "project rules"),
                            ", ",
                            (bs.keyword, "memory"),
                            ", and ",
                            (bs.keyword, "the tools you give the agent"),
                            (bs.body, " (for example, through MCP servers)"),
                            ".",
                        )
                        st_space("v", "6vh")
                        st_write(
                            bs.body,
                            (s.project.colors.muted, "Your pantry, your prep, your standards "
                            "\u2014 maintained every day, not just on opening night."),
                        )
