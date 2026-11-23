"""Slide — Four Git words: repository, commit, branch, remote."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Concept rows styles."""
    heading = s.project.titles.heading
    term = s.project.titles.subtitle
    text = s.project.titles.table_cell
bs = BlockStyles

_CARDS = [
    ("Repository", "The folder Git tracks. Its hidden .git/ holds the whole history."),
    ("Commit", "A snapshot + a message + a link to its parent. Commits form your timeline."),
    ("Branch", "A parallel timeline. Like it? Merge it. Don’t? Delete it."),
    ("Remote", "A copy on a server such as GitHub, usually called origin."),
]

_NOTES = [
    ("The message",
     "Four words are enough to follow the rest of the session: repository, commit, branch, remote."),
    ("Repository and commit",
     "The repository is the tracked folder; its hidden .git/ holds the whole history. A commit is a snapshot with "
     "a message and a link to its parent — the commits form the timeline."),
    ("Branch",
     "A parallel timeline: merge it if you like the result, delete it if you do not. Today: one branch per task."),
    ("Remote",
     "A copy on a server such as GitHub, usually called origin — where v0.1 is delivered at the end of the day."),
    ("The trap",
     "Confusing a commit (local) with a push (to the remote): a commit alone is not on GitHub."),
    ("Ask the room",
     "« Which of the four did you already use yesterday without naming it? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(70):
                st_write(bs.heading, "Four Words to Know", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Four Words to Know", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "4vh")

        # one row per word, alternating fills — motif L2 + fonds f1 (margins 5 %)
        cols = "5% 25% 65% 5%"
        cells = s.project.containers.rows(len(_CARDS), cols, filled=(2, 3))
        with st_zoom(108), st_grid(cols=cols, gap="4.5vh 0.4vw", cell_styles=cells) as g:
            for term, text in _CARDS:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.term, term, tag=t.div)
                with g.cell():
                    st_write(bs.text, text, tag=t.div)
                with g.cell():
                    pass  # right margin
