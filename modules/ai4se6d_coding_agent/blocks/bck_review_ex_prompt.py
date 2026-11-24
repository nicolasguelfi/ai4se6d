"""Slide — The review prompt for the plan agent."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """The review prompt — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "review_ex_prompt_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "review_ex_prompt_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "review_ex_prompt_foot")
bs = BlockStyles

# Text left-aligned (NG, 2026-11-23: same recipes as the intro module)
_left = Style("text-align:left;", "review_ex_prompt_left")

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Step 2 of the review exercise: they paste !git diff j2-start, "
     "then the review prompt, in the plan agent."),
    ("The message",
     "Two steps: put the diff into the conversation, then ask for a structured review of it against the plan."),
    ("The « ! » prefix",
     "In opencode, ! runs a shell command and puts its output into the conversation: !git diff j2-start gives "
     "the agent exactly what changed today, nothing more."),
    ("What the prompt asks",
     "A review against @docs/plan.md, focused on bugs and runtime errors, missing error handling, user input "
     "reaching storage unvalidated, tests that prove nothing. Each finding: RVW-n, HIGH/MEDIUM/LOW, file, why it "
     "matters, suggested fix. « Edit nothing »: the review only reports."),
    ("The trap",
     "A diff too long for one review. Then review one task at a time, e.g. !git diff j2-start -- src/utils/."),
    ("Ask the room",
     "« Why review against docs/plan.md and not only the code? »"),
]

_DIFF = """\
!git diff j2-start"""

_REVIEW = """\
Review this diff of CalcApp v0.1 against @docs/plan.md. Focus: bugs and
runtime errors, missing error handling, user input reaching storage
unvalidated, tests that prove nothing. For each finding: RVW-n,
HIGH/MEDIUM/LOW, file, why it matters, suggested fix. Edit nothing."""


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'The Review Prompt', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — The Review Prompt", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(105), st_block(_left):
            st_write(
                bs.body,
                'First, put the diff into the conversation — ',
                (bs.cmd, '!'),
                ' runs a shell command:',
                tag=t.div,
            )
            st_code(s.none, code=_DIFF, language='text', line_numbers=False, font_size="36pt")
            st_space("v", "4vh")
            st_write(bs.body, 'Then:', tag=t.div)
            st_code(s.none, code=_REVIEW, language='text', line_numbers=False, font_size="36pt")
            st_space("v", "4vh")
            st_write(
                bs.foot,
                'Diff too long? One task at a time: !git diff j2-start -- src/utils/',
                tag=t.div,
            )
