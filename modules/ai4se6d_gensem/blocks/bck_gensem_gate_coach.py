"""Slide — Real case: the GSE-One coach flags rubber-stamping at the Gates (decision P13, edition 2).

Source: reference rehearsal of days 1-4 (2026-11-10), day 3. The plan, requirements, design and
preview Gates had all been accepted with the recommended option; the coach (an AI sub-agent that
watches the collaboration) then wrote the message quoted below (verbatim from the session).
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Gate coach styles."""
    heading = s.project.titles.heading
    caption = Style.create(s.project.titles.caption + s.center_txt, "gatecoach_caption")
    quote = Style.create(s.project.titles.body + s.italic, "gatecoach_quote")
    lbl = Style.create(s.project.titles.table_label + s.center_txt, "gatecoach_tl")
    txt = s.project.titles.table_cell
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "gatecoach_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "gatecoach_foot")
bs = BlockStyles

QUOTE = ("“Your coach again (medium, dismissible): you've now taken the recommended option "
         "4 times in a row — past the point where it suggests a deliberate challenge. "
         "At the next checkpoint, pick ‘Discuss’ once … One genuine pushback re-calibrates "
         "the loop — it isn't a sign anything was wrong.”")

ROWS = [
    ("Why it matters", "Four Gates passed, no decision taken: the plan, the requirements, the design and the "
                       "preview are the agent's, not yours. A Gate you always accept is not a Gate."),
    ("What to do", "At the next Gate, ask the 3 questions; then choose Discuss, or change one thing "
                   "(split, reorder or remove a task; add a requirement)."),
    ("What it gave", "In the rehearsal: the CI task back to the backlog, and a measurable non-functional "
                     "requirement added (1,000 expenses listed in under 200 ms)."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(62):
            st_write(bs.heading, "When the Coach Says “Discuss Once”", tag=t.div, toc_lvl="+1",
                     label="Real case — the coach and the Gates")
            st_write(bs.caption, "Real case — our rehearsal of this afternoon. The coach is a GSE-One sub-agent "
                     "that watches how you and the agent work together.", tag=t.div)
            with st_block(s.project.containers.callout):
                st_write(bs.quote, QUOTE, tag=t.div)
            for name, what in ROWS:
                with st_grid(cols="20% 76%", gap="6px", cell_styles=s.project.containers.table_normal_cell) as g:
                    with g.cell(): st_write(bs.lbl, name)
                    with g.cell(): st_write(bs.txt, what)
            st_write(bs.foot, "A nudge, not a block. See the counter in ", (bs.cmd, ".gse/status.yaml"), ": ",
                     (bs.cmd, "consecutive_acceptances"), " (for a beginner the coach speaks from 3; "
                     "one real pushback resets it to 0).", tag=t.div)
