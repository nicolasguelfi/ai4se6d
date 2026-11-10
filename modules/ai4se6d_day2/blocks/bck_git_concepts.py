"""Slide — Four Git words: repository, commit, branch, remote."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s


class BlockStyles:
    """Concept cards styles."""
    heading = s.project.titles.heading
    term = s.project.titles.subtitle
    text = s.project.titles.table_cell
bs = BlockStyles

_CARDS = [
    ("Repository", "The folder Git tracks. Its hidden .git/ holds the whole history."),
    ("Commit", "A snapshot + a message + a link to its parent. Commits form your timeline."),
    ("Branch", "A parallel timeline. Like it? Merge it. Don’t? Delete it."),
    ("Remote", "A copy on a server such as GitHub, usually called origin."),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(75):
            st_write(bs.heading, "Four Words to Know", tag=t.div, toc_lvl="+1")
        st_space("v", 1)
        with st_grid(cols=s.project.containers.responsive_2col, grid_style=s.project.containers.gap_24) as g:
            for term, text in _CARDS:
                with g.cell():
                    with st_block(s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md):
                        st_write(bs.term, term, tag=t.div)
                        st_write(bs.text, text, tag=t.div)
