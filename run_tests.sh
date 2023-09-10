#!/bin/bash

cd "~/Documents/work/py dev in test AJAX/pythonProject"
source venv/bin/activate
export PYTHONPATH="${PYTHONPATH}:~/Documents/work/py dev in test AJAX/pythonProject"
pytest
