"""Slide — Post-lunch re-orientation checklist."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_ask_opencode, st_hover_tooltip


class BlockStyles:
    """Post-lunch re-orientation checklist — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "tasks_reorient_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "tasks_reorient_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "tasks_reorient_foot")
    number = s.bold + s.project.colors.highlight
bs = BlockStyles

_STEP_ZOOM = 88    # tuned by measure: content bottom <= 1000 px at 1920x1080
_PROMPT_ZOOM = 70   # the « Or ask opencode » line: smaller than the step it replaces


_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. The four re-orientation checks now, 5 min; wait for all hands up "
     "before moving on."),
    ("The message",
     "Four checks, five minutes, before anyone types a prompt after lunch: the repository, the tests, the app, "
     "the plan."),
    ("Why in this order",
     "A clean status on mywork first (nothing half done), then the Part 1 tests still green, then the app still "
     "renders, and only then the next task read from @docs/plan.md."),
    ("The trap",
     "Starting the next task on top of a red test or a dirty tree: every later failure becomes ambiguous."),
    ("If a check fails",
     "Not fixed in 5 minutes? The next slide restarts from the tag j2-part1."),
    ("Ask the room",
     "« Hands up when all four checks pass. » — wait for the room before moving on."),
    ("Or ask opencode",
     "Under check 4 only: checks 1-3 come before opencode starts. Once it runs (build agent), it can redo the git "
     "and test checks and name the next task. npm run dev stays in a terminal: it keeps running."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — cd ~/ai4se/calcapp",
     "cd = change directory: the terminal now works in your project folder (~ = your home folder). Those who "
     "restarted this morning use ~/ai4se/calcapp-restart instead."),
    ("Command — git status",
     "Read-only: changes nothing. Shows the branch you are on (« On branch mywork ») and what changed since the "
     "last commit: « Changes not staged » (modified, not yet added), « Changes to be committed » (added with git "
     "add), « Untracked files » (new files git does not follow yet). « nothing to commit, working tree clean » = "
     "everything is saved in a commit."),
    ("Command — npm run test:run",
     "Runs all the tests once with Vitest (script « vitest run » of package.json) and gives the prompt back; "
     "green = all pass, red = at least one fails. npm test would stay in watch mode in your terminal (q quits)."),
    ("Command — npm run dev",
     "Runs the « dev » script of package.json = vite: starts a development web server and prints its address, "
     "http://localhost:5173/ — open it in the browser. It reloads the page at every save and keeps the terminal "
     "busy until Ctrl+C stops it: run it in a second terminal tab, or stop it before typing other commands."),
    ("Command — opencode, then @docs/plan.md",
     "Type opencode in the project folder (not in the terminal busy with npm run dev). In its input box, "
     "@docs/plan.md adds the plan to the context; ask which task is marked [next] (T1 is [done] if you moved the labels "
     "after merging it)."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Re-orientation (5 min)', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Re-orientation", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")

        # One numbered row per check, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23); under check 4 (opencode
        # runs from there), the same checks asked to opencode — build agent (NG, 2026-11-25)
        items = [
            (('Go to your project and run ', (bs.cmd, 'cd ~/ai4se/calcapp && git status'), '. It must say that you are '
              'on the branch mywork and that there is nothing to commit.'), None),
            (('Run ', (bs.cmd, 'npm run test:run'), '. The tests of Part 1 must still pass.'), None),
            (('Run ', (bs.cmd, 'npm run dev'), ' and open the address it prints. The app must show in the browser.'), None),
            (('Start opencode and ask: ', (bs.cmd, '“Read @docs/plan.md: which task is marked [next]?”')),
             "Give me the commands to check that git status is clean on mywork and that the tests pass, then run "
             "them, and tell me which task of @docs/plan.md is marked [next]."),
        ]
        cols = "5% 5% 85% 5%"
        for i, (parts, prompt) in enumerate(items):
            if i:
                st_space("v", "1.6vh")
            cells = s.project.containers.rows(i + 1, cols, filled=(2, 3))[-4:]  # keeps the alternation
            with st_zoom(_STEP_ZOOM), st_grid(cols=cols, gap="0 0.5vw", cell_styles=cells) as g:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body + bs.number, f"{i + 1}", tag=t.div)
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
            if prompt:
                st_space("v", "0.4vh")
                st_ask_opencode(prompt, zoom=_PROMPT_ZOOM, cols="5% 90% 5%")
        st_space("v", "3vh")
        with st_zoom(110):
            st_write(bs.foot, 'One check fails and you cannot fix it in 5 minutes? Next slide.', tag=t.div)
