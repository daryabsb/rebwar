#!/bin/bash

APP_PORT=${PORT:-8000}

cd /app/
/opt/venv/bin/gunicorn app.wsgi:application --bind "0.0.0.0:${APP_PORT}"