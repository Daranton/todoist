import typer
import requests
from typing import Optional

app = typer.Typer()
API_URL = "https://localhost:8443/tasks"

# For dev, ignore SSL warnings (remove verify=False in prod)
requests.packages.urllib3.disable_warnings()

@app.command()
def add(title: str, description: Optional[str] = None):
    """Add a new task."""
    data = {"title": title}
    if description:
        data["description"] = description
    response = requests.post(API_URL + "/", json=data, verify=False)
    if response.status_code == 200 or response.status_code == 201:
        typer.echo(f"Task added: {response.json()['id']} - {response.json()['title']}")
    else:
        typer.echo(f"Failed to add task: {response.text}")

@app.command()
def list():
    """List all tasks."""
    response = requests.get(API_URL + "/", verify=False)
    if response.status_code == 200:
        tasks = response.json()
        if not tasks:
            typer.echo("No tasks found.")
            return
        for task in tasks:
            status = "✅" if task["completed"] else "❌"
            typer.echo(f"{task['id']}: {task['title']} {status}")
            if task.get("description"):
                typer.echo(f"   {task['description']}")
    else:
        typer.echo(f"Failed to fetch tasks: {response.text}")

@app.command()
def done(task_id: int):
    """Mark a task as completed."""
    data = {"completed": True}
    response = requests.put(f"{API_URL}/{task_id}", json=data, verify=False)
    if response.status_code == 200:
        typer.echo(f"Task {task_id} marked as done.")
    else:
        typer.echo(f"Failed to update task: {response.text}")

@app.command()
def delete(task_id: int):
    """Delete a task."""
    response = requests.delete(f"{API_URL}/{task_id}", verify=False)
    if response.status_code == 200:
        typer.echo(f"Task {task_id} deleted.")
    else:
        typer.echo(f"Failed to delete task: {response.text}")

if __name__ == "__main__":
    app()
