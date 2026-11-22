"""Slide — « Predicting the next word »: « The mouse loves the … », the last word reads the words before it.

Copied from streamtex-all-trainings content/atoms/bck_deep_learning_attention_mouse_prediction.py (planche
attention1, NG 2026-11-12), right after the « mouse » video (NG, 2026-11-22). The context point of « the » lands near
« cheese »; closeness gives the probabilities (bars), the halo stands for the temperature. Layout and player in
blocks/_attention_videos.py.
"""
# @guideline: maximize-viewport
from blocks._attention_videos import header, slide, video


class BlockStyles:
    """Title and player styles in blocks/_attention_videos.py (shared by the two mouse videos)."""
bs = BlockStyles


_NOTES = [
    ("How to run it",
     "26 seconds. « the » reads the words before it; the thickness of the golden lines is the share of attention it "
     "gives each one (mostly « mouse » and « loves »). Its context point, the golden dot, lands near « cheese »: the "
     "most probable word."),
    ("The bars",
     "Closeness gives the probabilities: cheese 82%, seeds 11%… The model DRAWS the word according to them: « seeds » "
     "remains possible. The dotted halo stands for the temperature: the higher it is, the more the distant candidates "
     "get their chance."),
    ("Why « the »",
     "An article has almost no meaning on its own; yet its position in context predicts what follows. The whole "
     "meaning of the sentence flows into it through attention."),
    ("What is really computed",
     "In a real model, the last word's vector is compared with the whole vocabulary (tens of thousands of words) by a "
     "dot product, then the softmax function turns the scores into probabilities. Distance in a three-dimensional "
     "space is a picture of that comparison."),
]


def build():
    with slide():
        header("Predicting the next word", "How « cheese » is found", _NOTES)
        video("attention-mouse-prediction-en.mp4", max_vh=85)
