# This code sets up the SQLAlchemy database connection and ORM base class for your project:

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./todo.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# Creates a database engine for connecting to SQLite

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Factory for creating new database sessions (used for interacting with the DB)

Base = declarative_base()
# Base class for your ORM models (all models should inherit from this)