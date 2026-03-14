# Todoist

A simple Todo List API built with FastAPI and SQLite, with a Python CLI client, MCP server integration for AI assistants, and Claude Code skills for natural-language task management.

---

## Features

- REST API with full CRUD for tasks (FastAPI)
- SQLite database with automatic migrations (Alembic)
- Python CLI to manage tasks from the terminal (Typer)
- MCP server so AI assistants (e.g. Claude) can manage tasks directly
- Claude Code skills (brain-dump, triage) built on top of MCP for higher-level task workflows
- Local skill marketplace bundled in `.claude/marketplace/`
- Docker support

---

## Quickstart

### 1. Clone the repository

```bash
git clone https://github.com/Daranton/todoist.git
cd todoist
```

### 2. Install dependencies

Requires **Python 3.12+**.

```bash
pip install -r requirements.txt
```

### 3. Run the API

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The database and tables are created automatically on first run.

API available at: `http://localhost:8000`
Interactive docs at: `http://localhost:8000/docs`

### 4. (Optional) Run with HTTPS

Generate a self-signed certificate:

```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=localhost"
```

Then start with SSL:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8443 --ssl-keyfile=key.pem --ssl-certfile=cert.pem
```

---

## CLI Usage

Open a second terminal and use the CLI to interact with the API:

```bash
# Add a task
python cli/todo.py add "Buy groceries" --description "Milk, eggs, bread"

# List all tasks
python cli/todo.py list

# Mark a task as done
python cli/todo.py done 1

# Delete a task
python cli/todo.py delete 1
```

---

## MCP Server (Claude / AI Assistants)

The project includes an MCP server so Claude Code or other MCP-compatible AI assistants can manage tasks directly.

A `.mcp.json` file is included in the repository — Claude Code picks it up automatically when you open the project.

To connect manually in Claude Code, run `/mcp` and select `todoist`.

The MCP server runs migrations and initializes the database automatically on startup.

Available tools:
- `list_tasks` — list all tasks
- `create_task` — create a new task
- `complete_task` — mark a task as completed
- `delete_task` — delete a task by ID

---

## Claude Code Skills

On top of the MCP server, this project ships a local skill marketplace with higher-level task workflows you can invoke directly from Claude Code.

Skills are located in `.claude/marketplace/plugins/todoist-skills/skills/`.

### Available skills

| Skill | Command | Description |
|-------|---------|-------------|
| `brain-dump` | `/brain-dump <freeform text>` | Parse a messy list of thoughts and bulk-create tasks |
| `triage` | `/triage` | Review all tasks, group by urgency, and clean up stale ones |

Skills call the MCP tools under the hood — the API must be running when you use them.

### Installing the marketplace

The marketplace is pre-configured in `.claude/marketplace/`. Claude Code picks it up automatically when you open the project. If you need to register it manually, point Claude Code at `.claude/marketplace` as a local marketplace source.

---

## Docker

```bash
docker-compose up --build
```

Migrations run automatically before the server starts. No manual setup required.

---

## Running Tests

```bash
pytest
```

---

## Project Structure

```
todoist/
├── app/
│   ├── main.py           # FastAPI app
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas
│   ├── crud.py           # DB operations
│   ├── database.py       # DB setup
│   └── mcp_server.py     # MCP server
├── alembic/
│   └── versions/         # Migration files
├── cli/
│   └── todo.py           # Typer CLI
├── tests/
│   ├── test_crud.py
│   └── test_todo.py
├── .claude/
│   └── marketplace/
│       ├── .claude-plugin/
│       │   └── marketplace.json   # Local marketplace definition
│       └── plugins/
│           └── todoist-skills/
│               ├── .claude-plugin/
│               │   └── plugin.json
│               └── skills/
│                   ├── brain-dump/SKILL.md
│                   └── triage/SKILL.md
├── .mcp.json             # MCP server config
├── docker-compose.yml
├── requirements.txt
└── alembic.ini
```

---

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DATABASE_URL` | `sqlite:///./todo.db` | SQLAlchemy database URL |

---

## License

MIT License — Copyright 2025-present Daranton
