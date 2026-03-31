FROM python:3.13-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_BROWSER_GATHERUSAGESTATS=false \
    UV_LINK_MODE=copy

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl git && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install dependencies
# Strip local editable source, re-lock from PyPI, then install
COPY pyproject.toml uv.lock ./
RUN sed -i '/\[tool.uv.sources\]/,/^$/d' pyproject.toml && \
    uv lock && uv sync --frozen --no-dev

# Copy project files, then strip sources again so uv run works at runtime
COPY . .
RUN sed -i '/\[tool.uv.sources\]/,/^$/d' pyproject.toml

ENV PORT=8501
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["uv", "run", "streamlit", "run", "book.py", \
            "--server.port=8501", "--server.address=0.0.0.0"]
