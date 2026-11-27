"""Slide — Preview of Day 3."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Preview of Day 3 — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "bridge_tomorrow_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "bridge_tomorrow_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "bridge_tomorrow_foot")
bs = BlockStyles

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Preview of day 3; ask who has a setup problem tonight, not "
     "tomorrow."),
    ("The message",
     "Tomorrow (Day 3, Thursday 3 December), GSE-One drives the loop you ran by hand today."),
    ("How it starts",
     "/gse-go inside your project. CalcApp continues; if your project is lost or broken, the recovery tag "
     "p3-start gives everyone the same starting point."),
    ("New habit",
     "Your work goes to GitHub, pushed before each break and every evening."),
    ("Before leaving",
     "Keep the laptop as it is: opencode, the model key, GSE-One v0.93.5 and your tutor are all needed "
     "tomorrow morning."),
    ("Ask the room",
     "« Is anyone's setup not working right now? Tell us tonight, not tomorrow morning. »"),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — /gse-go (GSE-One, day 3)",
     "The entry point, typed in opencode's input box inside the project folder: it reads the project's state "
     "(.gse/ folder) and proposes the next activity. --adopt = take over an existing project not created with "
     "GSE-One (the case of CalcApp); --status = show the state only."),
    ("Tag — p3-start",
     "Recovery tag of the starter for day 3 (p = part): same clone + git checkout -b mywork p3-start + npm ci as "
     "today."),
]

_ITEMS = [
    ('GSE-One drives the loop you ran by hand today',),
    ('Start with ', (bs.cmd, '/gse-go'), ' inside your project'),
    ('CalcApp continues — recovery tag ', (bs.cmd, 'p3-start')),
    ('Your work goes to GitHub, pushed before each break and every evening',),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Next: Day 3 (Thu 3 Dec)', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Next: Day 3", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")

        # one row per item, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "5% 90% 5%"
        cells = s.project.containers.rows(len(_ITEMS), cols, filled=(2,))
        with st_zoom(127), st_grid(cols=cols, gap="4.5vh 0.5vw", cell_styles=cells) as g:
            for parts in _ITEMS:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "5vh")
        with st_zoom(127):
            st_write(
                bs.foot,
                'Keep your laptop as it is: opencode, model key, GSE-One v0.93.5, your tutor.',
                tag=t.div,
            )
