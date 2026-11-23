"""Slide — If you did not finish Part 2."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """If you did not finish Part 2 — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "tasks_notfinished_body")
    keyword = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "tasks_notfinished_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "tasks_notfinished_foot")
bs = BlockStyles


_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Only those behind near 14:20: merge what is green, catch up from "
     "a tag if the app is broken, so that npm test and npm run dev work for 14:30."),
    ("The message",
     "Not finishing Part 2 is fine: the review section at 14:30 works on whatever code the participant has."),
    ("What to do",
     "Merge what is green; leave a red branch aside. If the app is broken, catch up with j2-part1 — or take "
     "j2-v0.1 to review the reference code."),
    ("The minimum before 14:30",
     "npm run test:run and npm run dev must work: the review needs running code."),
    ("The tone",
     "Being behind on code must never block the learning — say it explicitly to the participants who are "
     "behind."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(65):
                st_write(bs.heading, 'If You Did Not Finish', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — If You Did Not Finish", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")

        # One row per point, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        items = [
            ('v0.1 need not be complete to be reviewed: you review ', (bs.keyword, 'what you have')),
            ('Merge what is green; leave a red branch aside',),
            ('App broken? Catch up with ', (bs.cmd, 'j2-part1'), ', or ', (bs.cmd, 'j2-v0.1'),
             ' to review the reference code'),
            ('Then ', (bs.cmd, 'npm run test:run'), ' and ', (bs.cmd, 'npm run dev'), ' must work'),
        ]
        cols = "5% 90% 5%"
        cells = s.project.containers.rows(len(items), cols, filled=(2,))
        with st_zoom(100), st_grid(cols=cols, gap="4vh 0.5vw", cell_styles=cells) as g:
            for parts in items:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "5vh")
        with st_zoom(105):
            st_write(
                bs.foot,
                'Being behind on code must never block the learning: 14:30 is about review.',
                tag=t.div,
            )
