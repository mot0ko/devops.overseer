#!/bin/bash

rm -rf ./build
rm -rf ./dist

pip install -r requirements.dev.txt
pip install -r requirements.txt

python3 -m build
