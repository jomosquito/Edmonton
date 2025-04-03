#!/bin/bash
echo "Starting Edmonton Docker Container"
echo "================================"
echo

echo "1. Building Docker image..."
docker build -t edmonton .
if [ $? -ne 0 ]; then
    echo "ERROR: Docker build failed."
    exit 1
fi
echo "Docker image built successfully."
echo

echo "2. Running container in foreground mode..."
echo "(Press Ctrl+C to stop)"
echo
docker run -it --rm -p 5000:5000 -v "$(pwd)/config.py:/app/config.py" -v "$(pwd)/instance:/app/instance" edmonton

echo
echo "Container stopped."