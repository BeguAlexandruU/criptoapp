#!/bin/bash

# Așteaptă până când MySQL este gata
echo "Verificarea disponibilității serverului MySQL la $MYSQL_HOST..."
while ! mysqladmin ping -h"$MYSQL_HOST" --silent; do
    echo "Așteptând ca MySQL să fie gata..."
    sleep 2
done
echo "MySQL este gata. Continuarea inițializării."

# Continuă cu scriptul existent
cd cripto_app

alembic revision --autogenerate -m "Initial migration"

alembic upgrade head

cd ..

# poetry run uvicorn cripto_app.main:app --host 0.0.0.0 --port 5001 --reload
poetry run uvicorn cripto_app.main:app --reload --host 0.0.0.0 --port 5001