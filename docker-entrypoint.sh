#!/bin/bash
set -e

# Create the instance directory if it doesn't exist
mkdir -p /app/instance

# Check if the database file exists
if [ ! -f /app/instance/site.db ]; then
    echo "Database file doesn't exist, creating initial database..."
    # Touch the file to ensure it exists
    touch /app/instance/site.db
fi

# Run migrations
echo "Running database migrations..."
python migrations.py

# Start the application using the Docker-specific entry point
echo "Starting Flask application..."
exec python docker_main.py