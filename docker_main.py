# Docker-specific entry point for Edmonton application
# This ensures Flask binds to '0.0.0.0' when running in Docker

from main import app, db

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    # This is the crucial part - binding to '0.0.0.0'
    # so the app is accessible outside the container
    app.run(host='0.0.0.0', port=5000)