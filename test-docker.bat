@echo off
echo Edmonton Docker Test Script
echo ==========================
echo.

echo 1. Building Docker image...
docker build -t edmonton .
if %ERRORLEVEL% neq 0 (
    echo ERROR: Docker build failed.
    exit /b 1
)
echo Docker image built successfully.
echo.

echo 2. Creating a test container...
for /f "tokens=*" %%i in ('docker run -d -p 5000:5000 edmonton') do set CONTAINER_ID=%%i
if %ERRORLEVEL% neq 0 (
    echo ERROR: Failed to start Docker container.
    exit /b 1
)
echo Container started with ID: %CONTAINER_ID%
echo.

echo 3. Waiting for application to start (10 seconds)...
timeout /t 10 /nobreak > nul
echo.

echo 4. Checking container logs for errors...
docker logs %CONTAINER_ID%
echo.

echo 5. Stopping and removing test container...
docker stop %CONTAINER_ID%
docker rm %CONTAINER_ID%
echo.

echo Test completed.
echo.
echo If you want to run the application, use:
echo docker run -p 5000:5000 edmonton
echo or
echo docker-compose up