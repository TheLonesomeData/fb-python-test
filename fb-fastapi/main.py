from fastapi import FastAPI, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# SQLAlchemy setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapi.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Example model (won't be used in this simplified version)
class TodoModel(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    completed = Column(Boolean, default=False)


# Author model
class AuthorModel(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)


# Create tables
Base.metadata.create_all(bind=engine)


# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Pydantic models for request/response
class AuthorCreate(BaseModel):
    name: str


class Author(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


# FastAPI app
app = FastAPI(
    title="FastAPI Boilerplate",
    description="A simple FastAPI application with SQLite integration",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    """Health check endpoint to verify the service is running."""
    return {"status": "healthy", "message": "Service is up and running"}


@app.post("/authors", status_code=status.HTTP_201_CREATED, response_model=Author)
@app.post("/authors/", status_code=status.HTTP_201_CREATED, response_model=Author)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    """Create a new author."""
    db_author = AuthorModel(name=author.name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


# get authors

# create blog post

# get blog posts

# get blog post by id
