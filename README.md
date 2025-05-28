# 🏋️‍♀️ Fitness Tracker CLI

A simple command-line fitness tracker built with Python, SQLAlchemy ORM, and SQLite.

## Features

- Manage users
- Log workout sessions
- Track health metrics (weight, blood pressure, heart rate, sleep)
- View and delete data via a CLI interface

## Tech Stack

- Python 3.8
- SQLAlchemy
- Alembic
- SQLite
- Pipenv

## Setup

```bash
pipenv install
pipenv shell
alembic upgrade head
python lib/db/seed.py
python lib/cli.py
