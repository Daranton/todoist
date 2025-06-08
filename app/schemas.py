# Pydantic schemas are for data validation, serialization and documentation.
# Data validation - check input data is correct, complete, meets rules. 
# Serialization - convert models into JSON-safe data structure for response.
# Documentation - API docs from schemas & routes
from pydantic import BaseModel, Field
from typing import Optional

class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="Title")
    description: Optional[str] = Field(None, max_length=500, description="Optional task details")

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class Task(TaskBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True
