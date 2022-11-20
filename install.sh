#!/usr/bin/env sh

# cd ./PyManifold || echo "PyManifold not found. Please run this in the project root directory of plot-kelly."
python3 -m venv .venv || echo "Failed to create virtual environment."
source .venv/bin/activate || echo "Failed to activate virtual environment."
command -v pip3 || echo "pip not found. Please install pip."
pip3 install poetry || echo "Failed to install poetry in virtual environment."
poetry install && echo "Install complete. Run run plot-kelly.sh with required arguments."
