#!/usr/bin/env bash

set -Eeuo pipefail

psql -v ON_ERROR_STOP=1 -U postgres <<-EOSQL
  CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';
  ALTER ROLE $DB_USER SET client_encoding TO 'UTF8';
  ALTER ROLE $DB_USER SET TIMEZONE TO '$DB_TIME_ZONE';
  ALTER ROLE $DB_USER CREATEDB;
  CREATE DATABASE $DB_NAME OWNER $DB_USER;
  GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;
EOSQL
