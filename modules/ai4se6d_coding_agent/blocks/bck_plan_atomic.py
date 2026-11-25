"""Slide — From stories to atomic tasks (example)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Atomic tasks styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.center_txt, "atomic_body")
    keyword = s.project.titles.keyword
    story = Style.create(s.project.titles.table_cell + s.italic, "atomic_story")
    accept = s.project.titles.table_cell
    item = s.project.titles.table_cell
    check = s.bold + s.project.colors.accent
    number = s.bold + s.project.colors.highlight
bs = BlockStyles

_STORY_ZOOM = 90
_TASK_ZOOM = 95

# Two stories in user words, each with its tasks and their check (NG, 2026-11-25: the old task list was cryptic —
# no user, no need, no acceptance criterion). Tasks 1-2 keep the meaning of T1-T2 on the docs/plan.md slide.
_STORIES = [
    ("“As a user, I want to record an expense and still find it tomorrow.”",
     "an amount of 0 or less is refused; after closing the browser, the expense is still there.",
     [("Check the expense data", "a test refuses an amount of 0 or less"),
      ("Save it in the browser", "a test saves an expense and reads it back")]),
    ("“As a user, I want to see this month’s expenses and their total.”",
     "the list shows my expenses and the right monthly total.",
     [("Show the list and the total", "2 expenses → both listed, with their sum"),
      ("Two pages and a menu", "a test goes from the Add page to the list")]),
]

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Learners split their own stories this way in the plan exercise."),
    ("The message",
     "A user story is too big for one prompt. Split it into atomic tasks: one thing each, verifiable, in order."),
    ("Reading the example",
     "Each story says the need in user words and when it is accepted. Under it, its tasks: what to build, and "
     "the check that proves the task is done. Story 1 gives the expense rules (T1) and saving in the browser "
     "(localStorage, T2); story 2 gives the list with the monthly total, then the two pages and the menu."),
    ("Test first, code second",
     "Each « Check » is a test: in every task the test is written first (RED), then the code (GREEN)."),
    ("Why atomic",
     "One task = one prompt, one branch, one review. If it goes wrong you lose one small task, not the app."),
    ("The trap",
     "Forgetting the task that wires the parts together (entry point, assembly): the check of the exercise "
     "sheet asks for it."),
    ("Ask the room",
     "« Which of your stories needs to be split the most? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "From Stories to Atomic Tasks", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — From Stories to Atomic Tasks", entries=_NOTES,
                                 position="left", width="50vw")
        with st_zoom(110):
            st_write(bs.body, "One thing · ", (bs.keyword, "verifiable"), " · ordered", tag=t.div)
        st_space("v", "1.5vh")
        n = 0
        for story, accepted, tasks in _STORIES:
            with st_zoom(_STORY_ZOOM), st_block(s.project.containers.callout):
                st_write(bs.story, (bs.keyword, "Story — "), story, tag=t.div)
                st_write(bs.accept, (s.bold, "Accepted when: "), accepted, tag=t.div)
            # One numbered row per task, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
            cols = "8% 4% 34% 50% 4%"
            cells = s.project.containers.rows(len(tasks), cols, filled=(2, 3))
            with st_zoom(_TASK_ZOOM), st_grid(cols=cols, gap="1vh 0.5vw", cell_styles=cells) as g:
                for what, check in tasks:
                    n += 1
                    with g.cell():
                        pass  # indent under the story
                    with g.cell():
                        st_write(bs.item + bs.number, f"{n}", tag=t.div)
                    with g.cell():
                        st_write(bs.item, what, tag=t.div)
                    with g.cell():
                        st_write(bs.item, (bs.check, "Check: "), check, tag=t.div)
                    with g.cell():
                        pass  # right margin
            st_space("v", "2vh")
