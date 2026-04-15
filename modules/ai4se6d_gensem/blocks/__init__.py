"""Lazy-loading block registry with shared-blocks fallback."""

from pathlib import Path
from streamtex import ProjectBlockRegistry, BlockNotFoundError, BlockImportError

# Primary: local project blocks
registry = ProjectBlockRegistry(Path(__file__).parent)

# Fallback: shared blocks (trainer slides, glossary, etc.)
_shared_dir = Path(__file__).resolve().parent.parent.parent / "shared-blocks" / "blocks"
_shared_registry = (
    ProjectBlockRegistry(_shared_dir) if _shared_dir.exists() else None
)

__all__ = ["registry", "BlockNotFoundError", "BlockImportError"]


def __getattr__(name: str):
    # Try local blocks first
    try:
        return registry.get(name)
    except (BlockNotFoundError, BlockImportError):
        pass

    # Then shared blocks
    if _shared_registry is not None:
        try:
            return _shared_registry.get(name)
        except (BlockNotFoundError, BlockImportError):
            pass

    raise AttributeError(
        f"Block '{name}' not found in local or shared blocks"
    )


def __dir__():
    names = sorted(registry.list_blocks() + __all__)
    if _shared_registry is not None:
        names = sorted(set(names + _shared_registry.list_blocks()))
    return names
