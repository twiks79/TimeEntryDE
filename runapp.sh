#!/bin/bash

# Activate the virtual environment
source env/bin/activate

# Run the Flask app
export FLASK_APP=app.py
export FLASK_ENV=development

flask run