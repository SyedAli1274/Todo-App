"""
TodoService for business logic of the in-memory console application.
"""
from typing import List, Optional
from ..models.todo import Todo, TodoList


class TodoService:
    """
    Service class that handles all business logic for todo operations.
    """

    def __init__(self):
        """
        Initialize the TodoService with a TodoList collection.
        """
        self.todo_list = TodoList()

    def create_todo(self, title: str, description: str = "") -> Todo:
        """
        Create a new todo item.

        Args:
            title: Required title of the new todo
            description: Optional description of the new todo

        Returns:
            The newly created Todo object

        Raises:
            ValueError: If title is empty or None
        """
        return self.todo_list.add_todo(title, description)

    def list_todos(self) -> List[Todo]:
        """
        Retrieve all todo items.

        Returns:
            List of all Todo objects
        """
        return self.todo_list.list_todos()

    def update_todo(self, todo_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update an existing todo item.

        Args:
            todo_id: ID of the todo to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            True if update was successful, False if todo not found

        Raises:
            ValueError: If title is empty or None
        """
        return self.todo_list.update_todo(todo_id, title, description)

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo item by its ID.

        Args:
            todo_id: ID of the todo to delete

        Returns:
            True if deletion was successful, False if todo not found
        """
        return self.todo_list.delete_todo(todo_id)

    def mark_complete(self, todo_id: int) -> bool:
        """
        Mark a todo as completed.

        Args:
            todo_id: ID of the todo to mark as complete

        Returns:
            True if update was successful, False if todo not found
        """
        return self.todo_list.mark_complete(todo_id)

    def mark_incomplete(self, todo_id: int) -> bool:
        """
        Mark a todo as incomplete.

        Args:
            todo_id: ID of the todo to mark as incomplete

        Returns:
            True if update was successful, False if todo not found
        """
        return self.todo_list.mark_incomplete(todo_id)

    def get_todo(self, todo_id: int) -> Optional[Todo]:
        """
        Retrieve a specific todo by its ID.

        Args:
            todo_id: ID of the todo to retrieve

        Returns:
            Todo object if found, None otherwise
        """
        return self.todo_list.get_todo(todo_id)