"""Slide — Pattern 3: one branch per task (commit graph drawn with StreamTeX grids, NG 2026-11-24).

Replaces the old PNG « Git: Branches & Merging »: same story (a task branch leaves the main line, gets its own
commits, is merged back), with the names the learners use today (mywork, feat/add-history).
"""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_MAIN = s.project.tone_blue      # the main line (mywork)
_TASK = s.project.tone_green     # the task branch
_MERGE = s.project.tone_amber    # the merge


class BlockStyles:
    """Branch graph styles."""
    heading = s.project.titles.heading
    body = Style.create(s.project.titles.body + s.center_txt, "gitbr_body")
    keyword = s.project.titles.keyword
    label = Style.create(s.project.titles.caption + s.center_txt + Style("white-space: nowrap;", "gitbr_nowrap"),
                         "gitbr_label")
    node = Style.create(s.project.titles.body + s.bold + s.center_txt
                        + Style("border-radius: 50%; width: 2.4em; height: 2.4em; line-height: 2.4em; "
                                "margin: 0 auto;", "gitbr_node_shape"), "gitbr_node")
    merge_node = Style("background: linear-gradient(135deg, #7AB8F5 50%, #27AE60 50%);", "gitbr_merge_fill")
    glyph = Style.create(s.project.titles.body + s.bold + s.center_txt + Style("line-height: 1;", "gitbr_glyph_lh"),
                         "gitbr_glyph")
    tag = Style.create(s.project.titles.body + s.text.fonts.font_monospace + s.bold + s.center_txt
                       + Style("border-radius: 8px; padding: 4px 12px; white-space: nowrap;", "gitbr_tag_shape"),
                       "gitbr_tag")
    def_card = Style("min-height: 24vh; width: 100%;", "gitbr_def_card")
    def_text = Style.create(s.project.titles.body + s.center_txt, "gitbr_def")
bs = BlockStyles

_GRAPH_ZOOM = 80    # commit graph; tuned by measure (content bottom <= 1000 px at 1920x1080)
_GLYPH_ZOOM = 250   # the ↘ / ↗ arrows of the branch
_DEF_ZOOM = 60      # the three definition cards
_CAPTION_ZOOM = 88

# One column per position: N = commit, L = line, . = empty, D/U = branch leaves / comes back
_COLS = "2.2fr 1fr 0.55fr 1fr 0.55fr 1fr 0.55fr 1fr 0.55fr 1fr 0.55fr 1fr 0.55fr 1fr 0.55fr 1fr"
# main line: (kind, text, label)
_MAIN_ROW = [("tag", "mywork", ""), ("N", "c1", "j2-start"), ("L",), ("N", "c2", "plan"), ("L",),
             ("N", "c3", "expense type"), ("L",), ("L",), ("L",), ("N", "c4", "fix total"), ("L",),
             ("N", "c5", "style"), ("L",), ("M", "M", "merge"), ("L",), ("N", "c8", "continue")]
_TASK_ROW = [("tag", "feat/add-history", ""), (".",), (".",), (".",), (".",), (".",), ("D",), ("N", "c6", "test: history"), ("L",),
             ("N", "c7", "feat: history"), ("L",), ("L",), ("U",), (".",), (".",), (".",)]

_DEFS = [
    (_MAIN, "Commit", "A snapshot of the project at one moment: an ID, a message, a link to the commit before."),
    (_TASK, "Branch", "A parallel line for one task. Works? Merge it. Doesn't? Delete it: your line is untouched."),
    (_MERGE, "Merge", "Brings the task's commits back into your line: the merge commit has two parents."),
]

_NOTES = [
    ("Trainer action",
     "Read and comment — nothing to type. Follow the green line with your finger: it leaves mywork after c3, gets two "
     "commits, comes back at M. Learners create their own branch in the Git exercise."),
    ("The message",
     "Third habit: one branch per task. The agent never works directly on your main line."),
    ("Read the graph",
     "Blue = your main line (mywork), c1 … c8 = commits in time order. Green = the task branch feat/add-history: "
     "c6 and c7 are made on it while mywork can still move (c4, c5). M = the merge commit: it joins both lines."),
    ("How",
     "git switch -c feat/add-history (name it after your task) creates the branch. It works: merge it back. It does "
     "not: delete it — nothing is lost."),
    ("Why it matters with an agent",
     "Each task of the plan becomes a branch, so each change of the agent stays isolated and easy to check."),
    ("Link to the day",
     "The build this afternoon uses one branch per task of docs/plan.md."),
    ("Ask the room",
     "« What happens to your main line if the agent's attempt fails on a branch? »"),
    # Command recap: every command and option of the slide, in plain words (NG, 2026-11-24)
    ("Command — git switch -c feat/add-history",
     "Creates a new branch and moves onto it, starting from where you are now. -c = create. feat/add-history = its"
     " name; the / is just part of the name (a « feat/ » prefix groups task branches), not a folder. Older "
     "equivalent: git checkout -b feat/add-history."),
    ("Command — merge it back",
     "git switch mywork (go back to your main line), then git merge feat/add-history: brings the commits of the "
     "task branch into mywork. If both changed the same lines, Git stops and asks you to choose (« conflict »)."),
    ("Command — delete it",
     "git branch -d feat/add-history deletes the branch once it is merged; -d refuses if it is not. -D (capital) "
     "deletes anyway and drops its commits: use it to throw away a failed attempt. You cannot delete the branch "
     "you are on — switch first. git branch alone lists the branches, * marks the current one."),
]


def _row(cells, tone, g):
    """One line of the graph: commits (N), merge (M), line pieces (L), branch arrows (D/U), tags."""
    for cell in cells:
        kind = cell[0]
        with g.cell():
            if kind == "N":
                st_write(bs.node + tone.dot, cell[1], tag=t.div)
            elif kind == "M":
                st_write(bs.node + _MERGE.dot + bs.merge_node, cell[1], tag=t.div)
            elif kind == "L":
                st_write(tone.line, "", tag=t.div)
            elif kind in ("D", "U"):
                with st_zoom(_GLYPH_ZOOM):
                    st_write(bs.glyph + _TASK.fg, "↘" if kind == "D" else "↗", tag=t.div)
            elif kind == "tag":
                st_write(bs.tag + tone.chip + tone.fg, cell[1], tag=t.div)


def _labels(cells, g):
    for cell in cells:
        with g.cell():
            if cell[0] in ("N", "M"):
                st_write(bs.label, cell[2], tag=t.div)


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, "3 · One Branch per Task", tag=t.div, toc_lvl="+1")
            with h.cell():
                st_hover_tooltip(title="Trainer notes — One Branch per Task", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "3vh")
        with st_zoom(_GRAPH_ZOOM), st_grid(cols=_COLS, gap="1vh 0",
                                           cell_styles=s.project.containers.grid_cell_centered) as g:
            _row(_MAIN_ROW, _MAIN, g)
            _labels(_MAIN_ROW, g)
            _row(_TASK_ROW, _TASK, g)
            _labels(_TASK_ROW, g)
        st_space("v", "3vh")
        with st_zoom(_DEF_ZOOM), st_grid(cols="1fr 1fr 1fr", gap="0 2vw",
                                         cell_styles=s.project.containers.grid_cell_centered) as g:
            for tone, word, text in _DEFS:
                with g.cell(), st_block(tone.card + bs.def_card):
                    st_write(tone.title, word, tag=t.div)
                    st_write(bs.def_text, text, tag=t.div)
        st_space("v", "3vh")
        with st_zoom(_CAPTION_ZOOM):
            st_write(
                bs.body, (bs.keyword, "git switch -c feat/add-history"),
                " — works? merge it back. Doesn’t? delete it: nothing is lost.", tag=t.div,
            )
