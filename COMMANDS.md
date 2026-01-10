This file is meant to be a reference to useful .venv/python commands; Copy and Paste is king sometimes.

* Virtual Environment Commands:
# Create new venv
python -m venv venv

# Start venv session
./.venv/Scripts/Activate.ps1

* Django Server Commands:
# Start Django Server
python manage.py runserver

* Unit Testing Commands:
# Run all tests
pytest

# Run tests in specific file
pytest tests/test_simulation.py

# Run specific test
pytest tests/test_simulation.py::TestSimulateExponentialGrowth::test_default_parameters

# Run tests with verbose output
pytest -v

* Git Scripts:
# Check status
clear; git status

# Commit and push
clear; git commit -am "";git push; git status

# View log
clear; git log --oneline