#!/bin/sh

# Wait for the PostgreSQL database to be ready
# Replace <db-host> with your database host and <db-port> with the database port
until sshpass -p ${POSTGRES_PASSWORD} psql -h db -p 5432 -U ${POSTGRES_USER} -d ${POSTGRES_DB} -c '\l' -W; do
  echo "Waiting for PostgreSQL to start..."
  sleep 1
done

# Check if the database already exists
#if sshpass -p mypassword psql -h db -p 5432 -U myuser -d mydatabase -lqt -W | cut -d \| -f 1 | grep -qw mydatabase; then
#  echo "Database already exists, no need to initialize."
#else
  # Create the database
  sshpass -p ${POSTGRES_PASSWORD} psql -h db -p 5432 -U ${POSTGRES_USER} -d ${POSTGRES_DB} -f /app/create_todo_table.sql -W

  # Apply database migrations or other initialization steps
  # Replace this with the actual command you use for database initialization
  # For example, using Alembic for SQLAlchemy:
  # alembic upgrade head

  echo "Database initialized successfully."
#fi

# Start your actual application
exec "$@"

