#!/bin/sh

cd /usr/src/app/db/alembic
alembic revision --autogenerate
