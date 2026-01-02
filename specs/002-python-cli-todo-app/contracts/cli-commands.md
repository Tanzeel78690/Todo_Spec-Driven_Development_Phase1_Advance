# CLI Commands Contract

This document defines the contract for the menu-driven CLI.

## Main Menu

1.  **Add Task**: Prompts the user for task details and adds a new task.
2.  **View All Tasks**: Displays a list of all tasks with their details.
3.  **Update Task**: Prompts for a task ID and allows updating its details.
4.  **Delete Task**: Prompts for a task ID and deletes the task.
5.  **Mark Task Complete/Incomplete**: Prompts for a task ID and toggles its completion status.
6.  **Search & Filter Tasks**: Enters the Search & Filter sub-menu.
7.  **Exit**: Exits the application.

## Search & Filter Sub-Menu

1.  **Search by Keyword**: Prompts for a keyword and displays tasks matching it.
2.  **Filter by Status**: Prompts for a status (complete/incomplete) and displays matching tasks.
3.  **Filter by Priority**: Prompts for a priority and displays matching tasks.
4.  **Filter by Tag**: Prompts for a tag and displays matching tasks.
5.  **Sort Tasks**: Enters the Sort sub-menu.
6.  **Back to Main Menu**: Returns to the main menu.

## Sort Sub-Menu

1.  **Sort by Priority**: Displays tasks sorted by priority.
2.  **Sort by Title**: Displays tasks sorted alphabetically by title.
3.  **Back to Search & Filter Menu**: Returns to the Search & Filter sub-menu.
