#!/bin/bash

# Remove the virtual environment if it exists
rm -rf env

# Create a new virtual environment
python -m venv env

# Activate the virtual environment
source env/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt