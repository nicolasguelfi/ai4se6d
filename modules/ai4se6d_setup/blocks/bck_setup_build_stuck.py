"""Slide — If you get stuck while building (stays on screen during the workshop)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Build stuck slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    number = s.bold + s.project.colors.highlight
    keyword = s.bold + s.project.colors.accent
    warn = s.bold + s.project.colors.highlight
    caption = Style.create(s.project.titles.caption + s.center_txt, "setup_bstuck_caption")
bs = BlockStyles

_NOTES = [
    ("The message",
     "This slide stays on screen during the workshop: four steps, in order, when something does not work."),
    ("1 — the tutor window",
     "The right-hand terminal: participants ask it first, before anyone else."),
    ("2 and 3 — work with the agent",
     "Rephrase with a smaller, more precise request; or paste the error to the agent (« this fails with … ») — "
     "most blockers end there."),
    ("4 — raise your hand",
     "For technical blockers (installation, key, network), not for app design questions."),
    ("The tone",
     "« Do not worry about code quality today. There is no “right way” — just build. » Quality comes on day 2."),
]

_STEPS = [
    ("Ask ", (bs.keyword, "your tutor window"), " (right-hand terminal)"),
    ((bs.keyword, "Rephrase"), " — smaller, more precise request"),
    ((bs.keyword, "Paste the error"), " to the agent: “this fails with …”"),
    ((bs.warn, "Raise your hand"), " — technical blockers"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "If You Get Stuck", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — If You Get Stuck", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "4vh")

        # One numbered row per step, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(_STEPS), cols, filled=(2, 3))
        with st_zoom(100):
            with st_grid(cols=cols, gap="6vh 0.5vw", cell_styles=cells) as g:
                for n, parts in enumerate(_STEPS, 1):
                    with g.cell():
                        pass  # left margin
                    with g.cell():
                        st_write(bs.body + bs.number, f"{n}", tag=t.div)
                    with g.cell():
                        st_write(bs.body, *parts, tag=t.div)
                    with g.cell():
                        pass  # right margin
            st_space("v", "7vh")
            st_write(bs.caption, "Do not worry about code quality today. There is no “right way” — just build.",
                     tag=t.div)
