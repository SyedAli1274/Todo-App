# Todo In-Memory Python Console Application

A simple console-based todo application that runs entirely in memory with no persistent storage. This application allows users to create, list, update, mark complete, and delete todo items through a clean command-line interface.

## Features

- Create new todo items with title and optional description
- List all todos with ID, title, completion status, and description
- Mark todos as completed
- Update existing todo items
- Delete todo items
- Clean console interface with menu-driven navigation

## Requirements

- Python 3.x
- No external dependencies (uses only Python standard library)

## Usage

To run the application:

```bash
python src/cli/main.py
```

The application will present a menu with options to create, list, update, mark complete, or delete todos. Follow the on-screen prompts to interact with the application.

## Architecture

The application follows a clean architecture pattern with:

- **Models** (`src/models/`): Data models and collections
- **Services** (`src/services/`): Business logic and operations
- **CLI** (`src/cli/`): Console interface and user interaction
- **Lib** (`src/lib/`): Utility functions and helpers