# Quickstart Guide: Todo In-Memory Python Console Application

## Running the Application

1. Ensure Python 3.x is installed on your system
2. Navigate to the project root directory
3. Run the application with the command:
   ```bash
   python src/cli/main.py
   ```

## Using the Application

When the application starts, you will see a menu with the following options:

1. **Add Todo**: Creates a new todo item
   - Enter the title when prompted
   - Optionally enter a description
   - The system will assign a unique ID

2. **List Todos**: Displays all todos in the system
   - Shows ID, title, description, and completion status
   - Formatted for easy reading

3. **Update Todo**: Modifies an existing todo
   - Enter the ID of the todo to update
   - Optionally update the title and/or description

4. **Mark Todo as Complete**: Updates the completion status
   - Enter the ID of the todo to mark as complete
   - Status will change from "Incomplete" to "Complete"

5. **Delete Todo**: Removes a todo from the list
   - Enter the ID of the todo to delete
   - Confirmation will be required

6. **Exit**: Safely terminates the application
   - Saves nothing (in-memory only)
   - Confirms exit

## Important Notes

- All data is stored in memory only and will be lost when the application exits
- Use only valid numeric IDs when updating, completing, or deleting todos
- Invalid inputs will be handled gracefully with error messages
- The application will never crash due to invalid user input