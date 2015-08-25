#!/bin/sh

BASE_DIR=`dirname $0`
VENV_DIR=$BASE_DIR/../vrfy_env

source $VENV_DIR/bin/activate

$VENV_DIR/bin/gunicorn vrfy.wsgi:application
