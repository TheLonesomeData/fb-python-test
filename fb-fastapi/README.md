# FastAPI Application

A simple FastAPI application with SQLite database integration.

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
   uvicorn main:app --reload
   ```

5. Access the application:
   - API: `http://127.0.0.1:8000/health`
   - Interactive API documentation: `http://127.0.0.1:8000/docs`
   - Alternative API documentation: `http://127.0.0.1:8000/redoc`

## Features

- Health check endpoint
- SQLAlchemy integration with SQLite
- Interactive API documentation (Swagger UI and ReDoc)

## API Endpoints

- `GET /health` - Health check endpoint that returns service status

## Database

The application uses SQLite with SQLAlchemy. The database file (`fastapi.db`) will be created automatically when you first run the application.

## Project Structure

- `main.py` - Main application file with FastAPI app, routes, and models
- `requirements.txt` - Project dependencies
- `fastapi.db` - SQLite database (created on first run) 