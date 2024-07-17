#!/bin/bash

PATH_DB="../back/database/"
PATH_ALEMBIC="../back/cripto-app/cripto_app/alembic"
PATH_MIGRATION="../back/cripto-app/cripto_app"

PATH_ORIGIN=$(pwd)

## drop tables from db




##


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