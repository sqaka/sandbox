#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install --upgrade setuptools
pip install -r requirements.txt

mkdir chart_imade
mkdir calib_image
mkdir undist_image
mkdir tmp