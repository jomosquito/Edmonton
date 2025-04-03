FROM python:3.9-slim

WORKDIR /app

# Copy requirements file first to leverage Docker cache
COPY requirements-docker.txt /app/

# Install requirements
RUN pip install --no-cache-dir -r requirements-docker.txt

# Now copy the rest of the application
COPY . /app/

# Create necessary directories
RUN mkdir -p static/pdfs static/temp static/uploads/documentation static/uploads/signatures instance

# Expose port 5000
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

# Create an empty config.py file (will be overwritten at runtime)
RUN echo "client_id = 'your_client_id'" > config.py && \
    echo "client_secret = 'your_client_secret'" >> config.py && \
    echo "SECRET_KEY = 'your_secret_key'" >> config.py

# Run entrypoint script
COPY docker-entrypoint.sh /app/
RUN chmod +x /app/docker-entrypoint.sh
CMD ["/app/docker-entrypoint.sh"]