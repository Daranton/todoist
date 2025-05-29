# FastAPI Todo CLI

A simple Todo List backend API built with FastAPI, combined with a Python CLI client using Typer to manage tasks via the command line.

---

## Features

- **FastAPI REST API** with full CRUD for tasks
- **SQLite** database backend for local storage
- **HTTPS support** with self-signed certificates (for development)
- **Python CLI** powered by Typer to add, list, update, and delete tasks
- Tasks have `title`, `description`, and `completed` status

---

## Getting Started

### Prerequisites

- Python 3.9+
- [Poetry](https://python-poetry.org/) or `pip` for dependencies
- OpenSSL (to generate self-signed certs for HTTPS, optional)

### Installation

1. Clone this repository:

    git clone https://github.com/Daranton/todoist.git
    cd todoist

2. Install dependencies:

    pip install -r requirements.txt

3. (Optional) Generate self-signed SSL certs:

    openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=localhost"

Running the Backend API

Start the FastAPI server with HTTPS enabled:

    uvicorn app.main:app --host 0.0.0.0 --port 8443 --ssl-keyfile=key.pem --ssl-certfile=cert.pem
    The API will be available at: https://localhost:8443

    For development without HTTPS, run:
        uvicorn app.main:app --host 0.0.0.0 --port 8000

Using the CLI Client

Open a new terminal in IDE and run:

    python cli/todo.py --help

Common commands

Add a task:
    python cli/todo.py add "Buy groceries" --description "Milk, eggs, bread"

List all tasks:
    python cli/todo.py list

Mark a task as done:
    python cli/todo.py done 1

Delete a task:
    python cli/todo.py delete 1

Update a task (title, description, completed):
    python cli/todo.py update 1 --title "New title" --completed true

Project Structure

fastapi-todo-cli/
├── app/
│   ├── main.py           # FastAPI app
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas
│   ├── crud.py           # DB operations
│   └── database.py       # DB setup
├── cli/
│   └── todo.py           # Typer CLI commands
├── tests/
│   ├── test_todo.py      # Todo test
│   └── test_crud.py      # Crud test
├── requirements.txt      # Python dependencies
├── cert.pem              # SSL cert (optional)
├── key.pem               # SSL key (optional)
└── README.md

License

MIT License