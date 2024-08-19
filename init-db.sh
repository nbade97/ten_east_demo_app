#!/bin/bash
set -e

# Restore the database from the dump file
pg_restore -U postgres -d postgres /docker-entrypoint-initdb.d/db_backup.dump

# Execute the original entrypoint script
exec docker-entrypoint.sh "$@"