#!/bin/bash

#python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cd src
python3 main.py
cd ..
deactivate