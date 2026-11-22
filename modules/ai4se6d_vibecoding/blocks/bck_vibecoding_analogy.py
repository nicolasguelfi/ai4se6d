"""Slide — Historical analogy: LLM as the new compiler?"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """VibeCoding analogy slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    subheading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_warn = s.bold + s.project.colors.highlight
    emphasis = Style.create(
        s.Large + s.italic + s.project.colors.accent + s.center_txt,
        "vc_analogy_emphasis",
    )
bs = BlockStyles

# Text cell: vertically centred, left-aligned (NG, 2026-11-23: same recipes as the intro module)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"),
                          "vc_analogy_text_cell")

_NOTES = [
    ("The message",
     "An optimistic reading of VibeCoding: in the 1960s, high-level languages replaced assembly and programmers "
     "stopped writing machine code. Maybe LLMs are the next step: natural language replaces the programming "
     "language."),
    ("The idea explained",
     "The compiler became a trusted intermediary: nobody reads the machine code it produces. If the LLM became "
     "the same kind of intermediary, nobody would need to read the generated code."),
    ("Leave the question open",
     "Let the room answer before showing the next slide: the analogy is attractive, and part of it is true."),
    ("Ask the room",
     "« When did you last read the assembly produced by your compiler? Why not? »"),
]

_NOTES_DIFF = [
    ("The message",
     "The analogy breaks on one point: a compiler is deterministic, an LLM is stochastic."),
    ("The idea explained",
     "Same source, same compiler, same output — and compilers are specified and tested to translate faithfully. "
     "The same prompt can give different code from one run to the next, and sometimes wrong code."),
    ("The consequence",
     "We trust compilers because of that guarantee. Without it, the generated code must be checked: by tests, by "
     "review — which is what VibeEngineering adds."),
    ("Ask the room",
     "« Run the same prompt twice: do you get the same code? Should you be able to? »"),
]

_PROMPT = (
    f"{_PREFIX} A vintage punch-card machine morphing into a modern AI brain. Left side "
    "shows rigid geometric assembly patterns in muted blue. Right side shows fluid neural "
    "pathways in teal and amber. A timeline arrow runs beneath from 1960s to 2020s. "
    f"Symbolizes the evolution from assembly to AI-generated code. {_SUFFIX}"
)

def build():
    # Sub-slide 1: Historical parallel
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "LLM = The New Compiler?", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — LLM = The New Compiler?", entries=_NOTES,
                                 position="left", width="50vw")

        with st_grid(cols="1.5fr 3.5fr", gap="3vw",
                     cell_styles=[s.project.containers.grid_cell_centered, _text_cell]) as g:
            with g.cell():
                st_image(
                    s.none,
                    width="80%",
                    editable=IS_EDITABLE,
                    name="vc_analogy",
                    prompt=_PROMPT,
                    provider="openai",
                    ai_size="1024x1536",
                )

            with st_zoom(130), g.cell():
                st_write(
                    bs.body,
                    (s.project.colors.highlight + s.LARGE + s.bold, "1960s: "),
                    (bs.body, "High-level languages replaced assembly."),
                )
                st_space("v", 1)
                st_write(
                    bs.body,
                    (s.project.colors.muted,
                     "The compiler became the trusted intermediary \u2014 "
                     "programmers stopped writing machine code."),
                )
                st_space("v", 1)
                st_write(
                    bs.body,
                    (s.project.colors.highlight + s.LARGE + s.bold, "2025: "),
                    (bs.body, "LLMs generate code from natural language. "
                     "Are we seeing the same shift?"),
                )
    st_space("v", "20vh")
    st_slide_break()

    # Sub-slide 2: Critical difference — alternating rows, motif L2 + fonds f1 (NG, 2026-11-23)
    with st_block(s.project.containers.page_fill_top):
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.subheading, "The Critical Difference", tag=t.div, toc_lvl="2")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — The Critical Difference", entries=_NOTES_DIFF,
                                 position="left", width="50vw")
        st_space("v", "5vh")
        rows = [
            ("Compilers are deterministic", bs.keyword,
             "same input always produces the same output."),
            ("LLMs are stochastic", bs.keyword_warn,
             "same prompt can produce different (and sometimes wrong) code."),
        ]
        cols = "5% 35% 55% 5%"
        cells = s.project.containers.rows(len(rows), cols, filled=(2, 3))
        with st_zoom(115), st_grid(cols=cols, gap="3vh 0.5vw", cell_styles=cells) as g:
            for label, style, text in rows:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body + style, label, tag=t.div)
                with g.cell():
                    st_write(bs.body, text, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "5vh")
        with st_zoom(120):
            st_write(
                bs.emphasis,
                "You can trust a compiler blindly. Can you trust an LLM?",
            )
