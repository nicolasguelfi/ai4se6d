"""Slide — Review checklist — routing."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Review checklist — routing — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "tasks_routing_review_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "tasks_routing_review_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "tasks_routing_review_foot")
bs = BlockStyles


_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Walk through the five checks; learners apply them to the agent's"
     " routing code during the 13:30 exercise."),
    ("The message",
     "Five checks on the agent's routing code, each answerable in seconds — the first review habit of the "
     "afternoon."),
    ("What each check catches",
     "The wrong package (react-router-dom instead of react-router); plain <a href> links that reload the whole "
     "page; pages not in their own file under src/pages/; a test silently modified; a navigation that only "
     "looks right."),
    ("The key check",
     "git diff HEAD -- tests/ must show nothing: the GREEN prompt said « Do not change what the test checks ». If the agent "
     "changed it, the green result means nothing."),
    ("Try it in the browser",
     "npm run dev, click both links, use the back button: the tests do not cover everything."),
    ("Link",
     "« Trust, but verify » — the habit the review section practises at 14:30."),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Check — react-router in package.json",
     "Open package.json, section « dependencies »: react-router must be there, react-router-dom must not. Quick "
     "check in the terminal: grep react-router package.json (grep prints the lines containing that text)."),
    ("Words — Link vs a href",
     "Link is react-router's link component: it changes the page without reloading the app. A plain HTML « a href"
     " » link reloads the whole page (and loses in-memory state)."),
    ("Command — git diff HEAD -- tests/",
     "git diff shows line by line what changed (- removed, + added). HEAD = your last commit (here the test: "
     "commit of RED): the comparison covers every change since then, added with git add or not. « -- » means "
     "« what follows is a path, not a branch name »; tests/ limits the output to that folder. Empty output = the "
     "test was not touched. Run it BEFORE the feat: commit; after it, use git diff HEAD~1 -- tests/ (HEAD~1 = the "
     "commit before). Plain git diff -- tests/ would miss changes already added. q quits a long diff."),
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
                st_write(bs.heading, "Review the Agent's Routing", tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Review the Agent's Routing", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")

        # One row per check, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        items = [
            ('Does ', (bs.cmd, 'package.json'), ' use ', (bs.cmd, 'react-router'), ', and not ',
             (bs.cmd, 'react-router-dom'), '?'),
            ('Do the pages link with ', (bs.cmd, 'Link'), ' rather than ', (bs.cmd, '&lt;a href&gt;'),
             ', so the page does not fully reload?'),
            ('Is there one file per page in ', (bs.cmd, 'src/pages/'), '?'),
            ('Is the test unchanged? Run ', (bs.cmd, 'git diff HEAD -- tests/'), ': it must show nothing.'),
            ('Run ', (bs.cmd, 'npm run dev'), ': do both links work, and does the browser’s back button work?'),
        ]
        cols = "5% 90% 5%"
        cells = s.project.containers.rows(len(items), cols, filled=(2,))
        with st_zoom(96), st_grid(cols=cols, gap="2vh 0.5vw", cell_styles=cells) as g:
            for parts in items:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "3vh")
        with st_zoom(94):
            st_write(bs.foot, 'Trust, but verify — you will need this habit at 14:30.', tag=t.div)
