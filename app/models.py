# SQLAlchemy Model - DB structure + storage
# Allowed only low-level constraints (nullable, unique)

from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

# These should not be used for validation.
# SQLAlchemy Models. Their role is to map Python objects to database tables.

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    due_date = Column(String, nullable=True)
