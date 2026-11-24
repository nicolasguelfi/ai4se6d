"""Slide — AI review output is input to your judgment — accept, defer, refuse."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """AI review output is input to your judgment — accept, defer, refuse — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "review_judgment_body")
    keyword = s.bold + s.project.colors.highlight
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "review_judgment_foot")
bs = BlockStyles

_CODE_ZOOM = 99  # code readable in the room; tuned by measure so the slide fills one screen (NG, 2026-11-24)

# Text left-aligned (NG, 2026-11-23: same recipes as the intro module)
_left = Style("text-align:left;", "review_judgment_left")

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Read the three example decisions; learners must refuse one "
     "finding with a written reason in the 15:15 exercise."),
    ("The message",
     "The AI review output is input to your judgment, not a verdict. Each finding ends in one of three "
     "decisions: fix, defer, or refuse — with a written reason."),
    ("Read the example",
     "RVW-1 (HIGH, corrupt JSON crashes the app) and RVW-2 (MEDIUM, negative amount accepted) are fixed. "
     "RVW-3 (LOW, rename amount → amountEur) is refused: v0.1 has one currency, as docs/plan.md says."),
    ("Why write the refusal",
     "A written refusal is a decision, not laziness: someone else can review it, and the agent will not "
     "propose the same change again blindly."),
    ("Link to the exercise",
     "In the review exercise you must refuse at least one finding, with a written reason in docs/review.md."),
    ("Ask the room",
     "« Which finding would you refuse in your own code, and what is the reason? »"),
]

_TRIAGE = """\
RVW-1 [HIGH]   storage.ts: corrupt JSON crashes the app → FIX
RVW-2 [MEDIUM] AddExpense: negative amount accepted     → FIX
RVW-3 [LOW]    rename amount → amountEur          → REFUSED
               reason: v0.1 has one currency (docs/plan.md)"""


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'You Are the Judge', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — You Are the Judge", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "4vh")
        with st_zoom(115), st_block(_left):
            st_write(
                bs.body,
                'For each finding: ',
                (bs.keyword, 'fix'),
                ', ',
                (bs.keyword, 'defer'),
                ', or ',
                (bs.keyword, 'refuse — with a written reason'),
                '.',
                tag=t.div,
            )
            st_space("v", "6vh")
            with st_zoom(_CODE_ZOOM):
                st_code(s.none, code=_TRIAGE, language='markdown', line_numbers=False, font_size="36pt")
            st_space("v", "8vh")
            st_write(
                bs.foot,
                'A written refusal is a decision, not laziness — and someone else can review it.',
                tag=t.div,
            )
