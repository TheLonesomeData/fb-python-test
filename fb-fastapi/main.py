from fastapi import FastAPI, status
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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


# Create tables
Base.metadata.create_all(bind=engine)


# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# FastAPI app
app = FastAPI(
    title="FastAPI Boilerplate",
    description="A simple FastAPI application with SQLite integration",
)


@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    """Health check endpoint to verify the service is running."""
    return {"status": "healthy", "message": "Service is up and running"}
