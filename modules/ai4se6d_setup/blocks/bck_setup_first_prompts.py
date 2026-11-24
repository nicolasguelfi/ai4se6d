"""Slide — Suggested first prompts for the three ideas."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """First prompts slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    label = s.project.titles.label
bs = BlockStyles

_CODE_ZOOM = 175  # st_code font_size is not applied by Pygments: zoom instead
_PROMPTS = [
    ("Recipe Finder", "Create a Recipe Finder web app: type ingredients, see recipes."),
    ("Habit Tracker", "Build a Habit Tracker web app: daily check-off and streaks."),
    ("Movie Watchlist", "Create a Movie Watchlist web app: save movies, rate them 1-5."),
]

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type yet. Show the three ready-made prompts; learners paste theirs "
     "into opencode once their folder is set up (next slide)."),
    ("The message",
     "One first prompt per idea, ready to copy: one sentence saying WHAT the app does, nothing about how."),
    ("How to use them",
     "Copy the prompt (copy button of the code box), paste it into opencode, let the agent build, then react: "
     "the core loop."),
    ("The trap",
     "The prompt says nothing about storage, layout or errors: the agent decides all of it. That is vibe coding — "
     "note what it chose for you in notes.md."),
    ("Link to tomorrow",
     "Day 2 starts from a plan instead of a one-line prompt: the same intent, written down before the agent works."),
    ("Ask the room",
     "« What would you add to this sentence to get the app YOU want? »"),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Prompt — Create a Recipe Finder web app: type ingredients, see recipes.",
     "« Create a … web app » = the agent writes files for an app that runs in the browser, with technologies it "
     "chooses. Before the colon: the product; after it: the one behaviour wanted (enter ingredients, get matching "
     "recipes). Nothing says where the recipes come from: the agent will invent a small list or propose a service."),
    ("Prompt — Build a Habit Tracker web app: daily check-off and streaks.",
     "« daily check-off » = tick each habit done today; « streaks » = count of days in a row. Nothing says where the "
     "data is kept: the agent usually picks the browser's local storage (lost if you clear the browser)."),
    ("Prompt — Create a Movie Watchlist web app: save movies, rate them 1-5.",
     "Two behaviours: keep a list of movies and give each a rating from 1 to 5. Nothing about posters or a movie "
     "database: the agent decides (often you type titles by hand)."),
    ("Where to paste",
     "In the opencode window started in ~/ai4se/freeselfapp (next slide), not in the shell and not in the tutor "
     "window. Enter sends it; the agent then reads the folder, writes files and may ask permission to run "
     "commands (e.g. npm install): read each request before accepting."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "First Prompts", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — First Prompts", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")

        # Outer 5 % margins; each prompt stays a copyable code box (NG, 2026-11-23)
        with st_grid(cols="5% 90% 5%", cell_styles=s.project.containers.row_cell_left) as g:
            with g.cell():
                pass
            with g.cell():
                for name, prompt in _PROMPTS:
                    with st_block(s.none):
                        with st_zoom(120):
                            st_write(bs.label, name, tag=t.div)
                        with st_zoom(_CODE_ZOOM):
                            st_code(s.none, code=prompt, language="text", line_numbers=False)
                    st_space("v", "7vh")
            with g.cell():
                pass
