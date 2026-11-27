"""Slide — Day 3 agenda: four concepts this morning, GSE-One this afternoon (edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Day 3 agenda styles."""
    heading = s.project.titles.heading
    hdr = Style.create(s.project.titles.table_header + s.center_txt, "today_concepts_th")
    lbl = Style.create(s.project.titles.table_label + s.center_txt, "today_concepts_tl")
    txt = s.project.titles.table_cell
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "today_concepts_foot")
    body = s.project.titles.body
bs = BlockStyles

# First thing of day 3 (kit hd05-day3-am.md, ss2-ul-gse 20e237e; NG « ok », 2026-11-27)
_START = """\
~/ai4se/ai4se-kit/tutor update   # it prints a fix: line for GSE-One? run that line
~/ai4se/ai4se-kit/tutor          # in a second terminal: your tutor window"""

_NOTES = [
    ("Trainer action",
     "Learners type the two lines first, before the theory: the tutor gets today's notes and GSE-One moves to the "
     "course version."),
    ("Why a fix: line",
     "On day 1 everyone cloned GSE-One v0.93.4 into ~/ai4se/gensem. The course now uses v0.93.5 (it fixes the "
     "cleanup at /gse:deliver). setup-learner.sh never moves an existing clone, so tutor update checks the version "
     "and prints a fix: line (rm -rf …/gensem && sh …/setup-learner.sh) with the right path, even for a learner who "
     "chose another course folder. Copy and run that line as printed."),
    ("No fix: line?",
     "GSE-One is already the course version: nothing to do, go on to the tutor window."),
    ("Command — ~/ai4se/ai4se-kit/tutor update",
     "Downloads the latest course kit (notes, sheets) with git pull, then checks GSE-One."),
    ("Command — ~/ai4se/ai4se-kit/tutor",
     "Opens the tutor window: opencode in read-only mode on the course kit. Keep it open in its own terminal all "
     "day."),
]

ROWS = [
    ("09:15", "CCSET09", "Software engineering concepts — defining your GenSEM"),
    ("10:15", "CCSET10", "Requirements elicitation"),
    ("11:15", "CCSET11", "Non-functional requirements"),
    ("12:00", "CCSET12", "Verification and validation"),
    ("13:30", "Exercises", "With GSE-One on your CalcApp: discover, plan, requirements and design"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(75):
                st_write(bs.heading, "Day 3 — From Concepts to Method", tag=t.div, toc_lvl="1", label="Day 3 agenda")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Day 3", entries=_NOTES, position="left", width="50vw")
        with st_zoom(75):
            st_write(bs.body, "First: update the tutor; if it prints a fix: line for GSE-One, run that line. Then "
                     "open your tutor window in a second terminal.", tag=t.div)
            with st_zoom(150):  # readable from the back of the room; tuned by measure
                st_code(s.none, code=_START, language="bash", line_numbers=False, font_size="26pt")
            st_space("v", "1vh")
            with st_grid(cols="14% 20% 62%", gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell(): st_write(bs.hdr, "Time")
                with g.cell(): st_write(bs.hdr, "Cycle")
                with g.cell(): st_write(bs.hdr, "Topic")
            for time, cycle, topic in ROWS:
                with st_grid(cols="14% 20% 62%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.lbl, time)
                    with g.cell(): st_write(bs.lbl, cycle)
                    with g.cell(): st_write(bs.txt, topic)
            st_write(bs.foot, "This morning: theory, and how GSE-One solves each problem. "
                     "This afternoon: you use GSE-One for the first time.", tag=t.div)
