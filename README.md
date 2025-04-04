# Python Web Frameworks Interview Project

Welcome to the Python Web Frameworks interview project! This repository contains three simple web applications built with different Python frameworks:
- Django
- Flask
- FastAPI

Each folder includes a minimal boilerplate setup with SQLite database integration. You'll be building functionality on top of one of these frameworks.

## Project Structure

- `fb-django/` - Django implementation
- `fb-flask/` - Flask implementation  
- `fb-fastapi/` - FastAPI implementation

## Your Task

Please choose one of the frameworks and implement a simple blog API with the following requirements:

### Data Models

Create two models:
1. Author
2. BlogPost (which belongs to an Author)

Design the models with appropriate fields that you think would be necessary for a basic blog.

### API Endpoints

Implement the following endpoints:

#### Author Endpoints
- List all authors
- Get a specific author
- Create a new author
- Update an author
- Delete an author

#### BlogPost Endpoints
- List all blog posts
- List all posts by a specific author
- Get a specific post
- Create a new post
- Update a post
- Delete a post

### Stretch Goal

If time allows, add unit tests for some of the endpoints you've implemented. This will help demonstrate your understanding of testing in your chosen framework.

### Framework-Specific Guidelines

#### If using Django
- Use Django REST Framework
- Create appropriate serializers for your models

#### If using Flask
- Use Flask-SQLAlchemy for your models
- Implement JSON responses for your API

#### If using FastAPI
- Use SQLAlchemy for models and Pydantic for schemas
- Implement appropriate response models

## Getting Started

1. Choose your preferred framework
2. Navigate to the corresponding directory
3. Follow the setup instructions in the framework's README.md
4. Implement the required functionality

## What We're Looking For

- Clean, well-organized code
- Proper API design and implementation
- Appropriate error handling
- Good understanding of the chosen framework
- Thoughtful model design
