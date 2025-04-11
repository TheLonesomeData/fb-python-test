# Flask Application with SQLAlchemy

A simple Flask application with SQLAlchemy and SQLite integration.

## Setup

1. Set up Python 3.10.7 (required) using pyenv:
   ```
   # Install pyenv (macOS)
   brew install pyenv

   # Install Python 3.10.7
   pyenv install 3.10.7

   # Set Python 3.10.7 for this project
   pyenv local 3.10.7

   # Verify the Python version
   python --version  # Should show Python 3.10.7
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python app.py
   ```

4. Test the health check endpoint: `http://127.0.0.1:5000/health`

## Features

- Health check endpoint
- SQLAlchemy integration with SQLite

## API Endpoints

- `GET /health` - Health check endpoint that returns service status

## Database

The application uses SQLite with Flask-SQLAlchemy. The database file (`blog.db`) will be created automatically when you first run the application, although it doesn't contain any data in this simplified version.

## Project Structure

- `app.py` - Main application file with routes and models
- `requirements.txt` - Project dependencies
- `blog.db` - SQLite database (created on first run) 