"""Slide — test_evidence: Per-TASK Test Results (backlog.yaml)."""
# @guideline: minimalist-visual + maximize-viewport
from streamtex import *
from streamtex.enums import Tags as t
from custom.styles import Styles as s
from shared_widgets import st_hover_tooltip


class BlockStyles:
    """test_evidence artifact slide styles."""
    heading = s.project.titles.heading
    body = s.project.titles.body
    label = s.project.titles.label
    closing = s.project.titles.body + s.project.colors.highlight + s.bold

bs = BlockStyles

_BACKLOG_YAML = """\
# backlog.yaml — excerpt
- id: TASK-012
  type: feat
  sprint: 03
  status: done

  test_evidence:
    status: pass                  # absent | pass | fail | skipped
    campaign_ref: TCP-007
    timestamp: 2026-04-16T14:30:00Z
    pass_rate: 94                 # % of tests passing
    code_coverage: 78             # % of lines covered
    summary: "2 flakes in visual regression, non-blocking\""""


def build():
    st_marker("test_evidence \u2014 Per-TASK Test Results")
    with st_block(s.project.containers.page_fill_top):
        with st_zoom(90):
            st_write(bs.heading, "test_evidence \u2014 Per-TASK Test Results", tag=t.div, toc_lvl="+1")
        st_hover_tooltip(
            title="test_evidence \u2014 Structured per-TASK block",
            entries=[
                ("status", "absent (not yet run) | pass | fail | skipped. Single source of truth for this TASK's test state."),
                ("campaign_ref", "Links to the TCP-NNN campaign report (docs/sprints/sprint-NN/tests/TCP-NNN.md) that produced this evidence."),
                ("timestamp", "ISO-8601 of the canonical test run \u2014 when the evidence was collected."),
                ("pass_rate", "Percentage of tests passing (0-100). Captured from the run."),
                ("code_coverage", "Percentage of lines covered (0-100). Captured when the framework supports it."),
                ("summary", "One-line human-readable commentary \u2014 notable flakes, skipped suites, env quirks."),
                ("Distinct from health rollup", "status.yaml.test_pass_rate is a scalar 0-10 project-wide health dimension. test_evidence is per-TASK. Different concepts, different files."),
                ("Who writes it", "Written by the Canonical test run (PRODUCE Step 4 or /gse:tests --run) \u2014 same 7-step procedure, same output."),
            ],
            scale="2vw", width="70vw", position="center",
        )
        st_space("v", 0.5)

        with st_zoom(110):
            st_write(bs.body, (bs.label, "Example"), " \u2014 backlog.yaml after /gse:tests --run on TASK-012:")
            st_space("v", 0.5)

            st_code(s.none, code=_BACKLOG_YAML, language="yaml")

            st_space("v", 0.5)
            with st_block(s.project.containers.callout):
                st_write(
                    bs.closing,
                    "One campaign per TASK. Each TCP-NNN lives in docs/sprints/sprint-NN/tests/.",
                )
