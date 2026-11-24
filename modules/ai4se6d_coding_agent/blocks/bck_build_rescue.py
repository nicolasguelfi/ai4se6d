"""Slide — Rescue — restart from tag j2-start."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Rescue — restart from tag j2-start — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "build_rescue_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "build_rescue_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "build_rescue_foot")
bs = BlockStyles

_CODE_ZOOM = 102  # code readable in the room; tuned by measure so the slide fills one screen (NG, 2026-11-24)

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Only those who lost 15+ min on a broken setup: they run the "
     "rescue commands now, then restart at step 1 of the exercise."),
    ("The message",
     "A participant who has lost 15 minutes or more on a broken setup stops debugging it and restarts from the "
     "course's clean start: the tag j2-start of calcapp-starter."),
    ("What the commands do",
     "Clone the starter into a NEW folder (calcapp-restart), create the branch mywork from the tag j2-start, "
     "install the exact dependencies (npm ci). The old folder is left untouched."),
    ("What to carry over",
     "Only the participant's own work: docs/plan.md and AGENTS.md, copied back from ~/ai4se/calcapp and "
     "committed, then step 1 of the exercise again."),
    ("The trap",
     "Running opencode in the old folder afterwards: from now on, everything happens in calcapp-restart."),
    ("Link to the rest of the day",
     "Same mechanism after lunch with the tag j2-part1: a recovery tag is a safety net, not a failure."),
]


_RESCUE = """\
git clone https://github.com/nicolasguelfi/calcapp-starter ~/ai4se/calcapp-restart
cd ~/ai4se/calcapp-restart && git checkout -b mywork j2-start && npm ci"""


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Lost 15+ Minutes? Rescue', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Lost 15+ Minutes? Rescue", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(116):
            st_write(bs.body, "Don't fight a broken setup: restart from the course's clean start.", tag=t.div)
            st_space("v", "3vh")
            with st_zoom(_CODE_ZOOM):
                st_code(s.none, code=_RESCUE, language="bash", line_numbers=False, font_size="26pt")   # one line per command at this zoom
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
                    st_write(bs.body, 'Commit them, then restart at step 1 of the exercise')
            st_space("v", "3vh")
            st_write(bs.foot, 'Your old work stays in ~/ai4se/calcapp. From now on, run opencode in calcapp-restart.', tag=t.div)
