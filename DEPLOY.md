# AI4SE6D — Deployment Guide

## Architecture

Single Docker image, multiple Coolify services (one per module).
Each service sets `FOLDER=modules/<module_name>` to select which module to run.

```
ai4se6d (GitHub repo)
  → Docker build → single image
    → Coolify service: ai4se6d-collection     (FOLDER=modules/ai4se6d_collection)
    → Coolify service: ai4se6d-genai-intro    (FOLDER=modules/ai4se6d_genai_intro)
```

## GitHub Secret Required

Add this secret to `github.com/nicolasguelfi/ai4se6d` → Settings → Secrets → Actions:

| Secret | Value | Source |
|--------|-------|--------|
| `COOLIFY_API_TOKEN` | `1\|CXII0eH7...` | Coolify → Security → API Tokens |

## Coolify Service Setup

For each module, create a service on Coolify (https://coolify.streamtex.org):

### 1. ai4se6d-collection (Hub)

- **Source**: GitHub → `nicolasguelfi/ai4se6d` branch `main`
- **Build**: Dockerfile (at repo root)
- **Environment Variables**:
  - `FOLDER=modules/ai4se6d_collection`
  - `STX_URL_GENAI_INTRO=https://ai4se6d-genai-intro.streamtex.org`
- **Domain**: `ai4se6d.streamtex.org`
- **Port**: 8501

### 2. ai4se6d-genai-intro

- **Source**: GitHub → `nicolasguelfi/ai4se6d` branch `main`
- **Build**: Dockerfile (at repo root)
- **Environment Variables**:
  - `FOLDER=modules/ai4se6d_genai_intro`
  - `STX_OPENAI_API_KEY=sk-proj-...` (for AI image generation)
- **Domain**: `ai4se6d-genai-intro.streamtex.org`
- **Port**: 8501

### 3. Coolify UUIDs (already configured)

The workflow UUIDs in `.github/workflows/hetzner-deploy.yml` are:

```json
{
  "ai4se6d-collection":   {"uuid": "ilkmnoz457cta2j1z3k8ax8m"},
  "ai4se6d-genai-intro":  {"uuid": "x45el0zeq6eqhhv1vo99mz20"}
}
```

## Deployment Flows

### Automatic (on push to main)

```
git push origin main
  → GitHub Actions: hetzner-deploy.yml
    → Wait for streamtex >= .stx-version on PyPI
    → Detect which modules changed
    → Trigger Coolify deploy for affected services only
```

### Manual (workflow_dispatch)

```
GitHub → Actions → Deploy to Hetzner → Run workflow
  → Deploys ALL services
```

### Manual (CLI)

```bash
# Deploy a specific service
curl -s "https://coolify.streamtex.org/api/v1/deploy?uuid=<UUID>" \
  -H "Authorization: Bearer $COOLIFY_API_TOKEN"

# Or use stx deploy (if configured)
stx deploy update
```

## Local Development

```bash
# Option A: Docker Compose (all modules)
docker compose up --build

# Option B: Direct (individual modules)
cd modules/ai4se6d_genai_intro
uv run streamlit run book.py --server.port 8502

cd modules/ai4se6d_collection
uv run streamlit run book.py --server.port 8501
```

## Adding a New Module

1. Create `modules/ai4se6d_<name>/` with `book.py`, `setup.py`, `blocks/`, `custom/`, `.streamlit/`
2. Add `[projects.<name>]` entry in `modules/ai4se6d_collection/collection.toml`
3. Create Coolify service with `FOLDER=modules/ai4se6d_<name>`
4. Add the UUID to `.github/workflows/hetzner-deploy.yml`
5. Add `STX_URL_<NAME>=https://...` env var to the collection service
6. Add service to `docker-compose.yml`
7. Commit and push

## Version Gating

`.stx-version` contains the minimum StreamTeX version required.
Both the CI workflow and Dockerfile validate this:

- **CI**: Polls PyPI up to 6 minutes waiting for the required version
- **Docker**: Build fails if installed version < required

To update: publish new streamtex to PyPI first, then bump `.stx-version`.
