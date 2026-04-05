# blocks/helpers.py — inject project styles globally
from streamtex import (
    BlockHelperConfig, set_block_helper_config,
    show_code as _show_code,
    show_explanation as _show_explanation,
    show_details as _show_details,
)
from custom.styles import Styles as s


class ProjectBlockHelperConfig(BlockHelperConfig):
    """Project-level helper configuration for ai4se6d_vibecoding."""

    def get_code_style(self):
        return s.project.containers.callout

    def get_explanation_style(self):
        return s.project.containers.callout

    def get_details_style(self):
        return s.project.containers.callout


set_block_helper_config(ProjectBlockHelperConfig())

# Re-export for block imports: from blocks.helpers import show_code, ...
show_code = _show_code
show_explanation = _show_explanation
show_details = _show_details
