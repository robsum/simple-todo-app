#!/bin/sh

# Wait for the PostgreSQL database to be ready
# Replace <db-host> with your database host and <db-port> with the database port
until sshpass -p mypassword psql -h db -p 5432 -U myuser -d mydatabase -c '\l' -W; do
  echo "Waiting for PostgreSQL to start..."
  sleep 1
done

# Check if the database already exists
if psql -h db -p 5432 -U myuser -d mydatabase -lqt | cut -d \| -f 1 | grep -qw mydatabase; then
  echo "Database already exists, no need to initialize."
else
  # Create the database
  psql -h db -p 5432 -U myuser -d mydatabase -c "CREATE DATABASE todo"

  # Apply database migrations or other initialization steps
  # Replace this with the actual command you use for database initialization
  # For example, using Alembic for SQLAlchemy:
  # alembic upgrade head

  echo "Database initialized successfully."
fi

# Start your actual application
exec "$@"

