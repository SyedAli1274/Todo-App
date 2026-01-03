# Data Model: Todo In-Memory Python Console Application

## Todo Entity

### Fields
- **id**: Integer (unique identifier, auto-incrementing)
- **title**: String (required, non-empty)
- **description**: String (optional, can be empty)
- **completed**: Boolean (default: False)

### Validation Rules
- ID must be unique within the collection
- Title must not be empty or None
- Completed status must be boolean

### State Transitions
- Initially: completed = False
- After marking complete: completed = True
- After marking incomplete: completed = False (if feature supported)

## TodoList Collection

### Fields
- **todos**: List of Todo entities
- **next_id**: Integer (auto-incrementing counter for new IDs)

### Operations
- **Add Todo**: Add a new Todo entity to the collection with unique ID
- **Get Todo**: Retrieve a Todo entity by its ID
- **Update Todo**: Modify an existing Todo entity by its ID
- **Delete Todo**: Remove a Todo entity by its ID
- **List Todos**: Return all Todo entities in the collection
- **Mark Complete**: Update the completion status of a Todo by its ID

### Validation Rules
- No duplicate IDs allowed
- Operations with non-existent IDs should return appropriate errors
- Title validation must occur before adding/updating