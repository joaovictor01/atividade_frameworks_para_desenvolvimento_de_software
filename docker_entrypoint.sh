#!/usr/bin/env bash
export FLASK_APP=app.py
export FLASK_ENV=production
# export PYTHONPATH=/usr/local/bin/python3
# alias python=/usr/local/bin/python3
uwsgi app.ini