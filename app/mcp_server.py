import os
from alembic.config import Config
from alembic import command
from mcp.server.fastmcp import FastMCP
from app.database import SessionLocal
from app import crud, schemas

def _run_migrations():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    alembic_cfg = Config(os.path.join(base_dir, "alembic.ini"))
    command.upgrade(alembic_cfg, "head")

_run_migrations()

mcp = FastMCP("todoist")


def _task_to_dict(task) -> dict:
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed,
    }


@mcp.tool()
def create_task(title: str, description: str = None) -> str:
    """Create a new task."""
    db = SessionLocal()
    try:
        task = crud.create_task(db, schemas.TaskCreate(title=title, description=description))
        return str(_task_to_dict(task))
    finally:
        db.close()


@mcp.tool()
def list_tasks() -> str:
    """List all tasks."""
    db = SessionLocal()
    try:
        tasks = crud.get_tasks(db)
        return str([_task_to_dict(t) for t in tasks])
    finally:
        db.close()


@mcp.tool()
def complete_task(task_id: int) -> str:
    """Mark a task as completed."""
    db = SessionLocal()
    try:
        task = crud.update_task(db, task_id, schemas.TaskUpdate(completed=True))
        if task is None:
            return f"Task {task_id} not found."
        return str(_task_to_dict(task))
    finally:
        db.close()


@mcp.tool()
def delete_task(task_id: int) -> str:
    """Delete a task by ID."""
    db = SessionLocal()
    try:
        task = crud.delete_task(db, task_id)
        if task is None:
            return f"Task {task_id} not found."
        return f"Deleted task {task_id}: {task.title}"
    finally:
        db.close()


if __name__ == "__main__":
    mcp.run()
