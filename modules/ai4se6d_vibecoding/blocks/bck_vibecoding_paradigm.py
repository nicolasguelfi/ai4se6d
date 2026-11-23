"""Slide — Paradigm shift: from cook to customer (kitchen metaphor seeding)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from custom.config import IS_EDITABLE
from custom.prompts import AI_PREFIX as _PREFIX, AI_SUFFIX_PORTRAIT as _SUFFIX
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Paradigm shift slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    subheading = s.project.titles.section_title + s.center_txt
    body = s.project.titles.body
    keyword = s.bold + s.project.colors.primary
    keyword_accent = s.bold + s.project.colors.accent
    keyword_warn = s.bold + s.project.colors.highlight
    emphasis = Style.create(
        s.Large + s.italic + s.project.colors.highlight + s.center_txt,
        "vc_paradigm_emphasis",
    )
bs = BlockStyles

# Text cell: vertically centred, left-aligned (NG, 2026-11-23: same recipes as the intro module)
_text_cell = Style.create(s.container.layouts.vertical_center_layout + Style("text-align:left;", "txt_left"),
                          "vc_paradigm_text_cell")

_NOTES = [
    ("The message",
     "The kitchen metaphor that runs through the whole course starts here. Traditional software engineering: you "
     "are the cook. VibeCoding: you become the customer who orders and tastes."),
    ("The idea explained",
     "The customer judges the dish by its taste, not by the recipe. In the same way, the vibe coder judges the "
     "program by what it does on screen; the implementation stays behind the kitchen door."),
    ("Keep the metaphor alive",
     "It comes back later: the kitchen gets inspected (the dangers), the chef designs the menu (VibeEngineering), "
     "a tasting menu (iterations)."),
    ("Ask the room",
     "« When you eat at a restaurant, what can you NOT check from your table? »"),
]

_NOTES_STAYS = [
    ("The message",
     "What changes: you no longer write every line, you express intent. What stays: you are still responsible "
     "for the result."),
    ("The idea explained",
     "The customer can send the dish back; the developer cannot send the bug back to the model. Users, clients "
     "and auditors deal with the person who delivered the software."),
    ("The trap",
     "Responsibility without control is the core problem of naive VibeCoding: you answer for code you never read."),
    ("Ask the room",
     "« If your vibe-coded app leaks customer data, who is accountable? »"),
]

_PROMPT = (
    f"{_PREFIX} Split composition: left side shows a figure cooking at a stove, "
    "hands busy, surrounded by ingredients in teal tones. Right side shows a figure "
    "seated at an elegant restaurant table, a beautifully plated dish arriving, "
    "in electric blue and amber tones. A bold geometric arrow connects left to right. "
    f"Symbolizes the shift from doing the work to delegating it. {_SUFFIX}"
)

def build():
    # Sub-slide 1: From Cook to Customer
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "From Cook to Customer", tag=t.div, toc_lvl="1")
                st_space("v", "3vh")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — From Cook to Customer", entries=_NOTES,
                                 position="left", width="50vw")

        with st_grid(cols="1.5fr 3.5fr", gap="3vw",
                     cell_styles=[s.project.containers.grid_cell_centered, _text_cell]) as g:
            with g.cell():
                st_image(
                    s.none,
                    width="80%",
                    editable=IS_EDITABLE,
                    name="vc_paradigm",
                    prompt=_PROMPT,
                    provider="openai",
                    ai_size="1024x1536",
                )

            with g.cell(), st_zoom(110):
                st_write(
                    bs.body,
                    (bs.keyword, "Traditional SE: "),
                    "You are the cook \u2014 you choose ingredients, "
                    "follow the recipe, control every step.",
                )
                st_space("v", "3vh")
                st_write(
                    bs.body,
                    (bs.keyword_accent, "VibeCoding: "),
                    "You become the customer \u2014 you describe what you want, "
                    "the kitchen prepares it, you taste the result.",
                )
                st_space("v", "3vh")
                st_write(
                    bs.body+s.project.colors.muted,
                    "The implementation stays behind the kitchen door.",
                )
    st_space("v", "20vh")
    st_slide_break()

    # Sub-slide 2: What Changes, What Stays — alternating rows, motif L2 + fonds f1 (NG, 2026-11-23)
    with st_block(s.project.containers.page_fill_top):
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.subheading, "What Changes, What Stays", tag=t.div, toc_lvl="2")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — What Changes, What Stays", entries=_NOTES_STAYS,
                                 position="left", width="50vw")
        st_space("v", "6vh")
        rows = [
            ("Changes:", bs.keyword, "you stop writing every line.<br>You express intent."),
            ("Stays:", bs.keyword_accent, "you\u2019re still responsible for the result."),
        ]
        cols = "5% 28% 62% 5%"
        cells = s.project.containers.rows(len(rows), cols, filled=(2, 3))
        with st_zoom(125), st_grid(cols=cols, gap="3vh 0.5vw", cell_styles=cells) as g:
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
        with st_zoom(115):
            st_write(
                bs.emphasis,
                "You order the dish — but you're the one who serves it to your guests.",
            )
        st_space("v", "20vh")
