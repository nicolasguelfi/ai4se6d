"""Slide — Exercise sheet — task 1 of your own plan, part 2/2 (REFACTOR, mutant, merge, plan labels)."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_ask_opencode, st_hover_tooltip


class BlockStyles:
    """Exercise sheet — task 1 of your own plan, part 2/2 — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "build_ex_steps2_body")
    label = s.project.titles.label
    keyword = s.bold + s.project.colors.highlight
    number = s.bold + s.project.colors.highlight
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent
                       + Style("white-space: nowrap;", "build_ex_steps2_cmd_nowrap"), "build_ex_steps2_cmd")
    timer = Style.create(s.project.titles.stat + s.center_txt, "build_ex_steps2_timer")
bs = BlockStyles

_STEP_ZOOM = 70    # tuned by measure: content bottom <= 1000 px at 1920x1080
_PROMPT_ZOOM = 64   # the « Or ask opencode » line: smaller than the step it replaces

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine, same exercise (11:45 → 12:10), steps 4 to 7: once GREEN is committed, "
     "they refactor, prove the test with a mutant, merge into mywork and move the plan labels."),
    ("REFACTOR (step 4)",
     "Third prompt of the « Three Prompts per Task » slide: same behaviour, better structure, the test is not "
     "touched; npm run test:run stays green, then commit refactor: … . Nothing to improve is a valid result: no "
     "commit, go on."),
    ("Mutant check (step 5)",
     "Break the code on purpose (e.g. remove the check on the amount): a test must go red. Then undo the "
     "sabotage (git restore on the file) and the tests are green again."),
    ("Why move the labels",
     "After lunch the first prompt asks the agent which task is marked [next]. If T1 is still [next], it answers "
     "T1. Moving the labels keeps docs/plan.md true: [done] = merged into mywork, [next] = the one to build now."),
    ("Command — git switch mywork",
     "Moves you onto the existing branch mywork (your main line since this morning): the files in the folder "
     "become mywork's version. Git refuses if uncommitted changes would be lost: commit first (git status shows "
     "them)."),
    ("Command — git merge feat/expense-type",
     "Brings the commits of your T1 branch (here feat/expense-type) into the branch you are on (mywork). If mywork "
     "has not moved meanwhile, git just moves it forward (« Fast-forward »). Otherwise it creates a merge commit "
     "and may open a text editor for its message: save and close it (nano: Ctrl+O, Enter, Ctrl+X; vim: Esc then "
     ":wq). « CONFLICT » = both branches changed the same lines: raise your hand."),
    ("Or ask opencode",
     "Under steps 4, 6 and 7, the same thing asked to opencode (build agent): it gives the commands first, then "
     "runs them and shows the result. Accept if it asks permission. Git specialists can skip these lines."),
    ("Symbol — →",
     "Only means « then » on the slide: type the two commands one after the other, not the arrow."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Exercise — Task 1 of YOUR Plan (2/2)', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Exercise — Task 1 of YOUR Plan (2/2)", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(90):
            st_write(bs.timer, '11:45 → 12:10 · 25 min', tag=t.div)
            st_write(bs.body, (bs.label, 'Then: '), 'improve the code, check that the test really catches a bug, '
                     'and add T1 to ', (bs.cmd, 'mywork'), '.', tag=t.div)
        st_space("v", "1vh")
        # One numbered row per step, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23); under a step with a
        # terminal command, full width, the same thing as a prompt for opencode — build agent (NG, 2026-11-25)
        steps = [
            (('Paste the REFACTOR prompt. Run ', (bs.cmd, 'npm run test:run'), ': the tests must still pass. Commit '
              'with a message that starts with ', (bs.cmd, 'refactor:'), '. Nothing to improve? No commit, go on.'),
             "Give me the commands to run the tests, then commit the code as 'refactor: …' if green; run them."),
            (('Mutant check: break the code on purpose; a test must fail. Then undo your change.',), None),
            (('Go back to your main line and bring T1 into it: ', (bs.cmd, 'git switch mywork'), ', then ',
              (bs.cmd, 'git merge feat/expense-type'), ' (your name may differ: use the line below).'),
             "Give me the git commands to go back to mywork and merge T1's branch into it, then run them."),
            (('In ', (bs.cmd, 'docs/plan.md'), ', change the label of T1 to ', (bs.keyword, '[done]'), ' and the '
              'label of T2 to ', (bs.keyword, '[next]'), '. Commit with the message ', (bs.cmd, 'docs: T1 done'), '.'),
             "In docs/plan.md, mark T1 [done] and T2 [next], then commit it as 'docs: T1 done'."),
        ]
        cols = "5% 5% 85% 5%"
        for i, (parts, prompt) in enumerate(steps):
            if i:
                st_space("v", "1vh")
            cells = s.project.containers.rows(i + 1, cols, filled=(2, 3))[-4:]  # keeps the alternation
            with st_zoom(_STEP_ZOOM), st_grid(cols=cols, gap="0 0.5vw", cell_styles=cells) as g:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body + bs.number, f"{i + 4}", tag=t.div)
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
            if prompt:
                st_space("v", "0.4vh")
                st_ask_opencode(prompt, zoom=_PROMPT_ZOOM, cols="5% 90% 5%")
