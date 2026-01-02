# Python CLI-based In-Memory Todo Application

**Purpose**: This guide provides the basic steps to set up and run the Python CLI-based In-Memory Todo Application.

## Prerequisites
- Python 3.13+
- Git

## Setup

1.  **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  **Create a virtual environment**:
    It is recommended to use a virtual environment to manage project dependencies.
    ```bash
    python3 -m venv .venv
    ```

3.  **Activate the virtual environment**:
    ```bash
    # On Windows
    .venv\Scripts\activate
    # On Linux/macOS
    source .venv/bin/activate
    ```
    
4.  **(Optional) Install dependencies**:
    This project uses only the Python standard library, but if dependencies were required, you would install them here.
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

Once the setup is complete, you can run the application from the root of the project directory with the following command:

```bash
python3 -m src
```

This will start the application and display the main menu.

## Usage

The application is controlled through a simple command menu. When prompted, type one of the following commands and press Enter.

-   **`add`**: Prompts you to enter a title, optional description, priority (high/medium/low), and tags (comma-separated) for a new task. You can also specify an optional due date (YYYY-MM-DD) and set if it's a recurring task (daily/weekly).
    Example: `add "Buy groceries" "Milk, eggs, bread" high "home,shopping" 2026-01-05 daily`
-   **`view`**: Shows a list of all current tasks, including their ID, title, description, completion status, priority, tags, due date, and recurrence.
-   **`mark`**: Prompts you for a task ID to toggle its status (complete/incomplete).
    Example: `mark 1`
-   **`update`**: Prompts you for a task ID to update its title, description, priority, tags, or due date.
    Example: `update 1 --title "Buy organic milk" --priority medium`
-   **`delete`**: Prompts you for a task ID to delete a task.
    Example: `delete 1`
-   **`search`**: Prompts for a keyword to search for in task titles and descriptions.
    Example: `search milk`
-   **`filter`**: Prompts for criteria to filter tasks by (status, priority, tag).
    Example: `filter --status incomplete --priority high`
-   **`sort`**: Prompts for a sorting criterion (priority or title).
    Example: `sort --by priority`
-   **`help`**: Displays the command menu again.
-   **`exit`**: Closes the application.

### Reminders
Overdue tasks will trigger a console-based reminder every time the user interacts with the CLI by entering a command.
