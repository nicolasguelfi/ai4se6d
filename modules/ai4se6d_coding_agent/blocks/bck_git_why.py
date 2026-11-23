"""Slide — Why Git matters more with AI tools."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Why-Git styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    number = Style.create(s.project.titles.body + s.bold + s.project.colors.highlight, "gitwhy_number")
    closing = Style.create(s.project.titles.body_accent + s.center_txt, "gitwhy_closing")
bs = BlockStyles

_ITEMS = [
    ((bs.keyword, "Fast, broad changes"), " — the agent edits 10 files in seconds; Git shows which"),
    ((bs.keyword, "You review"), " — the agent proposes, ", (bs.keyword, "git diff"), " is how you check"),
    ((bs.keyword, "Cheap experiments"), " — try on a branch, delete it if it fails"),
]

_NOTES = [
    ("The message",
     "With an agent, Git is not optional: it is how you see, check and undo what the agent did."),
    ("Fast, broad changes",
     "The agent can edit ten files in seconds. Without Git you do not even know which files changed."),
    ("You review",
     "The agent proposes; git diff shows the exact lines, and that is your review."),
    ("Cheap experiments",
     "A branch costs nothing: try an idea there, delete it if it fails, main is untouched."),
    ("The trap",
     "Relying on the agent's own undo: opencode's /undo relies on Git — no repository, no undo."),
    ("Ask the room",
     "« After the agent worked yesterday, how did you know what it had changed? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(70):
                st_write(bs.heading, "Why Git Matters More with AI", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Why Git Matters More with AI", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "5vh")

        # one numbered row per reason, alternating fills — motif L2 + fonds f1 (margins 5 %, numbering column)
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(_ITEMS), cols, filled=(2, 3))
        with st_zoom(100), st_grid(cols=cols, gap="5vh 0.5vw", cell_styles=cells) as g:
            for n, item in enumerate(_ITEMS, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.body, *item, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "7vh")
        with st_zoom(100):
            st_write(bs.closing, "Even opencode’s /undo relies on Git: no repo, no undo.", tag=t.div)
