FROM python:3.13.9-trixie

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_PROJECT_ENVIRONMENT=/usr/local
ENV PYTHONPATH=/app

RUN pip install uv

COPY pyproject.toml uv.lock /app/
RUN uv sync --frozen
