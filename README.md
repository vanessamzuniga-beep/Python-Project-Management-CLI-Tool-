# Python Project Management CLI Tool

## Overview

A Python-based Command-Line Interface (CLI) application that manages a simulated multi-user project tracker system. The application allows users to create and manage users, projects, and tasks, persist data locally with file I/O, organize code with classes and modules, and integrate an external service.

## Technologies

- Python 3.8
- Object-oriented programming
- `argparse` for command-line argument parsing
- `requests` for HTTP requests
- JSON for data persistence
- Pipenv for dependency management
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/) for sample API data

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/vanessamzuniga-beep/Python-Project-Management-CLI-Tool-.git
cd Python-Project-Management-CLI-Tool-
```

Install the project dependencies:

```bash
pipenv install
```

Run the application through Pipenv:

```bash
pipenv run python main.py --help
```

## Data Storage

Application data is stored in `data/project_data.json`. Users, projects, and their tasks are serialized to JSON and loaded when commands run.

## Error Handling

The application reports errors for invalid users, projects, and tasks. API request failures are caught and displayed as readable error messages.

## Project Structure

```text
summative/
├── main.py
├── models/
│   ├── user.py
│   ├── project.py
│   └── task.py
├── services/
│   ├── api_client.py
│   └── storage_service.py
├── utils/
├── data/
│   └── project_data.json
├── Pipfile
├── Pipfile.lock
├── requirements.txt
└── README.md
```

## Dependencies

The project uses `requests` for external API communication. Dependencies are declared in `Pipfile` and locked in `Pipfile.lock`. `requirements.txt` also lists the `requests` dependency.
