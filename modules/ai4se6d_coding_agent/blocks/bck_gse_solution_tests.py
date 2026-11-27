"""Slide — CCSET07: how GSE-One handles tests (concept only, edition 2)."""
# @guideline: minimalist-visual + maximize-viewport
from gse_solution import gse_solution, CMD


class BlockStyles:
    """Layout and styles come from the shared gse_solution component."""
bs = BlockStyles


_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Concept only (CCSET07): learners use /gse-tests and /gse-produce"
     " from day 3."),
    ("The message",
     "An agent can write code that looks right, and tests that prove nothing. GSE-One makes tests a step with "
     "its own evidence."),
    ("Strategy first",
     "/gse-tests sets a test strategy from the requirements before any code: which levels, which cases, one "
     "acceptance (validation) test per Given/When/Then criterion."),
    ("Production",
     "/gse-produce builds each code task on its own branch as in the demo: the acceptance test first, run and "
     "seen failing, committed; then the code until it passes. Every test run is saved as a campaign report (TCP-NNN) in "
     "docs/sprints/sprint-NN/test-reports/, and the task's test_evidence in backlog.yaml points to it (status, "
     "date, pass rate, coverage). That is the evidence /gse-deliver checks (GSE-One v0.93.5, spec §6.3)."),
    ("Word — worktree",
     "A second working folder of the same git repository, checked out on another branch: GSE-One gives each task "
     "its own folder (.worktrees/sprint-NN-type-name) on its own branch gse/sprint-NN/type/name, so two tasks never "
     "mix their files. Default setting git.strategy: worktree in .gse/config.yaml; branch-only = a branch without "
     "a separate folder; none = no branch (GSE-One v0.93.5)."),
    ("Delivery is blocked",
     "While a requirement's tests have not been run and passed, delivery is blocked."),
    ("Ask the room",
     "« In the demo, what proved that the task was done? »"),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Symbol — /gse-… commands",
     "Typed in opencode's input box, not in the terminal: a message starting with / runs a command; the GSE-One "
     "plugin adds the /gse-… ones (typing / shows the list). Each accepts --help for its options."),
    ("Command — /gse-tests (GSE-One, day 3)",
     "Without argument: shows the test status and proposes the next step. --strategy defines the test strategy "
     "(levels: unit, integration, end-to-end; one acceptance test per Given/When/Then criterion), --run runs the "
     "suite, --evidence packages the results."),
    ("Command — /gse-produce (GSE-One, day 3)",
     "Runs the next task of the sprint: creates its branch (by default also a separate working folder, a git "
     "worktree), writes the acceptance test, shows it failing, commits it, then writes the code until it passes. "
     "--task TASK-ID picks a task; --dry-run only shows what it would do."),
]


def build():
    gse_solution(
        cycle="CCSET07 · Testing with AI",
        label="GSE-One solution — tests",
        problem="An agent can write code that looks right, and tests that prove nothing.",
        solution=[
            ((CMD, "/gse-tests"), " sets a test strategy from the requirements before any code: "
             "which levels, which acceptance tests."),
            ((CMD, "/gse-produce"), ", for each code task: the acceptance test first, seen failing, then the code — "
             "each task on its own branch and in its own folder (worktree); every test run is saved as a report in ",
             (CMD, "docs/sprints/…/test-reports/"), "."),
            "Delivery is blocked while a requirement's tests have not been run and passed.",
        ],
        notes=_NOTES,
        zoom=88,   # fills the slide (default 60 left the lower half empty) — NG, 2026-11-23
    )
