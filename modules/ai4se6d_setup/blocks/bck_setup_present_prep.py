"""Slide — FreeSelfApp iteration 3 (14:55): opencode makes a 6-minute presentation (NG, 2026-11-24)."""
# @guideline: maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Iteration 3 slide styles."""
    heading = s.project.titles.slide_title + s.center_txt
    body = s.project.titles.body
    label = s.project.titles.label
    keyword = s.bold + s.project.colors.accent
    warn = s.bold + s.project.colors.highlight
bs = BlockStyles

_PROMPT = ("Make a 6-minute presentation of my project for a team meeting — "
           "one HTML file I open in my browser.")

_NOTES = [
    ("Trainer action",
     "Learners do it — on their machine. They paste the prompt as is and open the HTML file. Do NOT add any "
     "structure to the prompt: what the presentation covers is what you want to observe."),
    ("Hidden goal — keep it to yourself",
     "How does each learner (and the model) see a software engineer's work? Do they talk about phases at all?"),
    ("Observation grid (15:30)",
     "Needs / requirements? Design or architecture? Tests? Risks? Maintenance? Deployment? Who decided — the learner "
     "or the AI? A failure shown? What the speaker adds or drops compared with the slides."),
    ("Practical",
     "One HTML file opens anywhere, no install. Google Meet link sent by Teams direct message or e-mail. In the room, "
     "microphones and speakers OFF in Meet (echo)."),
    ("Timing",
     "14:55 prompt · ~15:10 presentation checked in the browser · 15:15 break · 15:30 presentations."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "Iteration 3 — Your Presentation", tag=t.div, toc_lvl="1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Iteration 3 — Your Presentation", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")
        with st_zoom(110):
            st_write(bs.body, (bs.label, "Ask opencode:"), tag=t.div)
        with st_zoom(150):
            st_code(s.none, code=_PROMPT, language="text", line_numbers=False)
        st_space("v", "3vh")
        with st_zoom(110):
            st_write(bs.body, "Open it in your browser. ", (bs.keyword, "Commit"), ".", tag=t.div)
            st_space("v", "3vh")
            st_write(bs.body, (bs.label, "15:15 "), "break · ", (bs.label, "15:30 "), "you present ",
                     (bs.keyword, "6 min"), ", sharing your screen on ", (bs.keyword, "Google Meet"),
                     " (link by Teams / e-mail).", tag=t.div)
            st_space("v", "2vh")
            st_write(bs.body, (bs.warn, "In the room: "), "microphone and speakers OFF in Meet.", tag=t.div)
