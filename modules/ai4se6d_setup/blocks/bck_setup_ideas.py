"""Slide — Three ideas to get started (or bring your own)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Ideas slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    name = Style.create(s.project.titles.body_accent, "setup_idea_name_left")
    text = Style.create(s.project.titles.body, "setup_idea_text_left")
    body = Style.create(s.project.titles.body + s.center_txt, "setup_idea_body")
    keyword = s.bold + s.project.colors.highlight
    caption = Style.create(s.project.titles.caption + s.center_txt, "setup_idea_caption")
bs = BlockStyles

_IDEAS = [
    ("Recipe Finder", "type ingredients → get matching recipes"),
    ("Habit Tracker", "daily checklist with streaks"),
    ("Movie Watchlist", "browse, save and rate movies"),
]

_NOTES = [
    ("The message",
     "Three ready-made ideas so nobody loses time choosing: Recipe Finder, Habit Tracker, Movie Watchlist. "
     "Each has a suggested first prompt on the next slide."),
    ("Your own idea",
     "Welcome — as long as it stays small and personal: one screen, one thing it does well."),
    ("The rule to repeat",
     "Use made-up data only: no real personal or company data goes into a prompt (it leaves your machine)."),
    ("Why small",
     "45 minutes for v1, a client's feature and a presentation (v1 + 1 commit at 14:45). A small app reaches "
     "« done » and leaves time to iterate."),
    ("Ask the room",
     "« Hands up: who takes one of the three, who brings their own? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Three Ideas", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Three Ideas", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "4vh")

        # One row per idea, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "5% 32% 58% 5%"
        cells = s.project.containers.rows(len(_IDEAS), cols, filled=(2, 3))
        with st_zoom(100):
            with st_grid(cols=cols, gap="8vh 0.5vw", cell_styles=cells) as g:
                for name, text in _IDEAS:
                    with g.cell():
                        pass  # left margin
                    with g.cell():
                        st_write(bs.name, name, tag=t.div)
                    with g.cell():
                        st_write(bs.text, text, tag=t.div)
                    with g.cell():
                        pass  # right margin
            st_space("v", "7vh")
            st_write(bs.body, (bs.keyword, "Your own idea?"), " Go for it — keep it small and personal.", tag=t.div)
            st_space("v", "2vh")
            st_write(bs.caption, "Use made-up data: no real personal or company data.", tag=t.div)
