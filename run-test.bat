@echo off
echo Running Flask Docker Test
echo =======================
echo.

echo 1. Building test Docker image...
docker build -t edmonton-test -f Dockerfile.test .
if %ERRORLEVEL% neq 0 (
    echo ERROR: Docker build failed.
    exit /b 1
)
echo Test image built successfully.
echo.

echo 2. Running test container...
echo (Press Ctrl+C to stop)
echo.
docker run -it --rm -p 5000:5000 edmonton-test

echo.
echo Test container stopped.
echo.
echo If you saw the hello message in your browser at http://localhost:5000,
echo then Docker networking is working correctly, and the issue is with the main application.