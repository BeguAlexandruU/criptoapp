#!/bin/bash

PATH_MIGRATION="../back/cripto-app/cripto_app"

PATH_ORIGIN=$(pwd)

##generate new migration

source ../back/env/bin/activate

cd $PATH_MIGRATION

if [ -z "$1" ]
then
    echo "Warning: missing parameter[migration name]"

else
    poetry run alembic revision --autogenerate -m "${1}"
    poetry run alembic upgrade head

fi

cd $PATH_ORIGIN
##

deactivate