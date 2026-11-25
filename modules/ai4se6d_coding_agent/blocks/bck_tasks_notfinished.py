"""Slide — If you did not finish Part 2."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_ask_opencode, st_hover_tooltip


class BlockStyles:
    """If you did not finish Part 2 — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "tasks_notfinished_body")
    keyword = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "tasks_notfinished_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "tasks_notfinished_foot")
bs = BlockStyles

_STEP_ZOOM = 88    # tuned by measure: content bottom <= 1000 px at 1920x1080
_PROMPT_ZOOM = 76   # the « Or ask opencode » line: smaller than the step it replaces


_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. Only those behind near 14:20: merge what is green, catch up from "
     "a tag if the app is broken, so that npm run test:run and npm run dev work for 14:30."),
    ("The message",
     "Not finishing Part 2 is fine: the review section at 14:30 works on whatever code the participant has."),
    ("What to do",
     "Merge what is green; leave a red branch aside. If the app is broken, catch up with j2-part1 — or take "
     "j2-v0.1 to review the reference code."),
    ("The minimum before 14:30",
     "npm run test:run and npm run dev must work: the review needs running code."),
    ("The tone",
     "Being behind on code must never block the learning — say it explicitly to the participants who are "
     "behind."),
    ("Or ask opencode",
     "Under « merge what is green » and the test check (build agent). No prompt for the catch-up tags: they start "
     "from a new clone. npm run dev stays in a terminal: it keeps running."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — merge what is green",
     "On a branch whose tests pass: git switch mywork then git merge (branch). A red branch stays as it is: "
     "nothing is lost, you can come back to it with git switch (branch)."),
    ("Tag — j2-part1 / j2-v0.1",
     "A tag is a fixed label on one commit — here a checkpoint of the course: j2-start (start of day 2), j2-part1"
     " (end of Part 1), j2-v0.1 (v0.1 reference). Same commands as the catch-up slide, with the tag name changed:"
     " git checkout -b mywork j2-v0.1 gives the reference v0.1 code to review."),
    ("Command — npm run test:run",
     "Runs all the tests once with Vitest (script « vitest run » of package.json) and gives the prompt back; "
     "green = all pass, red = at least one fails. npm test would stay in watch mode in your terminal (q quits)."),
    ("Command — npm run dev",
     "Runs the « dev » script of package.json = vite: starts a development web server and prints its address, "
     "http://localhost:5173/ — open it in the browser. It reloads the page at every save and keeps the terminal "
     "busy until Ctrl+C stops it: run it in a second terminal tab, or stop it before typing other commands."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'If You Did Not Finish', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — If You Did Not Finish", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")

        # One row per point, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23); under a point with a command,
        # the same thing asked to opencode — build agent (NG, 2026-11-25)
        items = [
            (('v0.1 need not be complete to be reviewed: you review ', (bs.keyword, 'what you have')), None),
            (('Merge the branches whose tests pass; leave aside a branch whose tests fail.',),
             "Give me the git commands to merge into mywork only my task branches whose tests pass, then run them."),
            (('Your app is broken? Restart from the tag ', (bs.cmd, 'j2-part1'), ' (Catch-up slide), or from ',
              (bs.cmd, 'j2-v0.1'), ' to review the reference code.'), None),
            (('Then ', (bs.cmd, 'npm run test:run'), ' and ', (bs.cmd, 'npm run dev'), ' must both work.'),
             "Give me the command to run the tests, then run it."),
        ]
        cols = "5% 90% 5%"
        for i, (parts, prompt) in enumerate(items):
            if i:
                st_space("v", "1.4vh")
            cells = s.project.containers.rows(i + 1, cols, filled=(2,))[-3:]  # keeps the alternation
            with st_zoom(_STEP_ZOOM), st_grid(cols=cols, gap="0 0.5vw", cell_styles=cells) as g:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
            if prompt:
                st_space("v", "0.4vh")
                st_ask_opencode(prompt, zoom=_PROMPT_ZOOM, cols="5% 90% 5%")
        st_space("v", "3vh")
        with st_zoom(109):
            st_write(
                bs.foot,
                'Being behind on code must never block the learning: 14:30 is about review.',
                tag=t.div,
            )
