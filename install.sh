#!/usr/bin/env sh

python3 -m venv .venv || echo "Failed to create virtual environment."
source .venv/bin/activate
pip install poetry
poetry install && echo "Install complete. Run run plot-kelly.sh with required arguments."
