"""Commit graphs drawn with StreamTeX grids — shared by the day-2 git graph slides (NG, 2026-11-27).

A graph is a list of rows; every row has the same number of cells, one per grid column. Columns alternate:
a label column, then node / line / node / line … Cells:
    ("n", text, tone)      commit (circle with a short type: test, feat, docs …)
    ("m", text)            merge commit with two parents (half blue, half green)
    ("l", tone)            line between two commits of the same branch
    ("a", glyph, tone)     arrow between rows (↘ a branch leaves, ↗ it comes back)
    ("k", name, tone)      branch name chip (first column)
    ("p", text, tone)      pointer chip: a name on a commit that is not a new commit (tag v0.1, main)
    ("c", text)            caption under a commit (its message)
    (".",)                 empty
"""
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s

MAIN = s.project.tone_blue      # mywork, the main line
TASK = s.project.tone_green     # task branches
SIDE = s.project.tone_purple    # practice branch, never merged
MERGE = s.project.tone_amber    # merge commit, tags


class GraphStyles:
    """Commit-graph styles (one place: used by several slides)."""
    caption = Style.create(s.project.titles.caption + s.center_txt + Style("line-height: 1.15;", "gitg_cap_lh"),
                           "gitg_caption")
    node = Style.create(s.project.titles.body + s.bold + s.center_txt
                        + Style("border-radius: 50%; width: 3.2em; height: 3.2em; line-height: 3.2em; padding: 0; "
                                "margin: 0 auto; white-space: nowrap; display: block;", "gitg_node_shape"), "gitg_node")
    merge_fill = Style("background: linear-gradient(135deg, #7AB8F5 50%, #27AE60 50%);", "gitg_merge_fill")
    glyph = Style.create(s.project.titles.body + s.bold + s.center_txt + Style("line-height: 1;", "gitg_glyph_lh"),
                         "gitg_glyph")
    chip = Style.create(s.project.titles.body + s.text.fonts.font_monospace + s.bold + s.center_txt
                        + Style("border-radius: 8px; padding: 4px 12px; white-space: nowrap;", "gitg_chip_shape"),
                        "gitg_chip")


gs = GraphStyles

GLYPH_ZOOM = 260


def cols(n_nodes, label="2.4fr", node="1fr", line="0.5fr"):
    """Grid columns: one label column, then node, line, node, … (n_nodes nodes)."""
    return " ".join([label] + [node if i % 2 == 0 else line for i in range(2 * n_nodes - 1)])


def draw(columns, rows, zoom=80):
    with st_zoom(zoom), st_grid(cols=columns, gap="0.4vh 0", cell_styles=s.project.containers.grid_cell_centered) as g:
        for row in rows:
            for cell in row:
                kind = cell[0]
                with g.cell():
                    if kind == "n":
                        st_write(cell[2].dot + gs.node, cell[1], tag=t.div)
                    elif kind == "m":
                        st_write(MERGE.dot + gs.node + gs.merge_fill, cell[1], tag=t.div)
                    elif kind == "l":
                        st_write(cell[1].line, "", tag=t.div)
                    elif kind == "a":
                        with st_zoom(GLYPH_ZOOM):
                            st_write(gs.glyph + cell[2].fg, cell[1], tag=t.div)
                    elif kind in ("k", "p"):
                        st_write(gs.chip + cell[2].chip + cell[2].fg, cell[1], tag=t.div)
                    elif kind == "c":
                        st_write(gs.caption, cell[1], tag=t.div)


def steps(items, zoom=78):
    """Numbered rows under a graph: (number, (st_write parts …))."""
    cols_ = "3% 4% 90% 3%"
    cells = s.project.containers.rows(len(items), cols_, filled=(2, 3))
    with st_zoom(zoom), st_grid(cols=cols_, gap="0.6vh 0", cell_styles=cells) as g:
        for num, parts in items:
            with g.cell():
                pass  # left margin
            with g.cell():
                st_write(s.project.titles.table_label, num)
            with g.cell():
                st_write(s.project.titles.table_cell, *parts)
            with g.cell():
                pass  # right margin


def legend(items, zoom=66):
    """The commit messages behind the msg ids of the graph: (id, message) rows (NG, 2026-11-27: ids on the
    graph, real example messages below it)."""
    cols_ = "3% 8% 86% 3%"
    cells = s.project.containers.rows(len(items), cols_, filled=(2, 3))
    mono = Style.create(s.project.titles.table_cell + s.text.fonts.font_monospace, "gitg_msg")
    with st_zoom(zoom), st_grid(cols=cols_, gap="0.4vh 0", cell_styles=cells) as g:
        for ident, message in items:
            with g.cell():
                pass  # left margin
            with g.cell():
                st_write(s.project.titles.table_label, ident)
            with g.cell():
                st_write(mono, message)
            with g.cell():
                pass  # right margin
