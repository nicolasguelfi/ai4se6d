"""Slide — Transition: What Practices Remain Essential?"""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s

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

def build():
    # Sub-slide 1: Question
    with st_block(s.project.containers.page_fill_center):
        st_write(
            bs.question,
            "What Practices Remain Essential?",
            tag=t.div,
            toc_lvl="1",
        )
    st_space("v", "20vh")
    st_slide_break()

    # Sub-slide 2: Affirmation
    with st_block(s.project.containers.page_fill_center):
        with st_block(s.center_txt):
            st_write(
                bs.affirmation,
                "Exactly \u2014 That\u2019s VibeEngineering",
                tag=t.div,
                toc_lvl="2",
            )
            st_space("v", 2)
            st_write(
                bs.subtitle,
                "What separates the home cook from the starred chef.",
            )
