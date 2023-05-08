FROM mcr.microsoft.com/devcontainers/base:jammy

RUN apt update && export DEBIAN_FRONTEND=noninteractive \
    && apt install -y --no-install-recommends \
    build-essential python3-dev libcairo2-dev libpango1.0-dev ffmpeg python3-pip \
    texlive texlive-latex-extra

RUN pip3 install manim
