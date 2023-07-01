#!/bin/sh

echo "Creating DB"

mysql -h$DB_ENDPOINT -u$MARIADB_USER -p$MARIADB_PASSWORD -e \
"CREATE DATABASE IF NOT EXISTS  ${MARIADB_DATABASE} /*\!40100 DEFAULT CHARACTER SET utf8 */;"; \
echo "without SSL"; \


echo "Start migrations"

alembic upgrade head