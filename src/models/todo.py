"""
Todo data model and TodoList collection for the in-memory console application.
"""

from typing import List, Optional, Dict, Any
from datetime import datetime


class Todo:
    """
    Represents a single todo item with id, title, description, and completion status.
    """

    def __init__(self, id: int, title: str, description: str = "", completed: bool = False):
        """
        Initialize a Todo item.

        Args:
            id: Unique identifier for the todo
            title: Required title of the todo
            description: Optional description of the todo
            completed: Boolean indicating if the todo is completed (default: False)
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty or None")

        self.id = id
        self.title = title.strip()
        self.description = description.strip() if description else ""
        self.completed = completed
        self.created_at = datetime.now()

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the Todo object to a dictionary representation.

        Returns:
            Dictionary with all todo properties
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at.isoformat()
        }

    def __str__(self) -> str:
        """
        String representation of the Todo item.

        Returns:
            Formatted string with todo details
        """
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.id}. {self.title} - {self.description}"


class TodoList:
    """
    Collection class for managing multiple Todo items.
    """

    def __init__(self):
        """
        Initialize an empty TodoList with next_id counter.
        """
        self.todos: List[Todo] = []
        self.next_id = 1

    def add_todo(self, title: str, description: str = "") -> Todo:
        """
        Add a new Todo to the collection with unique ID.

        Args:
            title: Required title of the new todo
            description: Optional description of the new todo

        Returns:
            The newly created Todo object
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty or None")

        todo = Todo(self.next_id, title, description)
        self.todos.append(todo)
        self.next_id += 1
        return todo

    def get_todo(self, todo_id: int) -> Optional[Todo]:
        """
        Retrieve a Todo by its ID.

        Args:
            todo_id: ID of the todo to retrieve

        Returns:
            Todo object if found, None otherwise
        """
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def update_todo(self, todo_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update an existing Todo by its ID.

        Args:
            todo_id: ID of the todo to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            True if update was successful, False if todo not found
        """
        todo = self.get_todo(todo_id)
        if not todo:
            return False

        if title is not None:
            if not title or not title.strip():
                raise ValueError("Title cannot be empty or None")
            todo.title = title.strip()

        if description is not None:
            todo.description = description.strip() if description else ""

        return True

    def delete_todo(self, todo_id: int) -> bool:
        """
        Remove a Todo by its ID.

        Args:
            todo_id: ID of the todo to delete

        Returns:
            True if deletion was successful, False if todo not found
        """
        for i, todo in enumerate(self.todos):
            if todo.id == todo_id:
                del self.todos[i]
                return True
        return False

    def list_todos(self) -> List[Todo]:
        """
        Return all Todo items in the collection.

        Returns:
            List of all Todo objects
        """
        return self.todos.copy()

    def mark_complete(self, todo_id: int) -> bool:
        """
        Update the completion status of a Todo by its ID.

        Args:
            todo_id: ID of the todo to mark as complete

        Returns:
            True if update was successful, False if todo not found
        """
        todo = self.get_todo(todo_id)
        if not todo:
            return False

        todo.completed = True
        return True

    def mark_incomplete(self, todo_id: int) -> bool:
        """
        Update the completion status of a Todo by its ID to incomplete.

        Args:
            todo_id: ID of the todo to mark as incomplete

        Returns:
            True if update was successful, False if todo not found
        """
        todo = self.get_todo(todo_id)
        if not todo:
            return False

        todo.completed = False
        return True