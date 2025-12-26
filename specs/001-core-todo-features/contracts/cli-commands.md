# CLI Contracts: Core Todo Application Features

**Purpose**: To define the public interface of the command-line application, including all commands, arguments, and expected outputs.

This serves as the "API contract" for the CLI. The application will be controlled by a main menu that maps user input to these commands.

---

## Main Menu

The application will present the user with a main menu of options. The user will select an option by entering the corresponding command word.

**Example Menu Display:**
```
===== Todo Menu =====
- add    : Add a new task
- view   : View all tasks
- mark   : Mark a task as complete/incomplete
- update : Update a task
- delete : Delete a task
- help   : Show this menu
- exit   : Exit the application
Enter command: 
```

---

## Commands

### 1. `add`
- **Description**: Adds a new task to the list.
- **Arguments**:
  - `title` (string, required): The application will prompt the user for this.
  - `description` (string, optional): The application will prompt the user for this after the title.
- **Success Output**: "Task added successfully."
- **Error Output**: If the title is empty, "Error: Title cannot be empty."

### 2. `view`
- **Description**: Displays all tasks.
- **Arguments**: None.
- **Success Output**: A formatted table of all tasks. If no tasks exist, displays "No tasks to show."
  - **Format**: Each task is displayed with its ID, Status, Title, and Description.

### 3. `mark`
- **Description**: Toggles a task's status between "incomplete" and "complete".
- **Arguments**:
  - `id` (integer, required): The application will prompt the user for the ID of the task to mark.
- **Success Output**: "Task [id] marked as [new_status]."
- **Error Output**: "Error: Task with ID [id] not found." or "Error: Invalid ID format."

### 4. `update`
- **Description**: Updates the title and/or description of an existing task.
- **Arguments**:
  - `id` (integer, required): The application will prompt the user for the ID of the task to update.
  - `new_title` (string, optional): The application will prompt the user for a new title. Pressing Enter skips the update for this field.
  - `new_description` (string, optional): The application will prompt the user for a new description. Pressing Enter skips the update for this field.
- **Success Output**: "Task [id] updated successfully."
- **Error Output**: "Error: Task with ID [id] not found." or "Error: Invalid ID format."

### 5. `delete`
- **Description**: Deletes a task from the list.
- **Arguments**:
  - `id` (integer, required): The application will prompt the user for the ID of the task to delete.
- **Success Output**: "Task [id] deleted successfully."
- **Error Output**: "Error: Task with ID [id] not found." or "Error: Invalid ID format."

### 6. `help`
- **Description**: Displays the main menu of commands.
- **Arguments**: None.
- **Success Output**: The main menu text.

### 7. `exit`
- **Description**: Exits the application.
- **Arguments**: None.
- **Success Output**: "Goodbye!"
