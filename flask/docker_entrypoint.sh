#!/usr/bin/env bash
export FLASK_APP=app.py
export FLASK_ENV=production
uwsgi app.ini