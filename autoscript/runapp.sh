#!/bin/bash

PATH_APP="../back/cripto-app"

source ../back/env/bin/activate

cd $PATH_APP

PATTERN='^[0-9]+$'

if [[ $1 =~ $PATTERN ]]
then
    poetry run uvicorn cripto_app.main:app --workers $1 --host 0.0.0.0 --port 5001
else
    poetry run uvicorn cripto_app.main:app --reload --host 0.0.0.0 --port 5001
fi

deactivate