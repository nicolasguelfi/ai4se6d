"""Slide — Post-lunch re-orientation checklist."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Post-lunch re-orientation checklist — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "tasks_reorient_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "tasks_reorient_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "tasks_reorient_foot")
    number = s.bold + s.project.colors.highlight
bs = BlockStyles


_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. The four re-orientation checks now, 5 min; wait for all hands up "
     "before moving on."),
    ("The message",
     "Four checks, five minutes, before anyone types a prompt after lunch: the repository, the tests, the app, "
     "the plan."),
    ("Why in this order",
     "A clean status on mywork first (nothing half done), then the Part 1 tests still green, then the app still "
     "renders, and only then the next task read from @docs/plan.md."),
    ("The trap",
     "Starting the next task on top of a red test or a dirty tree: every later failure becomes ambiguous."),
    ("If a check fails",
     "Not fixed in 5 minutes? The next slide restarts from the tag j2-part1."),
    ("Ask the room",
     "« Hands up when all four checks pass. » — wait for the room before moving on."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(65):
                st_write(bs.heading, 'Re-orientation (5 min)', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Re-orientation", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")

        # One numbered row per check, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        items = [
            ((bs.cmd, 'cd ~/ai4se/calcapp'), ' → ', (bs.cmd, 'git status'), ': clean, on ', (bs.cmd, 'mywork')),
            ((bs.cmd, 'npm run test:run'), ' → Part 1 tests still green'),
            ((bs.cmd, 'npm run dev'), ' → the app renders in the browser'),
            ('Start opencode, read ', (bs.cmd, '@docs/plan.md'), ': which task is next?'),
        ]
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(items), cols, filled=(2, 3))
        with st_zoom(100), st_grid(cols=cols, gap="4vh 0.5vw", cell_styles=cells) as g:
            for n, parts in enumerate(items, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body + bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "5vh")
        with st_zoom(110):
            st_write(bs.foot, 'One check fails and you cannot fix it in 5 minutes? Next slide.', tag=t.div)
