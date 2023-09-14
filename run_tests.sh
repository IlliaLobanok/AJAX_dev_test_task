#!/bin/bash

cd "/home/charlie/Documents/work/py dev in test AJAX/pythonProject" || exit
source venv/bin/activate
export PYTHONPATH="${PYTHONPATH}:~/Documents/work/py dev in test AJAX/pythonProject"
pytest -v tests/main/test_menu.py
