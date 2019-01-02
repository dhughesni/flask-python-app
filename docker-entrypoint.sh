#!/bin/sh
pip install -r requirements.txt
pip install -e .
flaskPythonApp run --host=0.0.0.0 --port=5000
