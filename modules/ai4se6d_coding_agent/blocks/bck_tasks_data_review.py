"""Slide — Review checklist — data layer."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Review checklist — data layer — styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.text.wrap.hyphens, "tasks_data_review_body")
    cmd = Style.create(s.text.fonts.font_monospace + s.project.colors.accent, "tasks_data_review_cmd")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "tasks_data_review_foot")
bs = BlockStyles


_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Walk through the five checks; learners apply them during the "
     "13:30 exercise (the browser refresh check is the decisive one)."),
    ("The message",
     "Five checks on the agent's data layer: types, storage, form, navigation, persistence."),
    ("What each check catches",
     "A type left as any; data kept in React state instead of localStorage; uncontrolled form inputs "
     "(no value + onChange); a missing redirect to / with useNavigate after Add."),
    ("The decisive check",
     "Refresh the browser: is the expense still there? It is the quickest way to see whether the storage is "
     "real."),
    ("The trap",
     "Most common slip: data kept in React state only — the test may pass, the data is gone at the first "
     "refresh."),
    ("Ask the room",
     "« Who found something with this checklist that the tests did not catch? »"),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Words — any",
     "In TypeScript, any means « any type »: it switches type checking off. Search for it: grep -rn \"any\" src/ "
     "(-r = in all sub-folders, -n = with line numbers)."),
    ("Words — value + onChange",
     "A « controlled » input: value = what the input shows comes from React state, onChange = the function that "
     "updates that state at each keystroke. Without them React does not know the form's content."),
    ("Words — useNavigate",
     "react-router function that returns navigate; navigate(\"/\") goes to the Dashboard from code, e.g. after "
     "saving."),
    ("Check — the refresh",
     "In the browser (npm run dev): add an expense, press F5 (Cmd+R on Mac) to reload the page. Still there = "
     "really stored in localStorage; gone = kept only in React state, which is erased by a reload."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Review the Agent's Data Layer", tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Review the Agent's Data Layer", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")

        # One row per check, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        items = [
            ('Types in ', (bs.cmd, 'src/expense.ts'), ', no ', (bs.cmd, 'any'), '?'),
            ('Storage really uses localStorage — not just React state?',),
            ('Form inputs controlled (', (bs.cmd, 'value'), ' + ', (bs.cmd, 'onChange'), ')?'),
            ('After Add, back to ', (bs.cmd, '/'), ' with ', (bs.cmd, 'useNavigate'), '?'),
            ('Refresh the browser: is your expense still there?',),
        ]
        cols = "5% 90% 5%"
        cells = s.project.containers.rows(len(items), cols, filled=(2,))
        with st_zoom(118), st_grid(cols=cols, gap="3.5vh 0.5vw", cell_styles=cells) as g:
            for parts in items:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "4vh")
        with st_zoom(115):
            st_write(
                bs.foot,
                'Most common slip: data kept in React state only — gone at the first refresh.',
                tag=t.div,
            )
