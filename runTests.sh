#!/bin/sh

BASE_DIR=$(dirname $0)

export PYTHONPATH=$BASE_DIR/src/main/python:$BASE_DIR/src/test/python:$PYTHONPATH

python $BASE_DIR/src/test/python/versioned/version_tests.py -v
