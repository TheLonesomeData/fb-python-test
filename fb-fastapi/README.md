# FastAPI Application

A simple FastAPI application with SQLite database integration.

## Setup

1. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   uvicorn main:app --reload
   ```

4. Access the application:
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