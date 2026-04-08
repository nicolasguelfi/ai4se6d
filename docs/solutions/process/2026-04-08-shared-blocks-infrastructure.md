---
title: Shared blocks infrastructure pattern for multi-module projects
category: process
scope: generic
origin: ai4se6d cross-module review (2026-04-08)
tags: [shared-blocks, registry, glossary, bibliography, multi-module, collection]
---

## Context

Multi-module training projects (e.g., ai4se6d with genai_intro, vibecoding, gensem) need to share common blocks (glossary, references, trainer profiles) and static assets (bibliography). Without centralization, definitions drift between modules.

## Problem

- `ProjectBlockRegistry` scans only its local `blocks/` directory
- `setup.py` adds `shared-blocks/` to `sys.path` but this doesn't help the registry
- Each module had its own `bck_glossary.py` with diverging definitions (e.g., VibeCoding defined as "pair programmer" in one module, "without closely reviewing" in another)
- Each module had its own `references.bib` with different bibkeys for the same sources

## Solution

### 1. Chained registry in `blocks/__init__.py`

```python
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
```

### 2. Shared bibliography

- Single `shared-blocks/static/references.bib` file
- Each `book.py` uses: `bib_sources=[str(_shared_static / "references.bib")]`
- Variable `_shared_static` already exists (used for `set_static_sources`)

### 3. Resolution priority

```
local blocks/ > shared-blocks/blocks/
```

A local block with the same name shadows the shared one (local wins).

### 4. Container compatibility

The path `blocks_dir.parent.parent.parent / "shared-blocks"` resolves correctly in Docker because the `modules/` directory structure is preserved in the image.

## Future

Ticket nicolasguelfi/streamtex#19 proposes native support in `ProjectBlockRegistry` with `auto_shared=True` and recursive scan. When implemented, the `__init__.py` workaround can be removed.

## Reference

- `modules/shared-blocks/blocks/bck_shared_glossary.py`
- `modules/shared-blocks/static/references.bib`
- Each module's `blocks/__init__.py`

## Applies when

Any multi-module project using `shared-blocks/` convention.
