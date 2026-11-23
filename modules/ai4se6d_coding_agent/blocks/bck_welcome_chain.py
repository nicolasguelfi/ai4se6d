"""Slide — The artifact chain: each session produces what the next one uses."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Artifact chain styles."""
    heading = s.project.titles.heading
    number = Style.create(s.project.titles.table_label + s.project.colors.highlight, "chain_number")
    step = s.project.titles.table_label
    artifact = s.project.titles.table_cell
    closing = Style.create(s.project.titles.body_accent + s.center_txt, "chain_closing")
bs = BlockStyles

_CHAIN = [
    ("1", "Git", "a safety net: commit, branch, restore"),
    ("2", "opencode", "AGENTS.md + the right context"),
    ("3", "Plan", "docs/plan.md, 5-8 atomic tasks"),
    ("4", "Build", "tests then code, one branch per task"),
    ("5", "Review", "findings triaged HIGH / MEDIUM / LOW"),
    ("6", "Deliver", "v0.1 merged and tagged"),
]

_NOTES = [
    ("The message",
     "Each session of the day produces an artifact that the next session uses. Nothing is thrown away."),
    ("The chain",
     "Git gives the safety net; opencode gets AGENTS.md and the right context; the plan lists 5-8 atomic tasks in "
     "docs/plan.md; the build writes tests then code, one branch per task; the review triages findings HIGH / "
     "MEDIUM / LOW; the delivery merges and tags v0.1."),
    ("The trap",
     "Skipping a link: without the plan the build has no tasks, without tests the review has nothing to check "
     "against, without Git nothing can be restored."),
    ("Link to GSE-One",
     "Git, opencode, plan, build and review each have a « GSE-One solution » slide; the bridge at 16:30 connects the chain to GSE-One."),
    ("Ask the room",
     "« Which artifact did you NOT have yesterday? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(70):
                st_write(bs.heading, "The Artifact Chain", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — The Artifact Chain", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")

        # one numbered row per step, alternating fills — motif L2 + fonds f1 (margins 5 %, numbering column)
        cols = "5% 5% 22% 63% 5%"
        cells = s.project.containers.rows(len(_CHAIN), cols, filled=(2, 3, 4))
        with st_zoom(110), st_grid(cols=cols, gap="2.2vh 0.4vw", cell_styles=cells) as g:
            for num, step, artifact in _CHAIN:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.number, num, tag=t.div)
                with g.cell():
                    st_write(bs.step, step, tag=t.div)
                with g.cell():
                    st_write(bs.artifact, artifact, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "4vh")
        with st_zoom(110):
            st_write(bs.closing, "Each step feeds the next. By 17:00: a tested, reviewed, versioned app.", tag=t.div)
