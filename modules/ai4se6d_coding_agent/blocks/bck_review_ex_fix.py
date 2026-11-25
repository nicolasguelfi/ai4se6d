"""Slide — Fix one finding, test first."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_ask_opencode, st_hover_tooltip


class BlockStyles:
    """Fix one finding, test first — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "review_ex_fix_body")
    keyword = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "review_ex_fix_cmd")
bs = BlockStyles

_CODE_ZOOM = 100  # code readable in the room; tuned by measure so the slide fills one screen (NG, 2026-11-24)

# Text left-aligned (NG, 2026-11-23: same recipes as the intro module)
_left = Style("text-align:left;", "review_ex_fix_left")

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Step 4 of the review exercise: on fix/review, back to the build "
     "agent, they fix one finding test first."),
    ("The message",
     "A review finding is fixed like any task this morning: a failing test first (RED), then the fix (GREEN)."),
    ("Why test first",
     "The test proves the finding was real and stays fixed. Without it, « fixed » is only the agent's word."),
    ("Build agent, fix branch",
     "Shift+Tab back to the build agent (the plan agent does not edit your files), on the fix/review branch. "
     "« Change nothing else » keeps the diff small and readable."),
    ("Close the loop",
     "Read the diff, run npm run test:run, commit « fix: RVW-1 … », and mark RVW-1 as fixed in docs/review.md."),
    ("Ask the room",
     "« The agent's fix also touched another file. Do you keep it? »"),
    ("Or ask opencode",
     "Under the list, the test-then-commit step asked to opencode (build agent, already active). Reading the diff "
     "stays yours: that is the point of the slide."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Key — Shift+Tab (in opencode)",
     "Switches the primary agent: build (edits files, runs commands) ↔ plan (explores and proposes; by default it"
     " asks before any file edit or shell command, so it does not change your project). Tab does the same in the "
     "other direction; with two agents both just toggle. The current agent's name is shown under the input box."),
    ("Prompt — fix RVW-1",
     "« Fix RVW-1 from docs/review.md » = which finding (the agent reads it in that file). « First write a "
     "failing test that exposes it and run npm run test:run (RED) » = prove the problem. « then fix the code "
     "(GREEN) ». « Change nothing else » = keep the diff small."),
    ("Command — read the diff",
     "git diff (no argument) shows the uncommitted changes the agent made; git diff --stat lists only the files "
     "touched. q quits."),
    ("Command — npm run test:run",
     "Runs all the tests once with Vitest (script « vitest run » of package.json) and gives the prompt back; "
     "green = all pass, red = at least one fails. npm test would stay in watch mode in your terminal (q quits)."),
    ("Command — commit fix: RVW-1 …",
     "git add -A then git commit -m \"fix: RVW-1 corrupt JSON no longer crashes\": fix: = a correction, then the "
     "finding's number and a short description."),
]

_FIX = """\
Fix RVW-1 from docs/review.md. First write a failing test that exposes
it and run npm run test:run (RED), then fix the code (GREEN).
Change nothing else."""


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Fix One Finding — Test First', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Fix One Finding — Test First", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(108), st_block(_left):
            st_write(
                bs.body,
                'Shift+Tab back to the ',
                (bs.keyword, 'build'),
                ' agent, on branch ',
                (bs.cmd, 'fix/review'),
                ':',
                tag=t.div,
            )
            with st_zoom(_CODE_ZOOM):
                st_code(s.none, code=_FIX, language='text', line_numbers=False, font_size="36pt")
            st_space("v", "2vh")
            with st_list(list_type=lt.unordered, l_style=bs.body, li_style=bs.body,
                         text_align="left", item_gap=0.6) as l:
                with l.item():
                    st_write(bs.body, 'Read the diff: did it touch anything else?')
                with l.item():
                    st_write(bs.body, (bs.cmd, 'npm run test:run'), ' green → commit ', (bs.cmd, 'fix: RVW-1 …'))
                with l.item():
                    st_write(bs.body, 'In ', (bs.cmd, 'docs/review.md'), ': RVW-1 → ', (bs.keyword, 'fixed'))
            st_space("v", "0.2vh")  # the test-then-commit step asked to opencode — build agent (NG, 2026-11-25)
            st_ask_opencode("Give me the commands to run the tests, then commit as 'fix: RVW-1 …' if green; run "
                            "them.", zoom=70, cols="0% 100% 0%")
