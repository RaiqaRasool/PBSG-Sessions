FROM ghcr.io/astral-sh/uv:0.8.15 AS uv

FROM python:3.12-slim

COPY --from=uv /uv /usr/local/bin/uv

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev

COPY server.py ./

CMD ["uv", "run", "--no-sync", "python", "server.py"]

