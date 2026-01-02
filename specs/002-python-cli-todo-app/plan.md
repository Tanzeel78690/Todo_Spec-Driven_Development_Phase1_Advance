# Implementation Plan: Python CLI Todo App

**Feature Branch**: `002-python-cli-todo-app`
**Feature Spec**: `specs/002-python-cli-todo-app/spec.md`
**Created**: 2026-01-02
**Status**: In Progress

## 1. Technical Context

This plan outlines the technical implementation for a CLI-based, in-memory Todo application.

-   **Language**: Python 3.13+
-   **Runtime**: Command-Line Interface (CLI)
-   **Data Storage**: In-memory Python objects (e.g., lists, dictionaries).
-   **Dependencies**: Python Standard Library only.
-   **Architecture**: A modular architecture will be used, separating concerns into a `TaskManager` class for business logic, a `Task` class for the data model, and a `CLI` class for user interaction.

## 2. Constitution Check

-   [X] **Spec-first development**: This plan is derived directly from the feature specification.
-   [X] **Incremental feature progression**: The plan is structured to allow for staged implementation of Basic, Intermediate, and Advanced features.
-   [X] **Clarity and simplicity**: The CLI design will be menu-driven for ease of use.
-   [X] **Maintainability and clean Python architecture**: The proposed architecture promotes modularity and single-responsibility principles.
-   [X] **Deterministic behavior**: The in-memory nature and lack of external state ensure deterministic behavior.

## 3. Architecture

### High-Level Modules

1.  **`app.py`**: The main application entry point. It will initialize the `TaskManager` and the `CLI`, and start the main application loop.
2.  **`tasks.py`**: Will contain the `Task` data model class and the `TaskManager` class, which handles all business logic (adding, updating, deleting tasks, etc.).
3.  **`cli.py`**: Will contain the `CLI` class, responsible for all user interaction (displaying menus, getting user input, and printing output).
4.  **`utils.py`**: Will contain any utility functions, such as for parsing user input or generating unique IDs.

### Data Flow

1.  User starts the application, `app.py` initializes the `CLI` and `TaskManager`.
2.  The `CLI` displays the main menu.
3.  User selects an option (e.g., "Add Task").
4.  The `CLI` prompts for necessary information (e.g., title, description).
5.  The `CLI` calls the appropriate method on the `TaskManager` instance, passing the user's input.
6.  The `TaskManager` performs the operation (e.g., creates a new `Task` object and adds it to its internal list of tasks).
7.  The `TaskManager` returns a result (e.g., success or failure).
8.  The `CLI` displays the result to the user.

### In-Memory Data Structures

-   A `list` or `dict` within the `TaskManager` instance will hold all `Task` objects. A dictionary is preferred, with the task ID as the key for efficient lookups.
-   Each `Task` object will hold its own data (title, description, status, etc.) as attributes.

## 4. Key Decisions

| Decision | Rationale | Alternatives Considered |
| --- | --- | --- |
| **Task ID Generation** | Use a simple incrementing integer. It's easy to implement and sufficient for an in-memory application. | UUIDs. More robust for distributed systems, but overkill here. |
| **CLI Interaction Model** | Menu-driven. It is more user-friendly for beginners and explicitly stated in the spec. | Command-based (like `git`). More powerful for advanced users but has a steeper learning curve. |
| **Recurring Task Logic** | When a recurring task is completed, it is removed and a new task is created for the next recurrence date. This keeps the task list clean. | Marking the task as complete but keeping it in the list. This would require more complex logic to manage task visibility. |
| **Reminder Trigger** | Check for reminders on every user interaction (command). This provides timely reminders without a background service. | Check only on app start. This is less resource-intensive but reminders could be missed. |

## 5. Testing and Validation Strategy

-   **Unit Tests**: Each class (`TaskManager`, `CLI`) will have corresponding unit tests (`test_tasks.py`, `test_cli.py`) to verify its functionality in isolation.
-   **Integration Tests**: An integration test (`test_app_flow.py`) will simulate a user session, testing the flow of operations from the CLI to the task manager and back.
-   **Manual Validation**: The application will be manually tested against all acceptance criteria in the feature specification. This includes testing all commands, options, and edge cases.

## 6. Implementation Phases

### Phase 0: Research

-   Finalize the design of the CLI menu structure.
-   Confirm best practices for handling dates and times with the `datetime` module.

### Phase 1: Foundation (MVP)

-   Implement the `Task` data model.
-   Implement the `TaskManager` with basic CRUD operations (Add, View, Update, Delete, Mark Complete).
-   Implement the basic `CLI` for user interaction with the MVP features.

### Phase 2: Intermediate Features

-   Extend the `Task` model and `TaskManager` to handle priorities and tags.
-   Implement search, filter, and sort logic in the `TaskManager`.
-   Update the `CLI` to expose the new features.

### Phase 3: Advanced Features

-   Implement due dates and recurring task logic in the `TaskManager`.
-   Implement the reminder-checking mechanism in the `CLI`.
-   Update the `CLI` to expose the advanced features.