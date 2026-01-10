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
# Run Unit Test (entire file - Python)
python manage.py test authentication --keepdb

# Run Unit Test (specific test)
python manage.py test authentication.tests.MagicLinkAuthTests.test_email_change_unauthorized --keepdb

* Git Scripts:
# Check status
clear; git status

# Commit and push
clear; git commit -am "";git push; git status

# View log
clear; git log --oneline