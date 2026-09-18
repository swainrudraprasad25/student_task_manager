# Student Task Manager

A REST API for managing student tasks, built with FastAPI and MySQL.

## Tech Stack
Python · FastAPI · MySQL · Pydantic

## Features
- Create, view, update, and delete tasks

## Setup
```bash
git clone https://github.com/swainrudraprasad25/student-task-manager.git
cd student-task-manager
python -m venv myproject
myproject\Scripts\activate
pip install fastapi uvicorn mysql-connector-python 
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/docs` for API docs.

## Database Schema
```sql
CREATE TABLE task (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL
);
```
