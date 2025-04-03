# Edmonton (v0.2)

This project is a web application for managing user profiles and handling student requests such as medical withdrawals.

## Setup Instructions

### Option 1: Local Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/Edmonton.git
   cd Edmonton
   ```

2. **Install required packages:**
   ```sh
   pip install -r requirements.txt
   ```

   **This command installs**:
   - **Flask**: The web framework.
   - **flask_sqlalchemy**: An ORM for working with databases.
   - **O365**: A library for integrating with Microsoft Office 365.
   - **werkzeug**: Provides security utilities like password hashing.

3. **Fill in the configuration file (config.py):**
   Keys are for O365 authentication.
   Get your keys from: https://learn.microsoft.com/en-us/entra/fundamentals/entra-admin-center
   ```python
   client_id = 'your_client_id'
   client_secret = 'your_client_secret'
   SECRET_KEY = 'your_secret_key'
   ```

4. **Run the application:**
   ```sh
   python migrations.py
   python main.py
   ```

5. **Open in your web browser:**
   After running "python main.py" in your command terminal, visit: http://127.0.0.1:5000

### Option 2: Docker Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/Edmonton.git
   cd Edmonton
   ```

2. **Configure your application:**
   Edit the config.py file with your O365 keys:
   ```python
   client_id = 'your_client_id'
   client_secret = 'your_client_secret'
   SECRET_KEY = 'your_secret_key'
   ```

3. **Build and start the Docker container:**
   ```sh
   docker-compose up -d
   ```

4. **Access the application:**
   Open your browser and visit: http://localhost:5000

5. **To stop the container:**
   ```sh
   docker-compose down
   ```

## v0.2 Features

- User authentication and profile management
- Admin dashboard for user management
- Medical/Administrative withdrawal request submission and processing
- Student-initiated course drop requests
- PDF generation for official documentation
- Document upload capabilities
- **New in v0.2:** Docker support for easy deployment

## Project Structure

- `main.py`: Main application file
- `migrations.py`: Database migration script
- `authentication.py`: O365 authentication handling
- `pdf_utils.py`: Utilities for PDF generation
- `templates/`: HTML templates
- `static/`: Static assets (CSS, JavaScript, images)
- `Dockerfile` & `docker-compose.yml`: Docker configuration

## Contributors

Team Members: Niket Gupta, Joseph Mascardo, John Gleiter, Alexis Alejandro