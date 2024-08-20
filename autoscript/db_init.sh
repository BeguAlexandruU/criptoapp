#!/bin/bash

PATH_DB="../back/database/"
PATH_ALEMBIC="../back/cripto-app/cripto_app/alembic"
PATH_MIGRATION="../back/cripto-app/cripto_app"

PATH_ORIGIN=$(pwd)

## drop tables from db

# change dir to db path
cd $PATH_DB

# Execută comanda în containerul MySQL
DB_HOST="localhost"
DB_PORT="3306"
DB_NAME="mydb"
DB_USER="sandu"
DB_PASSWORD="begu"

# Comanda pentru a verifica numărul de tabele în baza de date
CHECK_TABLES_SQL="SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = '${DB_NAME}';"

# Comanda pentru a șterge toate tabelele din baza de date
DROP_TABLES_SQL="SET FOREIGN_KEY_CHECKS = 0; SELECT CONCAT('DROP TABLE IF EXISTS \`', table_schema, '\`.\`', table_name, '\`;') FROM information_schema.tables WHERE table_schema = '${DB_NAME}'; SET FOREIGN_KEY_CHECKS = 1;"

# Conectarea la baza de date și verificarea numărului de tabele
TABLE_COUNT=$(docker compose exec -T db mysql -u"${DB_USER}" -p"${DB_PASSWORD}" -h "${DB_HOST}" -P "${DB_PORT}" -se"${CHECK_TABLES_SQL}")

# Verifică dacă există tabele în baza de date
if [ "$TABLE_COUNT" -gt 0 ]; then
  echo "Există $TABLE_COUNT tabele. Se începe ștergerea..."
  # Generarea și executarea comenzilor de ștergere a tabelului
  docker compose exec -T db mysql -u"${DB_USER}" -p"${DB_PASSWORD}" -h "${DB_HOST}" -P "${DB_PORT}" -se"${DROP_TABLES_SQL}" | docker compose exec -T db mysql -u"${DB_USER}" -p"${DB_PASSWORD}" -h "${DB_HOST}" -P "${DB_PORT}" "${DB_NAME}"
  echo "Toate tabelele au fost șterse."
else
  echo "Nu există tabele de șters."
fi

cd $PATH_ORIGIN
##

## remove files from alembic
cd $PATH_ALEMBIC

rm -r versions/*
rm -r __pycache__

cd $PATH_ORIGIN
##

##generate new migration

source ../back/env/bin/activate

cd $PATH_MIGRATION

poetry run alembic revision --autogenerate -m 'revision migration'
poetry run alembic upgrade head

deactivate
cd $PATH_ORIGIN
##