"""Slide — Formal inspection vs testing — defect removal efficiency."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.bib import cite
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """Formal inspection vs testing — defect removal efficiency — styles."""
    heading = s.project.titles.heading
    body_center = Style.create(s.project.titles.body + s.center_txt, "review_jones_body_c")
    foot = Style.create(s.project.titles.caption + s.italic + s.center_txt, "review_jones_foot")
    source = s.project.citation + s.large + s.center_txt
    table_hdr = Style.create(s.project.titles.table_header + s.center_txt, "review_jones_th")
    table_txt = Style.create(s.project.titles.table_cell + s.center_txt, "review_jones_td")
    table_lbl = Style.create(s.project.titles.table_label, "review_jones_tl_left")
bs = BlockStyles


_NOTES = [
    ("The message",
     "Review and tests do not remove the same share of defects: formal code inspection removes far more of "
     "the defects present than unit or function testing."),
    ("The figures",
     "Defect removal efficiency, minimum / average: formal code inspection 60 % / 85 %; automated unit testing "
     "20 % / 40 %; function testing 33 % / 40 %. Capers Jones, data from more than 13,000 projects."),
    # The three practices in plain words (NG « ok », 2026-11-27)
    ("Formal code inspection",
     "People read the code together without running it, following a method: set roles (author, readers, "
     "moderator), a checklist, a meeting and a written list of the defects found. It finds logic errors, forgotten "
     "cases and unclear or risky code that no test would reveal. In the course: reading every line the agent wrote, "
     "or an AI review you triage."),
    ("Unit testing (automated)",
     "A small program checks one small part of the code (a function, a component) on its own, e.g. « formatAmount "
     "of 25.5 gives €25.50 ». Automated: one command (npm run test:run) reruns them all in seconds after each "
     "change. It finds errors in each brick right after writing it: the red-green of this morning's TDD."),
    ("Function testing",
     "Checks that a whole feature does what the user expects, using the app from the outside, as the user would, "
     "e.g. « I add a 12 € expense \"Lunch\": it appears in the list and the total goes up ». By hand or "
     "automated; several bricks together. It finds errors in how the bricks fit and needs that were misunderstood."),
    ("Picture it — a car",
     "Inspection = experts read the engine plans (« is it well designed? »). Unit test = each part is tested alone, "
     "the brake, the spark plug (« does this part work? »). Function test = a road test (« does the car do what the "
     "customer wants? »)."),
    ("How to read it",
     "« 85 % » means: of the defects present when the practice is applied, 85 % on average are removed by it. "
     "The practices find different defects, so they add up."),
    ("The trap",
     "Concluding « review instead of tests ». The conclusion is both — and today the participants did both: "
     "AI-TDD this morning, review this afternoon."),
    ("Ask the room",
     "« Which defect in your Part 2 code would a test never have found? »"),
]


def build():
    with st_block(s.project.containers.page_fill_top):
        # title and « i » on the same line, title smaller (NG, 2026-11-23: same recipes as the intro module)
        with st_grid(cols="95% 5%", cell_styles=s.project.containers.grid_cell_centered) as h:
            with h.cell(), st_zoom(80):
                st_write(bs.heading, 'Review vs Tests', tag=t.div, toc_lvl='+1')
            with h.cell():
                st_hover_tooltip(title="Trainer notes — Review vs Tests", entries=_NOTES,
                                 position="left", width="50vw")
        st_space("v", "2vh")

        # Header row, then one row per practice with alternating fills — motif L2 + fonds f1 (NG, 2026-11-23)
        cols = "5% 50% 20% 20% 5%"
        with st_zoom(134):
            with st_grid(cols=cols, gap="1vh 0.5vw",
                         cell_styles=[s.none, s.project.containers.table_header_cell,
                                      s.project.containers.table_header_cell,
                                      s.project.containers.table_header_cell, s.none]) as g:
                with g.cell():
                    pass  # left margin
                with g.cell():
                    st_write(bs.table_hdr, 'Practice')
                with g.cell():
                    st_write(bs.table_hdr, 'Minimum')
                with g.cell():
                    st_write(bs.table_hdr, 'Average')
                with g.cell():
                    pass  # right margin
            rows = [
                ('Formal code inspection', '60%', '85%'),
                ('Unit testing (automated)', '20%', '40%'),
                ('Function testing', '33%', '40%'),
            ]
            cells = s.project.containers.rows(len(rows), cols, filled=(2, 3, 4))
            with st_grid(cols=cols, gap="1.5vh 0.5vw", cell_styles=cells) as g:
                for practice, low, avg in rows:
                    with g.cell():
                        pass  # left margin
                    with g.cell():
                        st_write(bs.table_lbl, practice)
                    with g.cell():
                        st_write(bs.table_txt, low)
                    with g.cell():
                        st_write(bs.table_txt, avg)
                    with g.cell():
                        pass  # right margin
        st_space("v", "3vh")
        with st_zoom(107):
            st_write(
                bs.body_center,
                'Share of the defects present that each practice removes (data from 13,000+ projects).',
                tag=t.div,
            )
            st_write(bs.source, cite('jones-dre2011'), tag=t.div)
            st_space("v", "2vh")
            st_write(bs.foot, 'Not tests OR review: you need both — today you did both.', tag=t.div)
