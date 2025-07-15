# 🗂️ FastAPI Task Manager

A lightweight and async Task Manager API using **FastAPI**, **PostgreSQL**, **SQLAlchemy (async)**, and **Alembic**.

## 🚀 Features

- JWT-based user authentication
- CRUD APIs for Users, Projects, and Tasks
- Asynchronous DB access using `asyncpg`
- Database migrations via Alembic
- Swagger UI docs at `/docs`

## 🔧 Setup

git clone https://github.com/yourusername/fastapi-task-manager.git
cd fastapi-task-manager
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
fastapi dev app/main.py
