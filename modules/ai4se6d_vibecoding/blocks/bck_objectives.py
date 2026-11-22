"""Slide — Learning objectives for the VibeCoding & VibeEngineering session."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

class BlockStyles:
    """Learning objectives slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    verb = s.bold + s.project.colors.accent
    number = s.bold + s.project.colors.highlight
bs = BlockStyles

_NOTES = [
    ("The message",
     "Four objectives for this part, in the order of the session: define, identify the dangers, distinguish, "
     "learn the principles."),
    ("Define",
     "VibeCoding: what the term means (Karpathy, 2025) and its four principles — intent over implementation, "
     "trust in output, conversational iteration, low barrier to entry."),
    ("Identify",
     "The dangers of naive AI-assisted development, with figures: vulnerabilities, hallucinated packages, "
     "technical debt, productivity paradoxes, trust."),
    ("Distinguish and learn",
     "VibeEngineering keeps the speed of AI but adds engineering discipline: six principles, from requirements "
     "before prompts to context engineering."),
    ("Ask the room",
     "« Which of the four do you expect to be the hardest? »"),
]

def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Learning Objectives", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Learning Objectives", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "4vh")

        # One numbered row per objective, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23):
        # outer margins 5 %, a numbering column, the objective.
        items = [
            ("Define", " VibeCoding and its core principles"),
            ("Identify", " key dangers and limitations of naive AI-assisted development"),
            ("Distinguish", " VibeCoding from VibeEngineering"),
            ("Learn", " the VibeEngineering principles to structure AI-assisted work"),
        ]
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(items), cols, filled=(2, 3))
        with st_zoom(105), st_grid(cols=cols, gap="4vh 0.5vw", cell_styles=cells) as g:
            for n, (verb, text) in enumerate(items, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body + bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.body, (bs.verb, verb), text, tag=t.div)
                with g.cell():
                    pass  # right margin
