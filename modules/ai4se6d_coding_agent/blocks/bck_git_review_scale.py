"""Slide — Too big to read every line? Reading every line does not scale; how the check grows with the change (NG, 2026-11-24).

Placed at the end of the Git section: today's tasks are small, so learners read the whole diff, but the course says
upfront how the check changes when an agent changes hundreds or thousands of files.
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Review-at-scale styles."""
    heading = s.project.titles.heading
    pitch = Style.create(s.project.titles.body_accent + s.center_txt, "revscale_pitch")
    th = s.project.titles.table_header
    td = s.project.titles.table_cell
    tl = s.project.titles.table_label
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "revscale_cmd")
    note = Style.create(s.project.titles.caption + s.center_txt, "revscale_note")
bs = BlockStyles

_TABLE_ZOOM = 88    # tuned by measure: content bottom <= 1000 px at 1920x1080

# (size of the change, how you check it, where in the course)
_ROWS = [
    ("A few lines, one task", ("read the whole ", (bs.cmd, "git diff")), "Today, CalcApp tasks"),
    # full sentences, one check each (NG « ok », 2026-11-27)
    ("Tens of files", ("See which files changed and how much (", (bs.cmd, "git diff --stat"), "): is that what the "
                       "task asked? Run the tests: all must pass. Check that the agent did not edit the tests to make "
                       "them pass. Read the risky parts line by line."), "Day 2 — tasks with tests (11:30)"),
    ("Hundreds of files", ("AI review against the plan, triage HIGH / MEDIUM / LOW, read and fix the HIGH ones",),
     "Day 2 — review (14:30)"),
    ("Thousands of files", ("Automatic checks run on every change: tests (", (bs.cmd, "npm run test:run"), "), lint (",
                            (bs.cmd, "npm run lint"), "), type check (", (bs.cmd, "npm run build"), "). Several agents "
                            "review the change. You review the plan, the tests and the risky parts."),
     "Days 3-6 — GSE-One"),
]

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Say it clearly: today you read everything because the tasks are small; "
     "that is training, not the rule for real projects."),
    ("The message",
     "You never stop being responsible for what the agent wrote. What changes with the size of the change is how you "
     "check it: reading, then scope + tests, then AI review, then automatic checks and several reviewers."),
    ("Why not read everything",
     "A coding agent can change thousands of files in minutes: nobody reads that line by line, and a tired reader "
     "misses bugs anyway. Reading is kept for what is small or risky."),
    ("Risky parts — what to read even in a big change",
     "Security (authentication, secrets, input that reaches storage or a query), data (formats, migrations, "
     "deletion), money and business rules, configuration and dependencies (package.json, lock file, CI), and any "
     "change to the tests themselves."),
    ("Prevention — keep changes reviewable",
     "One small task per prompt, one branch per task (the plan of 11:00). A rule in AGENTS.md can ask the agent to "
     "stop and ask when a task needs more than a few files."),
    ("Words",
     "Scope = which files and how many lines changed. Triage = sort the problems by severity. Lint = a tool that "
     "flags suspicious or badly written code without running it (npm run lint, ESLint). Type check = TypeScript "
     "reads all the code without running it and flags a value of the wrong kind, e.g. text where amount: number is "
     "expected, or a field that does not exist (npm run build runs tsc first). Tests run the code; lint and type "
     "check do not, so they also cover lines no test reaches. N-version review = several agents "
     "review the same change independently."),
    ("Tests untouched — when",
     "On day 2 the test: commit (red) adds the test on purpose. The check is for the next step: between the test "
     "commit and the feat commit, the test files must not change. An agent that edits or deletes a test to get "
     "green proves nothing (git diff --stat shows a .test.ts file in the list)."),
    ("Command — git diff --stat",
     "One line per changed file with the number of lines added (+) and removed (-), then a total; no content. "
     "--stat = statistics only. The first thing to read on any change, big or small."),
    ("Ask the room",
     "« The agent changed 300 files for a 1-line request. What do you do before reading a single line? » "
     "(stop: the scope is wrong — undo with git restore, make the task smaller)."),
]


def render(rows, title, foot):
    """One half of the table: the slide title, the pitch, the rows, a foot line (shared by both halves)."""
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, title, tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Too Big to Read Every Line?", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(105):
            st_write(bs.pitch, "You own every change — how you check it grows with its size.", tag=t.div)
        st_space("v", "3vh")

        # Header row, then one row per size, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "2% 22% 50% 24% 2%"
        base = s.project.containers.row_cell_left
        hc = s.project.containers.table_header_cell
        head = [base, hc, hc, hc, base]
        cells = head + s.project.containers.rows(len(rows), cols, filled=(2, 3, 4))
        with st_zoom(_TABLE_ZOOM), st_grid(cols=cols, gap="1.5vh 0.5vw", cell_styles=cells) as g:
            for h in ("", "The change", "How you check it", "In this course", ""):
                with g.cell():
                    if h:
                        st_write(bs.th, h)
            for size, how, when in rows:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.tl, size)
                with g.cell():
                    st_write(bs.td, *how)
                with g.cell():
                    st_write(bs.td, when)
                with g.cell():
                    pass  # right margin
        st_space("v", "3vh")
        with st_zoom(105):
            st_write(bs.note, foot, tag=t.div)


# Split in two after the rows became full sentences (NG « ok », 2026-11-27): small changes here, large ones in
# bck_git_review_scale_large.
def build():
    render(_ROWS[:2], "Too Big to Read Every Line? (1/2)",
           "Today the tasks are small: you read every line. The next slide: when the change grows.")
