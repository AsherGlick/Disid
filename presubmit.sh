#!/bin/bash
source ./venv/bin/activate
FILES=`find . -type f -name "*.py" -not -path "./venv/*"`
flake8 --ignore=E501,E266,W503 $FILES
mypy --strict $FILES


# Run Unit Tests
coverage run -m unittest discover -s . -p '*_test.py'

# Integration Tests
# coverage run -a someotherfile.py args

coverage report -m --omit='venv/*'
