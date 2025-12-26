# Tasks: Core Todo Application Features

**Input**: Design documents from `specs/001-core-todo-features/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/

**Tests**: Test tasks are included as they align with the project's "Clean Code" and "Reproducibility" principles. The TDD-style approach (tests first) is followed within each user story phase.

**Organization**: Tasks are grouped by user story to enable independent, incremental implementation.

## Format: `[ID] [P?] [Story] Description`
- **[P]**: Can run in parallel (different files, no dependencies).
- **[Story]**: Which user story this task belongs to (e.g., US1, US2).

---
## Phase 1: Setup (Shared Infrastructure)
**Purpose**: Create the directories and empty files for the project structure defined in `plan.md`.

- [x] T001 [P] Create source directory `src/`.
- [x] T002 [P] Create tests directory `tests/` with subdirectories `unit/` and `integration/`.
- [x] T003 [P] Create empty placeholder files: `src/__main__.py`, `src/app.py`, `src/tasks.py`, `src/cli.py`, `src/utils.py`.
- [x] T004 [P] Create empty test files: `tests/unit/test_tasks.py`, `tests/unit/test_cli.py`, `tests/integration/test_app_flow.py`.
- [x] T005 [P] Create a basic `pyproject.toml` file to configure `pytest`.

---
## Phase 2: Foundational (Blocking Prerequisites)
**Purpose**: Define the core data structure that all other logic will depend on.

- [x] T006 Define the `Task` data structure (e.g., as a `typing.TypedDict` or `dataclasses.dataclass`) in `src/tasks.py` based on `data-model.md`.

---
## Phase 3: User Stories 1 & 2 - Add and View Tasks (Priority: P1) 🎯 MVP
**Goal**: Implement the ability to add a task and view the list of all tasks.
**Independent Test**: Run the app, use the `add` command, then use the `view` command and verify the new task is displayed correctly.

### Tests for User Stories 1 & 2 ⚠️
- [x] T007 [P] [US1] In `tests/unit/test_tasks.py`, write a failing unit test for adding a task to the in-memory list.
- [x] T008 [P] [US2] In `tests/unit/test_tasks.py`, write a failing unit test for retrieving the list of all tasks.

### Implementation for User Stories 1 & 2
- [x] T009 [US1] In `src/tasks.py`, implement the in-memory list to store tasks and the function `add_task(title, description)` which creates a new task and adds it to the list. This task depends on T006.
- [x] T010 [US2] In `src/tasks.py`, implement the function `get_all_tasks()` that returns the complete list of tasks.
- [x] T011 [P] [US1] In `src/cli.py`, implement the function `prompt_for_new_task()` to get a title and description from the user.
- [x] T012 [P] [US2] In `src/cli.py`, implement the function `display_tasks(tasks)` to print the list of tasks in a formatted table.
- [x] T013 [US1, US2] In `src/app.py`, implement logic for the `add` and `view` commands in the main application menu to call the appropriate functions from `tasks.py` and `cli.py`.

---
## Phase 4: User Story 3 - Mark Task Status (Priority: P2)
**Goal**: Allow a user to toggle a task's status between "incomplete" and "complete".
**Independent Test**: Run the app, add a task, view it, use the `mark` command with the task's ID, and view again to confirm the status has changed.

### Tests for User Story 3 ⚠️
- [x] T014 [P] [US3] In `tests/unit/test_tasks.py`, write failing unit tests for toggling a task's status. It should handle finding the task, changing "incomplete" to "complete", and vice-versa.

### Implementation for User Story 3
- [x] T015 [US3] In `src/tasks.py`, implement the function `toggle_task_status(task_id)` to find a task by its ID and flip its status.
- [x] T016 [P] [US3] In `src/cli.py`, implement the function `prompt_for_task_id(action)` to ask the user for a task ID for a specific action (e.g., "mark").
- [x] T017 [US3] In `src/app.py`, integrate the `mark` command, calling the functions from `tasks.py` and `cli.py`.

---
## Phase 5: User Story 4 - Update Task (Priority: P2)
**Goal**: Allow a user to edit the title and description of an existing task.
**Independent Test**: Run the app, add a task, view it, use the `update` command with the task's ID, provide a new title/description, and view again to confirm the changes.

### Tests for User Story 4 ⚠️
- [x] T018 [P] [US4] In `tests/unit/test_tasks.py`, write a failing unit test for updating a task's title and description.

### Implementation for User Story 4
- [x] T019 [US4] In `src/tasks.py`, implement the function `update_task(task_id, new_title, new_description)`.
- [x] T020 [P] [US4] In `src/cli.py`, implement the function `prompt_for_task_updates()` to get a new title and/or description from the user.
- [x] T021 [US4] In `src/app.py`, integrate the `update` command.

---
## Phase 6: User Story 5 - Delete Task (Priority: P3)
**Goal**: Allow a user to remove a task from the list.
**Independent Test**: Run the app, add a task, view it, use the `delete` command with the task's ID, and view again to confirm it's gone.

### Tests for User Story 5 ⚠️
- [x] T022 [P] [US5] In `tests/unit/test_tasks.py`, write a failing unit test for deleting a task.

### Implementation for User Story 5
- [x] T023 [US5] In `src/tasks.py`, implement the function `delete_task(task_id)`.
- [x] T024 [US5] In `src/app.py`, integrate the `delete` command.

---
## Phase 7: Polish & Cross-Cutting Concerns
**Purpose**: Finalize the application loop, error handling, and user-facing documentation.

- [x] T025 In `src/app.py`, implement the main application loop that displays the menu, accepts user commands, and continues until the `exit` command is entered.
- [x] T026 [P] In `src/tasks.py`, add error handling to all functions that accept a `task_id` to handle cases where the ID is not found.
- [x] T027 [P] In `src/cli.py`, implement user-friendly formatting for error messages.
- [x] T028 In `src/__main__.py`, add the code to start the application by calling the main loop from `src/app.py`.
- [x] T029 Create a `README.md` file at the project root based on the contents of `specs/001-core-todo-features/quickstart.md`.
