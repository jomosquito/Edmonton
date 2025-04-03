@echo off
echo Edmonton Docker Debug Script
echo =========================
echo.

echo 1. Stopping any existing containers...
docker-compose down
echo.

echo 2. Building fresh Docker image...
docker-compose build --no-cache
if %ERRORLEVEL% neq 0 (
    echo ERROR: Docker build failed.
    exit /b 1
)
echo Docker image built successfully.
echo.

echo 3. Starting container in interactive mode...
echo Running docker-compose up (press Ctrl+C to stop when done)
echo.
docker-compose up

echo.
echo Debug session ended.