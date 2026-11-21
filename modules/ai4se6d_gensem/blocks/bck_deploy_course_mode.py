"""Slide — How we deploy in this course: the operating mode of exercise E19 (CCSET16, edition 2).

Learner path rehearsed on the course server on 2026-11-21 (GSE-One v0.91.0, Coolify, Learner role).
No server name, domain or token here: the course file `.env.training` carries them.
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from exercise_sheet import _parts  # backticks → monospace, as in the sheets


class BlockStyles:
    """Course deployment set-up styles."""
    heading = s.project.titles.heading
    hdr = Style.create(s.project.titles.table_header + s.center_txt, "course_mode_th")
    lbl = Style.create(s.project.titles.table_label + s.center_txt, "course_mode_tl")
    txt = s.project.titles.table_cell
    warn = Style.create(s.project.titles.body + s.bold + s.project.colors.highlight + s.center_txt, "course_mode_warn")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "course_mode_foot")
bs = BlockStyles

ROWS = [
    ("Your repository", "Your own CalcApp repository becomes `origin`; push `main` — the server builds what is on GitHub"),
    ("Your identifier", "`l` + your number in the tracking sheet (e.g. `l07`) → `calcapp-l07.<course domain>`"),
    ("The course file", "`.env.training` from the trainer → `.env` in CalcApp; ignored by git, never committed"),
    ("The command", "`/gse-deploy`, role Learner: checks, build, start, HTTPS, health check (1-3 min)"),
    ("Your logs", "`/gse-deploy --logs` (last 100 lines; `--lines 300` for more)"),
    ("The waves", "5 learners at the deployment table: 11:00 · 11:40 · 13:15 · 14:00"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(62):
            st_write(bs.heading, "How We Deploy in This Course", tag=t.div, toc_lvl="+1",
                     label="Course deployment set-up")
            with st_grid(cols="22% 74%", gap="6px", cell_styles=s.project.containers.table_header_cell) as g:
                with g.cell(): st_write(bs.hdr, "Step")
                with g.cell(): st_write(bs.hdr, "What you do")
            for name, what in ROWS:
                with st_grid(cols="22% 74%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.lbl, name)
                    with g.cell(): st_write(bs.txt, *_parts(what))
            with st_block(s.project.containers.callout):
                st_write(bs.warn, "The course token reaches every app on the server: deploy only your own. "
                         "It is revoked, and every app removed, after the course.", tag=t.div)
            st_write(bs.foot, "Exercise E19 — the sheet follows.", tag=t.div)
