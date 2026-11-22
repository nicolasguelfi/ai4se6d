"""Slide — « One word, several meanings »: the attention video on « mouse » (silent, or narrated with sound).

Copied from streamtex-all-trainings content/atoms/bck_deep_learning_attention_mouse.py (planche attention1, NG
2026-11-12/14), inserted after « Attention in Action » (NG, 2026-11-22). « mouse » changes neighbours as the sentence
grows: ambiguous, then computing with « desk », then animal with « cheese ». Under the video, two buttons play a
narrated version with sound (Simple, Advanced: no Intermediate in English); clicking the chosen button again brings
back the silent video. Layout and player in blocks/_attention_videos.py.
"""
# @guideline: maximize-viewport
import streamlit as st
from streamtex import *
from custom.styles import Styles as s
from blocks._attention_videos import header, slide, video


class BlockStyles:
    """Title and player styles in blocks/_attention_videos.py (shared by the two mouse videos)."""
bs = BlockStyles


_NOTES = [
    ("The narrated versions",
     "Under the video, two buttons play a narrated version, with sound: Simple, Advanced. Clicking the chosen button "
     "again brings back the silent video, to comment it yourself."),
    ("How to run it",
     "50 seconds. Let it play once in silence, then again while commenting: each time a word is added, « mouse » is "
     "read again by the last word. Ambiguous at first (animal or computer), it slides towards computing with « desk », "
     "then swings back to the animal with « cheese » (in slow motion)."),
    ("What moves",
     "The hollow circle is « mouse » as it was when it arrived: it no longer changes (in ChatGPT, the key-value cache "
     "keeps it as is). The solid dot is « mouse » as READ by the last word: this reading changes with every word, and "
     "it is what serves to predict what comes next."),
    ("The prediction",
     "Before « cheese », the prediction: « phone » comes first (47%) and « cheese » is at the very bottom (1%). It "
     "comes anyway, ticked ✓: a text does not always take the most probable word."),
    ("The lines",
     "A line joins the word to each concept that pulls it; its thickness is the strength of the pull. The dotted path "
     "keeps the past readings: the same word, changing meaning."),
    ("The trap",
     "The concepts (animal, keyboard…) are teaching labels, and the space has three dimensions instead of thousands: "
     "the video shows the principle, not the real positions inside a model."),
    ("And an encoder (BERT)?",
     "A bidirectional encoder rereads the whole sentence: there, the position of « mouse » itself moves."),
]

# (key, button label, narrated video)
_LEVELS = [
    ("simple", "Simple", "attention-mouse-narrated-simple-en.mp4"),
    ("advanced", "Advanced", "attention-mouse-narrated-advanced-en.mp4"),
]
_KEY = "attention-mouse-level"


def build():
    with slide():
        header("One word, several meanings", "Attention moves the meaning", _NOTES)
        chosen = st.session_state.get(_KEY)
        narrated = next((v for k, _, v in _LEVELS if k == chosen), None)
        if narrated:
            video(narrated, max_vh=70, muted=False)   # the click lets the browser play the sound
        else:
            video("attention-mouse-en.mp4", max_vh=70)
        with st_zoom(160), st_grid(cols="1fr auto 1fr", cell_styles=s.project.containers.grid_cell_centered) as g:
            with g.cell():
                pass
            with g.cell():
                st.segmented_control("Narrated version", [k for k, _, _ in _LEVELS],
                                     format_func=lambda k: next(lab for kk, lab, _ in _LEVELS if kk == k),
                                     key=_KEY, label_visibility="collapsed")
            with g.cell():
                pass
