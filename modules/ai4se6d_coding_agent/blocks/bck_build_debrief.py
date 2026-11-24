"""Slide — Debrief — Part 1."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Debrief — Part 1 — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "build_debrief_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "build_debrief_cmd")
    timer = Style.create(s.project.titles.stat + s.center_txt, "build_debrief_timer")
    number = s.bold + s.project.colors.highlight
bs = BlockStyles


_NOTES = [
    ("Trainer action",
     "Learners do it — they answer aloud. Debrief 12:10 → 12:15: two questions to the room, then "
     "neighbours compare their git log --oneline."),
    ("The message",
     "Five minutes to turn the morning's practice into two observations, before lunch: did the AI-TDD discipline "
     "hold, and did the tests really test something?"),
    ("Question 1 — « test only »",
     "The RED prompt asks the agent for a test only. Collect the cases where it also wrote the code, and what "
     "the participant did: refuse, undo, re-prompt."),
    ("Question 2 — the mutant check",
     "Break the implementation on purpose: if no test fails, the test proves nothing. Ask who found such a test."),
    ("Why compare git logs",
     "The log shows the rhythm of the loop: a test: commit, then a feat: commit, per task. A neighbour's log "
     "makes a missing step visible at a glance."),
    ("Link to the afternoon",
     "Part 2 runs the same loop on routing, data and UI, then the review section at 14:30."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — git log --oneline",
     "Lists the commits of the branch you are on. --oneline = one line per commit: short id (7 characters, e.g. "
     "a1b2c3d) then the message. Newest at the TOP: « test: before feat: » in time means the feat: line is ABOVE "
     "the test: line. Long list? Space scrolls, q quits."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Debrief — Part 1 (5 min)', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Debrief, Part 1", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(120):
            st_write(bs.timer, '12:10 → 12:15', tag=t.div)
        st_space("v", "3vh")

        # One numbered row per question, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        items = [
            'Did the agent respect “test only”? If not, what did you do?',
            'Did your mutant check reveal a test that proved nothing?',
        ]
        cols = "5% 5% 85% 5%"
        cells = s.project.containers.rows(len(items), cols, filled=(2, 3))
        with st_zoom(131), st_grid(cols=cols, gap="4vh 0.5vw", cell_styles=cells) as g:
            for n, text in enumerate(items, 1):
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body + bs.number, f"{n}", tag=t.div)
                with g.cell():
                    st_write(bs.body, text, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "5vh")
        with st_zoom(131), st_block(s.project.containers.callout):
            st_write(
                bs.body,
                'Compare with your neighbour: show each other your ',
                (bs.cmd, 'git log --oneline'),
                '.',
            )
