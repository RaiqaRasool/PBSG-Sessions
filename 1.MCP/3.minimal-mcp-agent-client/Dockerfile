FROM ghcr.io/astral-sh/uv:0.8.15 AS uv

FROM python:3.12-slim

COPY --from=uv /uv /usr/local/bin/uv

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev

COPY client.py ./

ENTRYPOINT ["uv", "run", "--no-sync", "python", "client.py"]
