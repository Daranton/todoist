import pytest
from typer.testing import CliRunner
from cli.todo import app

runner = CliRunner()

def test_add_and_list_task():
    result = runner.invoke(app, ["add", "CLI test task", "--description", "desc"])
    assert result.exit_code == 0
    assert "Task added" in result.output

    result = runner.invoke(app, ["list"])
    assert result.exit_code == 0
    assert "CLI test task" in result.output

def test_done_and_delete():
    # Add task
    result = runner.invoke(app, ["add", "Task to complete"])
    assert result.exit_code == 0
    # Extract ID from output
    import re
    match = re.search(r"Task added with ID: (\d+)", result.output)
    task_id = int(match.group(1))

    # Mark done
    result = runner.invoke(app, ["done", str(task_id)])
    assert result.exit_code == 0
    assert f"Task {task_id} marked as done" in result.output

