"""
Main application loop for the Todo In-Memory Console Application.
"""
from typing import Optional
import sys
import os

# Add the src directory to the path to allow imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.services.todo_service import TodoService
from src.lib.utils import (
    validate_todo_title, validate_todo_id, safe_int_input,
    safe_string_input, display_error, display_success, confirm_action
)


class TodoApp:
    """
    Main application class that manages the console interface and user interaction.
    """

    def __init__(self):
        """
        Initialize the TodoApp with a TodoService.
        """
        self.todo_service = TodoService()
        self.running = True

    def display_menu(self):
        """
        Display the main menu options to the user.
        """
        print("\n" + "="*40)
        print("TODO APPLICATION")
        print("="*40)
        print("1. Create new todo")
        print("2. List all todos")
        print("3. Update todo")
        print("4. Mark todo as completed")
        print("5. Delete todo")
        print("6. Exit")
        print("="*40)

    def create_todo(self):
        """
        Handle the create todo functionality.
        """
        print("\n--- Create New Todo ---")
        title = safe_string_input("Enter title: ")

        if not title:
            display_error("Title is required to create a todo.")
            return

        if not validate_todo_title(title):
            display_error("Invalid title. Title cannot be empty.")
            return

        description = safe_string_input("Enter description (optional): ", allow_empty=True)

        try:
            new_todo = self.todo_service.create_todo(title, description or "")
            display_success(f"Todo '{new_todo.title}' created successfully with ID {new_todo.id}")
        except ValueError as e:
            display_error(f"Could not create todo: {str(e)}")

    def list_todos(self):
        """
        Handle the list todos functionality.
        """
        print("\n--- All Todos ---")
        todos = self.todo_service.list_todos()

        if not todos:
            print("No todos found.")
            return

        for todo in todos:
            status = "✓ Completed" if todo.completed else "○ Incomplete"
            print(f"ID: {todo.id} | {status} | {todo.title}")
            if todo.description:
                print(f"     Description: {todo.description}")
            print("-" * 40)

    def update_todo(self):
        """
        Handle the update todo functionality.
        """
        print("\n--- Update Todo ---")
        if not self.todo_service.list_todos():
            display_error("No todos exist to update.")
            return

        todo_id = safe_int_input("Enter the ID of the todo to update: ")

        if not todo_id or not validate_todo_id(todo_id):
            display_error("Invalid todo ID.")
            return

        existing_todo = self.todo_service.get_todo(todo_id)
        if not existing_todo:
            display_error(f"Todo with ID {todo_id} not found.")
            return

        print(f"Updating todo: {existing_todo.title}")

        new_title = safe_string_input(f"Enter new title (current: '{existing_todo.title}'): ", allow_empty=True)
        new_description = safe_string_input(f"Enter new description (current: '{existing_todo.description}'): ", allow_empty=True)

        # If user didn't enter a new title, keep the existing one
        if new_title is None:
            new_title = existing_todo.title

        # If user didn't enter a new description, keep the existing one
        if new_description is None:
            new_description = existing_todo.description

        try:
            success = self.todo_service.update_todo(todo_id, new_title, new_description)
            if success:
                display_success(f"Todo with ID {todo_id} updated successfully.")
            else:
                display_error("Failed to update todo.")
        except ValueError as e:
            display_error(f"Could not update todo: {str(e)}")

    def mark_complete(self):
        """
        Handle the mark todo as completed functionality.
        """
        print("\n--- Mark Todo as Completed ---")
        if not self.todo_service.list_todos():
            display_error("No todos exist to mark as completed.")
            return

        todo_id = safe_int_input("Enter the ID of the todo to mark as completed: ")

        if not todo_id or not validate_todo_id(todo_id):
            display_error("Invalid todo ID.")
            return

        success = self.todo_service.mark_complete(todo_id)
        if success:
            display_success(f"Todo with ID {todo_id} marked as completed.")
        else:
            display_error(f"Todo with ID {todo_id} not found.")

    def delete_todo(self):
        """
        Handle the delete todo functionality.
        """
        print("\n--- Delete Todo ---")
        if not self.todo_service.list_todos():
            display_error("No todos exist to delete.")
            return

        todo_id = safe_int_input("Enter the ID of the todo to delete: ")

        if not todo_id or not validate_todo_id(todo_id):
            display_error("Invalid todo ID.")
            return

        existing_todo = self.todo_service.get_todo(todo_id)
        if not existing_todo:
            display_error(f"Todo with ID {todo_id} not found.")
            return

        print(f"Todo to delete: {existing_todo.title}")
        if not confirm_action("Are you sure you want to delete this todo?"):
            print("Deletion cancelled.")
            return

        success = self.todo_service.delete_todo(todo_id)
        if success:
            display_success(f"Todo with ID {todo_id} deleted successfully.")
        else:
            display_error("Failed to delete todo.")

    def exit_app(self):
        """
        Handle the exit functionality.
        """
        print("\n--- Exit Application ---")
        if confirm_action("Are you sure you want to exit?"):
            print("\nThank you for using the Todo Application. Goodbye!")
            self.running = False
        else:
            print("\nExit cancelled.")

    def run(self):
        """
        Main application loop that handles user input and routes to appropriate functionality.
        """
        print("Welcome to the Todo In-Memory Console Application!")
        print("All data is stored in memory and will be lost when the application exits.")

        while self.running:
            self.display_menu()
            choice = safe_string_input("Select an option (1-6): ")

            if not choice:
                display_error("Invalid input. Please enter a number between 1 and 6.")
                continue

            if choice == "1":
                self.create_todo()
            elif choice == "2":
                self.list_todos()
            elif choice == "3":
                self.update_todo()
            elif choice == "4":
                self.mark_complete()
            elif choice == "5":
                self.delete_todo()
            elif choice == "6":
                self.exit_app()
            else:
                display_error("Invalid option. Please select a number between 1 and 6.")


def main():
    """
    Entry point for the application.
    """
    app = TodoApp()
    try:
        app.run()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted. Exiting gracefully...")
        sys.exit(0)
    except Exception as e:
        display_error(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()