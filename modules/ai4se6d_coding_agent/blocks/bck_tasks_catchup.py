"""Slide — Catch-up — restart from tag j2-part1."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Catch-up — restart from tag j2-part1 — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "tasks_catchup_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "tasks_catchup_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "tasks_catchup_foot")
bs = BlockStyles

_CODE_ZOOM = 95  # code readable in the room; tuned by measure so the slide fills one screen (NG, 2026-11-24)


_CATCHUP = """\
git clone https://github.com/nicolasguelfi/calcapp-starter ~/ai4se/calcapp-restart
cd ~/ai4se/calcapp-restart && git checkout -b mywork j2-part1 && npm ci"""

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Only those who failed a re-orientation check: they restart from "
     "the tag j2-part1 now."),
    ("The message",
     "For whoever failed a re-orientation check: restart from the tag j2-part1, the end of Part 1 (first "
     "features, tests green)."),
    ("What the commands do",
     "Clone the starter into a new folder (calcapp-restart), create mywork from j2-part1, install the exact "
     "dependencies with npm ci. The old folder stays as it was."),
    ("What to carry over",
     "docs/plan.md and AGENTS.md from ~/ai4se/calcapp — the participant's own plan and rules — then skip the "
     "tasks the tag already contains."),
    ("The tone",
     "A recovery tag is a safety net, not a failure: the goal of the afternoon is the loop and the review, "
     "not finishing at all costs."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Catch-up: Tag j2-part1', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Catch-up: Tag j2-part1", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(115):
            st_write(bs.body, 'Restart from the end of Part 1 (first features, tests green):', tag=t.div)
            st_space("v", "3vh")
            with st_zoom(_CODE_ZOOM):
                st_code(s.none, code=_CATCHUP, language="bash", line_numbers=False, font_size="26pt")   # one line per command at this zoom
            st_space("v", "3vh")
            with st_list(list_type=lt.unordered, l_style=bs.body, li_style=bs.body,
                         text_align="left", item_gap=0.6) as l:
                with l.item():
                    st_write(
                        bs.body,
                        'Copy back ',
                        (bs.cmd, 'docs/plan.md'),
                        ' and ',
                        (bs.cmd, 'AGENTS.md'),
                        ' from ',
                        (bs.cmd, '~/ai4se/calcapp'),
                    )
                with l.item():
                    st_write(bs.body, 'Skip the tasks already done in the tag, continue with the next one')
            st_space("v", "3vh")
            st_write(bs.foot, 'A recovery tag is a safety net, not a failure.', tag=t.div)
