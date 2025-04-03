FROM python:3.9-slim

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

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

# Run migrations and then the application
CMD ["sh", "-c", "python migrations.py && python main.py"]