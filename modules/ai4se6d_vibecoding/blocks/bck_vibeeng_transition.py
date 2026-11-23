"""Slide — Transition: What Practices Remain Essential?"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Transition slide styles."""
    question = Style.create(
        s.Giant + s.bold + s.center_txt + s.project.colors.accent,
        "vibeeng_transition_question",
    )
    affirmation = Style.create(
        s.Giant + s.bold + s.center_txt + s.project.colors.primary,
        "vibeeng_transition_affirmation",
    )
    subtitle = Style.create(
        s.Large + s.italic + s.project.colors.muted + s.center_txt,
        "ve_trans_subtitle",
    )
bs = BlockStyles

_NOTES_Q = [
    ("The message", "After the dangers of naive VibeCoding: which software-engineering practices must survive when an "
                    "AI writes the code?"),
    ("Run it", "Let the room answer before the next slide: requirements, tests, design, review, version control… "
               "Write their answers down; the six principles will match most of them."),
    ("The idea", "AI changes who types the code, not what makes software reliable."),
    ("Ask the room", "« Name one practice you would keep even if the AI wrote 100% of your code. »"),
]

_NOTES_A = [
    ("The message", "The practices the room just listed are exactly what VibeEngineering keeps: the speed of AI, with "
                    "the discipline of engineering."),
    ("The metaphor", "What separates the home cook from the starred chef: not the oven, but the menu, the recipes, the "
                     "tasting at every step and the responsibility for every plate."),
    ("Next", "From Coding to Engineering, then the six principles (P1 to P6)."),
    ("Ask the room", "« Which of your answers would a starred chef call a recipe, which a check? »"),
]

def build():
    # Two slides, each in its own st_slide box (NG, 2026-11-23), as in streamtex-all-trainings:
    # the box fills the screen and centres its content; the second slide gets its break and its listed marker.
    # the stops sit on the slide boxes (marker=), the headings only attach their TOC entry to them:
    # the arrows show each whole slide, not the heading scrolled to the top (NG, 2026-11-23)
    with st_slide(marker="What Practices Remain Essential?"):
        _question_slide()
    with st_slide(cut=True, marker="Exactly \u2014 That\u2019s VibeEngineering"):
        _affirmation_slide()


def _question_slide():
    with st_block(s.center_txt):
        # question and « i » on the same line, one line (NG, 2026-11-23)
        with st_grid(cols="95% 5%", gap="0px", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(60):
                st_write(
                    bs.question,
                    "What Practices Remain Essential?",
                    tag=t.div,
                    toc_lvl="1",
                    marker="attach",
                )
            with h.cell():
                st_hover_tooltip(title="Trainer notes — What Practices Remain Essential?", entries=_NOTES_Q,
                                 position="left", width="50vw")


def _affirmation_slide():
    with st_block(s.center_txt):
        with st_grid(cols="95% 5%", gap="0px", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(60):   # one line (NG, 2026-11-23)
                st_write(
                    bs.affirmation,
                    "Exactly \u2014 That\u2019s VibeEngineering",
                    tag=t.div,
                    toc_lvl="2",
                    marker="attach",
                )
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Exactly, that's VibeEngineering", entries=_NOTES_A,
                                 position="left", width="50vw")
        st_space("v", 2)
        with st_zoom(160):
            st_write(
                bs.subtitle,
                "What separates the home cook from the starred chef.",
            )
