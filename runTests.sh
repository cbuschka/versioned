#!/bin/sh

BASE_DIR=$(dirname $0)

export PYTHONPATH=$BASE_DIR/src/main/python:$BASE_DIR/src/test/python:$PYTHONPATH

coverage run -m unittest discover -s $BASE_DIR/src/test/python/versioned -v -p '*_test?.py'
