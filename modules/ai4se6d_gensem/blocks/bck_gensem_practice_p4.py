"""P4 — Decision classification scenarios — 3 scenarios by IT expertise."""
# @guideline: minimalist-visual + maximize-viewport
# @pattern: exercise-flow
from streamtex import *
from streamtex.enums import Tags as t, ListTypes as lt
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_cell = s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_acc = s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_act = s.project.containers.cell_active_bg + s.project.containers.cell_pad_md + s.center_txt
_hdr = s.project.containers.table_header_cell
_norm = s.project.containers.table_normal_cell


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.text.wrap.hyphens, "p4_body")
    keyword = Style.create(s.Large + s.bold + s.project.colors.primary, "p4_kw")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "p4_acc")
    table_hdr = s.project.titles.table_header
    table_txt = s.project.titles.table_cell
    timer = Style.create(s.Huge + s.bold + s.project.colors.highlight + s.center_txt, "p4_timer")
bs = BlockStyles

_left = Style("text-align: left;", "p4_left")

_SCENARIOS_BEGINNER = [
    "Rename a variable across the project",
    "Add a small utility library (e.g., dayjs)",
    "Change the CSS framework (e.g., Tailwind \u2192 Bootstrap)",
    "Fix a visible bug in the UI",
]

_SCENARIOS_INTERMEDIATE = [
    ("Rename expense \u2192 transaction", "Auto"),
    ("Add dayjs for date formatting", "Inform"),
    ("Migrate React state \u2192 Redux", "Gate"),
    ("Fix rounding bug in totals", "Auto"),
    ("Add external currency API", "Gate"),
    ("Write unit tests for ExpenseForm", "Auto"),
    ("Replace Vitest with Jest", "Gate"),
    ("Add notes field to Expense", "Inform"),
]

_SCENARIOS_ADVANCED = [
    ("Migrate from localStorage to IndexedDB", "Gate"),
    ("Replace the ORM layer (Prisma \u2192 Drizzle)", "Gate"),
    ("Add OAuth2 authentication flow", "Gate"),
    ("Refactor to microservices architecture", "Gate"),
]


def build():
    st_slide_break(marker_label="P4: Classify Decisions")

    # ── Beginner ────────────────────────────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(70):
                st_write(bs.heading, "P4: Classify Decisions \u2014 Beginner", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="P4 Beginner \u2014 What to do",
                entries=[
                    ("Goal", "Learn the 3 decision tiers (Auto / Inform / Gate) with simple, concrete scenarios. The trainer explains each term."),
                    ("Time", "45 minutes: classify (15 min) + provoke guardrail (10 min) + discussion (20 min)."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

            with st_grid(
                cols="1fr 1fr",
                gap="16px",
                cell_styles=s.project.containers.cell_pad_sm,
            ) as g:
                with g.cell():
                    with st_block(_cell + _left):
                        with st_list(l_style=bs.body + _left, li_style=bs.body + _left, list_type=lt.unordered) as l:
                            with l.item():
                                st_write(bs.body + _left, (bs.keyword, "1. "), (bs.keyword, "Classify 4 scenarios: "), "rename variable, add library, change framework, fix bug \u2014 is each Auto, Inform, or Gate?")
                            with l.item():
                                st_write(bs.body + _left, (bs.keyword, "2. "), (bs.keyword, "Provoke 1 guardrail: "), "try to commit directly on main \u2014 what happens?")
                with g.cell():
                    with st_block(_cell + _left):
                        with st_list(l_style=bs.body + _left, li_style=bs.body + _left, list_type=lt.unordered) as l:
                            with l.item():
                                st_write(bs.body + _left, (bs.keyword, "3. "), (bs.keyword, "Discussion: "), "why did the agent refuse? What is a guardrail protecting?")

            st_space("v", 1)
            st_write(bs.accent, "Question: Can you explain the difference between Auto, Inform, and Gate?")
            st_space("v", 1)
            st_write(bs.timer, "45 minutes")

    st_slide_break(marker_label="P4: Intermediate")

    # ── Intermediate ────────────────────────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(70):
                st_write(bs.heading, "P4: Classify Decisions \u2014 Intermediate", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="P4 Intermediate \u2014 What to do",
                entries=[
                    ("Goal", "Classify 8 CalcApp scenarios, write consequence analyses, and provoke guardrails."),
                    ("Time", "45 minutes: classify (10 min) + consequences (10 min) + guardrails (10 min) + discussion (15 min)."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

            with st_zoom(85):
                with st_grid(cols="70% 30%", gap="6px", cell_styles=_hdr) as g:
                    with g.cell():
                        st_write(bs.table_hdr + s.center_txt, "Scenario")
                    with g.cell():
                        st_write(bs.table_hdr + s.center_txt, "Your Answer?")

                for scenario, _ in _SCENARIOS_INTERMEDIATE:
                    with st_grid(cols="70% 30%", gap="6px", cell_styles=_norm) as g:
                        with g.cell():
                            st_write(bs.table_txt + s.center_txt, scenario)
                        with g.cell():
                            st_write(bs.table_txt + s.center_txt, "Auto / Inform / Gate")

            st_space("v", 1)
            st_write(bs.accent, "Then: write Now / 3 months / 1 year consequences for 2 Gate decisions.")
            st_write(bs.timer, "45 minutes")

    st_slide_break(marker_label="P4: Advanced / Expert")

    # ── Advanced / Expert ───────────────────────────────────────────
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_zoom(70):
                st_write(bs.heading, "P4: Classify Decisions \u2014 Advanced / Expert", tag=t.div, toc_lvl="+1")
            st_hover_tooltip(
                title="P4 Advanced / Expert \u2014 What to do",
                entries=[
                    ("Goal", "Classify 12 scenarios (8 standard + 4 architectural), analyze all Gate consequences, provoke all 3 guardrail levels."),
                    ("Time", "45 minutes: classify (10 min) + consequences (15 min) + guardrails (10 min) + calibration discussion (10 min)."),
                ],
                scale="2vw", width="70vw", position="center",
            )
            st_space("v", 1)

            with st_zoom(80):
                with st_grid(
                    cols="1fr 1fr",
                    gap="16px",
                    cell_styles=s.project.containers.cell_pad_sm,
                ) as g:
                    with g.cell():
                        with st_block(_cell_act + _left):
                            with st_list(l_style=bs.body + _left, li_style=bs.body + _left, list_type=lt.unordered) as l:
                                with l.item():
                                    st_write(bs.body + _left, (bs.keyword, "1. "), (bs.keyword, "Classify 8 + 4 scenarios: "), "standard CalcApp + architectural (DB migration, ORM change, OAuth, microservices)")
                                with l.item():
                                    st_write(bs.body + _left, (bs.keyword, "2. "), (bs.keyword, "Consequence analysis: "), "for all 6 Gate decisions, write Now / 3 months / 1 year")
                    with g.cell():
                        with st_block(_cell_act + _left):
                            with st_list(l_style=bs.body + _left, li_style=bs.body + _left, list_type=lt.unordered) as l:
                                with l.item():
                                    st_write(bs.body + _left, (bs.keyword, "3. "), (bs.keyword, "Provoke all 3 guardrail levels: "), "Soft (>5 branches) + Hard (commit on main) + Emergency (force push)")
                                with l.item():
                                    st_write(bs.body + _left, (bs.keyword, "4. "), (bs.keyword, "Calibration: "), "how would you set Auto/Inform/Gate thresholds for your professional project?")

            st_space("v", 1)
            st_write(bs.accent, "Question: Should experts have fewer Gates? When should you override a guardrail?")
            st_space("v", 1)
            st_write(bs.timer, "45 minutes")
