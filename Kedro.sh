#!/usr/bin/env bash

python3.11 -m venv .venv
source .venv/bin/activate
trap "deactivate" EXIT SIGINT SIGTERM SIGHUP SIGQUIT
pip install -r requirements.txt
kedro run
