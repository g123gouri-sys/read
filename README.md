# Hello Project

A basic Python project with a command-line interface and tests.

## Setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the project in editable mode:

```powershell
python -m pip install -e ".[dev]"
```

## Run

```powershell
python -m hello_project
python -m hello_project Gouri
```

## Test

```powershell
python -m pytest
```
