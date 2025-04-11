# Django Application

A simple Django application with SQLite database integration.

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

4. Run database migrations (if needed):
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000`

## Features

- Basic Django project structure
- SQLite database integration
- Admin interface (accessible at `/admin/`)

## Management Commands

- `python manage.py runserver` - Start the development server
- `python manage.py migrate` - Apply database migrations
- `python manage.py makemigrations` - Create new migrations based on model changes
- `python manage.py createsuperuser` - Create an admin user

## Project Structure

- `manage.py` - Django's command-line utility for administrative tasks
- `app/` - Main application directory containing Django project settings
- `blog/` - Example app directory
- `db.sqlite3` - SQLite database file 