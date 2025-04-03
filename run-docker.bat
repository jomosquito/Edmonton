@echo off
echo Starting Edmonton Docker Container
echo ================================
echo.

echo 1. Building Docker image...
docker build -t edmonton .
if %ERRORLEVEL% neq 0 (
    echo ERROR: Docker build failed.
    exit /b 1
)
echo Docker image built successfully.
echo.

echo 2. Running container in foreground mode...
echo (Press Ctrl+C to stop)
echo.
docker run -it --rm -p 5000:5000 -v %cd%/config.py:/app/config.py -v %cd%/instance:/app/instance edmonton

echo.
echo Container stopped.