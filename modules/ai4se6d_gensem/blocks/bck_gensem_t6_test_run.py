"""Slide — Canonical Test Run: 7 immutable steps shared by PRODUCE & /gse:tests --run."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip

_pf = s.project.containers.page_fill_top
_cell = s.project.containers.cell_primary_bg + s.project.containers.cell_pad_md + s.center_txt
_cell_acc = s.project.containers.cell_accent_bg + s.project.containers.cell_pad_md + s.center_txt


class BlockStyles:
    heading = s.project.titles.slide_title + s.center_txt
    body = Style.create(s.Large + s.text.wrap.hyphens, "ttr_body")
    badge = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "ttr_badge")
    step_title = Style.create(s.Large + s.bold + s.project.colors.primary, "ttr_title")
    step_desc = Style.create(s.Large + s.text.wrap.hyphens, "ttr_desc")
    accent = Style.create(s.Large + s.bold + s.project.colors.accent + s.center_txt, "ttr_acc")

bs = BlockStyles

_STEPS = [
    ("1", "Execute", "Run test suite in the worktree (PRODUCE) or project root/worktree (TESTS). Coverage enabled when the framework supports it."),
    ("2", "Capture", "Pass/fail per test, timings, stdout/stderr, stack traces, coverage data, screenshots and videos (when visual testing is on)."),
    ("3", "Persist raw evidence", "Save to tests/evidence/sprint-NN/TASK-NNN/ \u2014 results.json, coverage.json, screenshots, videos."),
    ("4", "Allocate TCP & create campaign", "Assign TCP-NNN id and create docs/sprints/sprint-NN/tests/TCP-NNN.md campaign report."),
    ("5", "Write test_evidence", "Populate the structured block on the TASK in backlog.yaml (status, campaign_ref, timestamp, pass_rate, code_coverage, summary)."),
    ("6", "Inline summary", "One-paragraph chat summary \u2014 counts, coverage, notable failures. You know without opening files."),
    ("7", "Refresh health & dashboard", "Update status.yaml health dimensions + dashboard cards (Sprint Workflow, Coherence Alerts)."),
]


def build():
    st_marker("Canonical Test Run")
    with st_block(_pf):
        with st_block(s.center_txt):
            with st_grid(
                cols="95% 5%",
                gap="0px",
                cell_styles=s.project.containers.grid_cell_centered,
            ) as g:
                with g.cell():
                    with st_zoom(90):
                        st_write(bs.heading, "Canonical Test Run \u2014 7 Immutable Steps", tag=t.div, toc_lvl="+1")
                with g.cell():
                    st_hover_tooltip(
                        title="Canonical Test Run \u2014 spec \u00a76.3",
                        entries=[
                            ("Two entry points", "/gse:produce Step 4 (automatic post-production run) and /gse:tests --run (explicit). Both MUST produce the same artefacts and the same user-visible output."),
                            ("Immutable", "The seven steps below are immutable. Each activity adds only its own pre/post-conditions; the core procedure never diverges."),
                            ("Why it matters", "A divergence between the two entry points is a methodology bug, not a feature. Same tests \u2192 same outputs \u2014 always."),
                            ("Evidence trail", "Steps 3-4 persist evidence and create the TCP-NNN campaign; step 5 links it to the TASK; step 6 surfaces results to the user; step 7 updates the project health."),
                            ("See also", "test_evidence slide (step 5 output), /gse:tests slide (activity wrapper), /gse:produce slide (entry point 1)."),
                        ],
                        scale="2vw", width="70vw", position="left",
                    )
            st_space("v", 0.8)

        with st_zoom(95):
            for num, title, desc in _STEPS:
                cell_s = _cell_acc if int(num) % 2 == 1 else _cell
                with st_grid(cols="6% 94%", gap="12px", cell_styles=cell_s) as g:
                    with g.cell():
                        st_write(bs.badge, num)
                    with g.cell():
                        st_write(bs.body, (bs.step_title, title), (bs.step_desc, f" \u2014 {desc}"))
                st_space("v", 0.2)

            st_space("v", 0.5)
            st_write(bs.accent, "Both /gse:produce and /gse:tests --run invoke the same 7 steps. Any divergence is a methodology bug.")
