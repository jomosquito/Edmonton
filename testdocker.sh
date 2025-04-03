#!/bin/bash
# Test script for Docker deployment of Edmonton

echo "Edmonton Docker Test Script"
echo "=========================="
echo

echo "1. Building Docker image..."
docker build -t edmonton .
if [ $? -ne 0 ]; then
    echo "ERROR: Docker build failed."
    exit 1
fi
echo "Docker image built successfully."
echo

echo "2. Creating a test container..."
CONTAINER_ID=$(docker run -d -p 5000:5000 edmonton)
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to start Docker container."
    exit 1
fi
echo "Container started with ID: $CONTAINER_ID"
echo

echo "3. Waiting for application to start (10 seconds)..."
sleep 10
echo

echo "4. Checking if application is responding..."
if curl -s http://localhost:5000 > /dev/null; then
    echo "SUCCESS: Application is responding."
else
    echo "WARNING: Application is not responding on http://localhost:5000"
fi
echo

echo "5. Checking container logs for errors..."
docker logs $CONTAINER_ID
echo

echo "6. Stopping and removing test container..."
docker stop $CONTAINER_ID
docker rm $CONTAINER_ID
echo

echo "Test completed."
echo
echo "If you want to run the application, use:"
echo "docker run -p 5000:5000 edmonton"
echo "or"
echo "docker-compose up"