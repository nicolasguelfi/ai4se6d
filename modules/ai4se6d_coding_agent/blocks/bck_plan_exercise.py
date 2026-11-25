"""Slide — Try it: write and commit docs/plan.md (steps)."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: ptn_exercise_flow
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Exercise steps styles."""
    heading = s.project.titles.heading
    timer = Style.create(s.project.titles.stat + s.center_txt, "plan_ex_timer")
    step = s.project.titles.table_cell
    keyword = s.project.titles.table_label
    number = s.bold + s.project.colors.highlight
    ask = s.project.titles.ask_label
    prompt = s.project.titles.ask_prompt
    prompt_cell = s.project.containers.ask_cell
bs = BlockStyles

_STEP_ZOOM = 98    # tuned by measure: content bottom <= 1000 px at 1920x1080
_PROMPT_ZOOM = 76   # the « Or ask opencode » line: smaller than the step it replaces

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine, 20 min. Everyone elicits with the plan agent, splits into 5-8 tasks and "
     "commits docs/plan.md on mywork; walk around."),
    ("The message",
     "20 minutes, one deliverable: docs/plan.md committed on your mywork branch."),
    ("The steps",
     "Plan agent first (elicitation prompt, answer its questions, split into 5-8 atomic tasks, tests first). "
     "Then the build agent writes the file in the slide format. You edit, mark T1 [next], stage, read the "
     "staged diff, commit."),
    ("The step not to skip",
     "Push back at least once: too big? not testable? The plan is yours, not the agent's."),
    ("Trap — plan saves outside the project",
     "Asked to save the plan (even « save it to docs/plan.md »), the plan agent writes it under ~/.opencode/plan/ "
     "in your home folder, with a name it chooses — never in the project: plan may not edit project files. Nothing "
     "to commit then. Tested on opencode 2.4.1 (2026-11-25). Fix: Shift+Tab → build, then « Write docs/plan.md in "
     "the slide format. »"),
    ("Why git diff --staged",
     "A new file is untracked: git diff ignores it. git add first, then git diff --staged shows what you commit."),
    ("Link to what follows",
     "Task 1 of this plan is the exercise of the next part: test first, on its own branch."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Or ask opencode",
     "Under steps 6 and 7, the same thing asked to opencode — the build agent, already active since step 5: it "
     "gives the git commands first, then runs them and shows the result. Accept if it asks permission. Git "
     "specialists can skip these lines."),
    ("Command — git switch mywork",
     "Moves to the existing branch mywork (your main line today): your files now show that branch. No -c here "
     "because the branch already exists. Git refuses if uncommitted changes would be overwritten: commit them "
     "first."),
    ("Command — opencode",
     "Starts opencode in the current folder: run it inside the project folder (~/ai4se/calcapp), because that "
     "folder is what the agent sees and edits. Quit with /exit or Ctrl+C."),
    ("Key — Shift+Tab",
     "In opencode, hold Shift and press Tab: it switches to the next primary agent (plan → build → plan). The "
     "active agent's name is shown near the prompt box. « Shift+Tab → plan » = press it until plan is shown."),
    ("Prompt — « Split into 5-8 atomic tasks, tests first, with acceptance criteria. »",
     "Sent to the plan agent: 5-8 small tasks, one thing each, each starting with its test, each with a checkable "
     "« done » condition."),
    ("Prompt — « Write docs/plan.md in the slide format. »",
     "Sent to the build agent (plan does not edit project files): it creates the file with the T1/T2 headings, "
     "[next]/[todo], Accept and Branch lines."),
    ("Command — git add docs/plan.md, then git diff --staged",
     "git add stages the new file; git diff --staged shows what will be committed (--staged = compare the staging "
     "area with the last commit). Plain git diff shows nothing for a new file."),
    ("Command — git commit -m \"docs: v0.1 plan\"",
     "Saves the staged plan as a commit on mywork. -m = the message in quotes; « docs: » = a documentation change."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Try It: Your docs/plan.md", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Try It: Your docs/plan.md", entries=_NOTES,
                                 position="left", width="50vw")
        st_write(bs.timer, "20 min · goal: a committed plan", tag=t.div)
        st_space("v", "1vh")
        # One numbered row per step, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23); under a step with a
        # terminal command, full width, the same thing as a prompt for opencode — build agent (NG, 2026-11-25)
        steps = [
            (((bs.keyword, "git switch mywork"), ", ", (bs.keyword, "opencode"), ", ",
              (bs.keyword, "Shift+Tab → plan")), None),
            (("Paste the elicitation prompt, answer its questions",), None),
            (("“Split into 5-8 atomic tasks, tests first, with acceptance criteria.”",), None),
            (("Push back at least once: too big? not testable?",), None),
            (((bs.keyword, "Shift+Tab → build"), ": “Write docs/plan.md in the slide format.”"), None),
            (("Edit, mark T1 ", (bs.keyword, "[next]"), ", ", (bs.keyword, "git add"), " it, ",
              (bs.keyword, "git diff --staged")),
             "Give me the git commands to stage docs/plan.md and show what will be committed, then run them."),
            (((bs.keyword, "git commit -m \"docs: v0.1 plan\""),),
             "Give me the git command to commit docs/plan.md as 'docs: v0.1 plan', then run it."),
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
                    st_write(bs.step + bs.number, f"{i + 1}", tag=t.div)
                with g.cell():
                    st_write(bs.step, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
            if prompt:
                st_space("v", "0.4vh")
                with st_zoom(_PROMPT_ZOOM), st_grid(cols="5% 90% 5%", gap="0",
                                                    cell_styles=[s.none, bs.prompt_cell, s.none]) as g:
                    with g.cell():
                        pass  # left margin
                    with g.cell():
                        st_write(bs.prompt, (bs.ask, "Or ask opencode:  "), f"“{prompt}”")
                    with g.cell():
                        pass  # right margin
