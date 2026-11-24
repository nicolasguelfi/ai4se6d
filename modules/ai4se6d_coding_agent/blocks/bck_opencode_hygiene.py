"""Slide — What NOT to put in the context."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Context hygiene styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    keyword = s.project.titles.keyword
    danger = Style.create(s.project.titles.keyword + s.project.colors.critical, "hyg_danger")
    closing = Style.create(s.project.titles.body_accent + s.center_txt, "hyg_closing")
bs = BlockStyles

_NOTES = [
    ("The message",
     "Less but relevant beats more: what you keep OUT of the context matters as much as what you put in."),
    ("Secrets first",
     "Never paste or @mention .env, your model key or passwords: whatever enters the context is sent to the "
     "model provider."),
    ("Noise",
     "Generated folders (node_modules/, dist/) stay in .gitignore; paste the 10 lines of a log that matter, not the "
     "whole log."),
    ("Old tasks",
     "One task, one session: /new. A previous task left in the conversation pulls the agent back to it."),
    ("Link to the day",
     "The CalcApp AGENTS.md rule « Never commit secrets (.env* stays out of git) » is the same idea on the Git "
     "side."),
    ("Ask the room",
     "« Has anyone already pasted a key into a chat? What did you do next? »"),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("File — .env",
     "A hidden file (starts with a dot) holding secrets such as API keys, as NAME=value lines. Never pasted, never"
     " @mentioned, never committed."),
    ("File — .gitignore",
     "Lists the files and folders Git must ignore (one per line). In the starter: node_modules, dist, .env, "
     ".env.*. Ignored files never show in git status."),
    ("Folders — node_modules/ and dist/",
     "node_modules/ = the libraries installed by npm ci (thousands of files, rebuilt any time). dist/ = the built "
     "app produced by npm run build. Generated, so not worth any context."),
    ("Command — /new",
     "Typed in the opencode prompt box: starts a new, empty session (conversation). AGENTS.md is read again, the "
     "previous chat is forgotten, your files are unchanged. Shortcut: Ctrl+X then N."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "What NOT to Put in Context", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — What NOT to Put in Context", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")

        # One row per item, alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        items = [
            ((bs.danger, "Secrets"), " — .env, your model key, passwords: never paste, never @"),
            ((bs.keyword, "Generated folders"), " — node_modules/, dist/ stay in .gitignore"),
            ((bs.keyword, "Whole logs"), " — paste the 10 lines that matter"),
            ((bs.keyword, "Old tasks"), " — one task, one session: /new"),
        ]
        cols = "5% 90% 5%"
        cells = s.project.containers.rows(len(items), cols, filled=(2,))
        with st_zoom(115), st_grid(cols=cols, gap="3vh 0.5vw", cell_styles=cells) as g:
            for parts in items:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.body, *parts, tag=t.div)
                with g.cell():
                    pass  # right margin
        st_space("v", "5vh")
        with st_zoom(120):
            st_write(bs.closing, "Less but relevant beats more.", tag=t.div)
