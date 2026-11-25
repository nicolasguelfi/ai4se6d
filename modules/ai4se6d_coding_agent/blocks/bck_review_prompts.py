"""Slide — Weak vs effective review prompts."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Weak vs effective review prompts — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "review_prompts_body")
    label = s.project.titles.label
    keyword = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "review_prompts_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "review_prompts_foot")
bs = BlockStyles

_CODE_ZOOM = 98  # code readable in the room; tuned by measure so the slide fills one screen (NG, 2026-11-24)

# Text left-aligned (NG, 2026-11-23: same recipes as the intro module)
_left = Style("text-align:left;", "review_prompts_left")

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Show the weak vs effective prompts; learners run a review prompt"
     " with the plan agent in the 15:15 exercise."),
    ("The message",
     "« Review this code. » gives vague, generic findings. An effective review prompt names one file, one "
     "concern and the context the agent cannot guess."),
    ("Why the plan agent",
     "Shift+Tab switches to the plan agent, which does not edit your project files: the review reports findings and edits nothing. "
     "You decide later what gets fixed."),
    ("The two examples",
     "The first targets user input in AddExpense (empty, negative, huge amounts). The second targets storage: "
     "corrupt JSON or a full localStorage, with each finding classified HIGH / MEDIUM / LOW."),
    ("Link to the rest of the afternoon",
     "The severity scale is the one of the next slide, and the one you use in the review exercise at 15:15."),
    ("Ask the room",
     "« What context does the agent need that is not in the file itself? »"),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Key — Shift+Tab (in opencode)",
     "Switches the primary agent: build (edits files, runs commands) ↔ plan (reads and proposes; it"
     " cannot edit your project files). Tab does the same in the "
     "other direction; with two agents both just toggle. The current agent's name is shown under the input box."),
    ("Symbol — @docs/plan.md (in opencode)",
     "@ followed by a path adds that file to the agent's context: the agent reads its content with your message. "
     "Typing @ opens a fuzzy file search; Enter or Tab picks the file. The path is relative to the project folder"
     " (docs/plan.md = file plan.md in folder docs)."),
    ("Prompt — effective 1 (AddExpense)",
     "@src/pages/AddExpense.tsx = the one file to review. « Review edge cases and error handling » = the one "
     "concern. « The input comes from a user form: empty, negative, huge amounts? » = the context and the cases "
     "to try, which the agent cannot guess."),
    ("Prompt — effective 2 (storage)",
     "@src/storage.ts = the file. « corrupt JSON » = the stored text is not valid JSON (the data format "
     "localStorage holds), so JSON.parse throws an error. « full » = localStorage is limited (about 5 MB per "
     "site), setItem then throws. « Classify each finding HIGH / MEDIUM / LOW » = the triage scale of the next "
     "slide."),
]

_GOOD1 = """\
@src/pages/AddExpense.tsx Review edge cases and error handling.
The input comes from a user form: empty, negative, huge amounts?"""

_GOOD2 = """\
@src/storage.ts What happens if localStorage holds corrupt JSON
or is full? Classify each finding HIGH / MEDIUM / LOW."""


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Weak vs Effective Prompts', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Weak vs Effective Prompts", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(103), st_block(_left):
            st_write(bs.body, (bs.label, 'Weak: '), (bs.cmd, 'Review this code.'), tag=t.div)
            st_space("v", "5vh")
            st_write(
                bs.body,
                (bs.label, 'Effective: '),
                (bs.keyword, 'plan'),
                ' agent (Shift+Tab — no file edits), one file, one concern, the context:',
                tag=t.div,
            )
            with st_zoom(_CODE_ZOOM):
                st_code(s.none, code=_GOOD1, language='text', line_numbers=False, font_size="36pt")
            with st_zoom(_CODE_ZOOM):
                st_code(s.none, code=_GOOD2, language='text', line_numbers=False, font_size="36pt")
            st_space("v", "5vh")
            st_write(
                bs.foot,
                'Name the file, the concern, the context: specific prompt, actionable findings.',
                tag=t.div,
            )
