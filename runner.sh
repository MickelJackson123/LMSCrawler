#!/bin/bash
# Let's call this script venv.sh
source "$HOME/PycharmProjects/LMSCrawler/venv/bin/activate"
echo $PWD
pip3 install -r requirements.txt
python main.py