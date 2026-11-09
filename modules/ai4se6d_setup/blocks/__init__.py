"""Blocks package — lazy-loaded via streamtex.ProjectBlockRegistry."""
from pathlib import Path
from streamtex import ProjectBlockRegistry, BlockNotFoundError, BlockImportError

# Primary: local blocks
registry = ProjectBlockRegistry(Path(__file__).parent)

# Fallback: shared blocks (convention: ../shared-blocks/blocks/)
_shared_dir = Path(__file__).resolve().parent.parent.parent / "shared-blocks" / "blocks"
_shared_registry = ProjectBlockRegistry(_shared_dir) if _shared_dir.exists() else None

__all__ = ["registry", "BlockNotFoundError", "BlockImportError"]


def __getattr__(name: str):
    try:
        return registry.get(name)
    except (BlockNotFoundError, BlockImportError):
        pass
    if _shared_registry:
        try:
            return _shared_registry.get(name)
        except (BlockNotFoundError, BlockImportError):
            pass
    raise AttributeError(f"Block '{name}' not found in local or shared blocks")


def __dir__():
    shared = _shared_registry.list_blocks() if _shared_registry else []
    return sorted(set(registry.list_blocks() + shared + __all__))
