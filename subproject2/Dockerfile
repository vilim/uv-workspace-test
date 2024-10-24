ARG BASE_IMAGE="ghcr.io/astral-sh/uv:python3.12-bookworm-slim"

###################################################
# Image for building uv environment
###################################################

FROM ${BASE_IMAGE} as uv-test-build

#USER root
#RUN apt-get update && apt-get install -y libgl1

WORKDIR /app
COPY pyproject.toml uv.lock /app/

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

ADD subproject1 /app/subproject1
ADD subproject2 /app/subproject2

RUN uv sync --all-extras --dev --frozen --no-install-workspace