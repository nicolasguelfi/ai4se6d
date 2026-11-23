"""Slide — Optimal review size — 200 to 400 lines."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Optimal review size — 200 to 400 lines — styles."""
    heading = s.project.titles.heading
    body_center = Style.create(s.project.titles.body + s.center_txt, "review_size_body_c")
    stat = Style.create(s.Giant + s.bold + s.project.colors.highlight + s.center_txt, "review_size_stat")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "review_size_foot")
    source = s.project.citation + s.large + s.center_txt
bs = BlockStyles


_STAT = """\
git diff j2-start --stat    # how many lines did you change today?"""

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. One command only: git diff j2-start --stat, to see how many lines"
     " they changed today; then you comment on the 200-400 rule."),
    ("The message",
     "A review has a useful size: 200 to 400 lines at a time, and no more than 60 minutes per session — beyond "
     "that, defect detection drops."),
    ("The source",
     "SmartBear guidance from the Cisco MeetingPlace case study of lightweight review (Jason Cohen, « Best Kept "
     "Secrets of Peer Code Review », 2006)."),
    ("Why it matters with an agent",
     "An agent writes 1,000 lines in a session: reviewing a whole day at once is beyond the limit. Review per "
     "task — which is exactly what one branch per task allows."),
    ("Try it",
     "git diff j2-start --stat shows how many lines each participant changed today."),
    ("Ask the room",
     "« How many lines did you change today? How many did you actually read? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(65):
                st_write(bs.heading, 'How Much per Review?', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — How Much per Review?", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(104):
            st_space("v", "2vh")
            st_write(bs.stat, '200–400 lines', tag=t.div)
            st_space("v", "2vh")
            st_write(
                bs.body_center,
                'per review — beyond that, defect detection drops. And no more than 60 minutes per session.',
                tag=t.div,
            )
            st_write(bs.source, cite('cohen2006-peer-review'), tag=t.div)
            st_space("v", "3vh")
            st_code(s.none, code=_STAT, language='bash', line_numbers=False, font_size="36pt")
            st_space("v", "3vh")
            st_write(
                bs.foot,
                'An agent writes 1,000 lines in a session: review per task, not per day.',
                tag=t.div,
            )
