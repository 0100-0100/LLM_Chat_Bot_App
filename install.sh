#!/usr/bin/env bash
python3 -m venv .venv
if [ $? -ne 0 ]; then
    echo 'Error while creating virtual environment with python3 -m venv .venv'
    exit
fi
source .venv/bin/activate
pip3 install -r requirements.txt
