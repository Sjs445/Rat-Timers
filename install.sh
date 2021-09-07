#!/bin/sh
DIR="$( cd "$( dirname "$0" )" && pwd )"
pip install -r "$DIR/requirements.txt"
pip3 install -r "$DIR/requirements.txt"
