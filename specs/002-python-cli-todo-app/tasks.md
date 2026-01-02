---
description: "Task list for Python CLI Todo App"
---

# Tasks: Python CLI Todo App

**Input**: Design documents from `/specs/002-python-cli-todo-app/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/cli-commands.md

**Tests**: Tests are included as per the implementation plan.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup

**Purpose**: Create the initial project structure.

- [X] T001 Create initial file structure: `src/app.py`, `src/tasks.py`, `src/cli.py`, `src/utils.py`, `tests/unit/test_tasks.py`, `tests/unit/test_cli.py`, `tests/integration/test_app_flow.py`.
- [X] T002 Create `src/__main__.py` to serve as the application entry point as defined in `quickstart.md`.

---

## Phase 2: Foundational

**Purpose**: Implement the core data model.

- [X] T003 [US1] Implement the `Task` class in `src/tasks.py` with basic attributes (`id`, `title`, `description`, `completed`) as defined in `data-model.md`.

---

## Phase 3: User Story 1 - Basic Task Management (Priority: P1) 🎯 MVP

**Goal**: As a user, I want to be able to add, view, update, delete, and mark tasks as complete.

**Independent Test**: The user can add a task, see it in the list, update its content, mark it as complete, and then delete it.

### Implementation for User Story 1

- [X] T004 [US1] Implement the `TaskManager` class in `src/tasks.py` with an in-memory dictionary to store tasks.
- [X] T005 [US1] In `TaskManager`, implement `add_task(title, description)` method.
- [X] T006 [US1] In `TaskManager`, implement `get_all_tasks()` method.
- [X] T007 [US1] In `TaskManager`, implement `update_task(task_id, title, description)` method.
- [X] T008 [US1] In `TaskManager`, implement `delete_task(task_id)` method.
- [X] T009 [US1] In `TaskManager`, implement `toggle_task_completion(task_id)` method.
- [X] T010 [P] [US1] Implement the `CLI` class in `src/cli.py` with the main menu structure from `contracts/cli-commands.md`.
- [X] T011 [US1] In `CLI`, implement the user interaction flows for adding, viewing, updating, deleting, and marking tasks as complete, calling the corresponding `TaskManager` methods.
- [X] T012 [US1] Implement the main application loop in `src/app.py` that initializes `TaskManager` and `CLI` and starts the interaction.
- [X] T013 [US1] Implement the entry point logic in `src/__main__.py` to run the application.

### Tests for User Story 1

- [X] T014 [P] [US1] Write unit tests in `tests/unit/test_tasks.py` for all `TaskManager` methods related to US1.
- [X] T015 [P] [US1] Write unit tests in `tests/unit/test_cli.py` to mock user input and verify `CLI` calls to `TaskManager` for US1 features.
- [X] T016 [US1] Write an integration test in `tests/integration/test_app_flow.py` to simulate the full user journey for US1.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 4: User Story 2 - Task Organization (Priority: P2)

**Goal**: As a user, I want to assign priorities and tags to my tasks, and then search, filter, and sort them.

**Independent Test**: The user can add priorities and tags to tasks, and then use search, filter, and sort commands to view specific subsets of tasks.

### Implementation for User Story 2

- [X] T017 [US2] Extend the `Task` class in `src/tasks.py` to include `priority` and `tags` attributes.
- [X] T018 [US2] In `TaskManager`, implement `search_tasks(keyword)` method.
- [X] T019 [US2] In `TaskManager`, implement `filter_tasks_by_status(status)`, `filter_tasks_by_priority(priority)`, and `filter_tasks_by_tag(tag)` methods.
- [X] T020 [US2] In `TaskManager`, implement `sort_tasks_by_priority()` and `sort_tasks_by_title()` methods.
- [X] T021 [US2] Update the `CLI` in `src/cli.py` to include the "Search & Filter" and "Sort" sub-menus.
- [X] T022 [US2] In `CLI`, implement the interaction flows for the new search, filter, and sort options.

### Tests for User Story 2

- [X] T023 [P] [US2] Write unit tests in `tests/unit/test_tasks.py` for the new search, filter, and sort methods in `TaskManager`.
- [X] T024 [P] [US2] Update unit tests in `tests/unit/test_cli.py` for the new sub-menus and user flows.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently.

---

## Phase 5: User Story 3 - Advanced Task Features (Priority: P3)

**Goal**: As a user, I want to set due dates and create recurring tasks.

**Independent Test**: The user can set a due date for a task and create a task that recurs on a schedule.

### Implementation for User Story 3

- [X] T025 [US3] Extend the `Task` class in `src/tasks.py` to include `due_date` and `recurrence` attributes, using the `datetime` module.
- [X] T026 [US3] Update `TaskManager.add_task` and `TaskManager.update_task` to handle `due_date` and `recurrence`.
- [X] T027 [US3] In `TaskManager`, implement logic to handle recurring tasks as per `spec.md` (re-create task for next occurrence upon completion).
- [X] T028 [US3] In `CLI`, implement logic to check for and display reminders for overdue tasks on every user interaction.
- [X] T029 [US3] Update the `CLI` in `src/cli.py` to allow users to add/update due dates and recurrence.

### Tests for User Story 3

- [X] T030 [P] [US3] Write unit tests in `tests/unit/test_tasks.py` for due date handling and recurring task logic.
- [X] T031 [P] [US3] Update unit tests in `tests/unit/test_cli.py` for the reminder logic and new input flows.

**Checkpoint**: All user stories should now be independently functional.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories.

- [X] T032 Implement utility function for generating unique task IDs in `src/utils.py`.
- [X] T033 [P] Implement robust error handling in `src/cli.py` for invalid user input (e.g., non-existent IDs, incorrect formats) as specified in `spec.md` edge cases.
- [X] T034 [P] Refine all user-facing messages in `src/cli.py` for clarity and consistency.
- [ ] T035 Final code review and cleanup across all files.

---

## Dependencies & Execution Order

- **Phase 1 & 2**: Must be completed before any User Story work begins.
- **User Stories**: Can be implemented sequentially (US1 -> US2 -> US3). All depend on Phase 1 & 2.
- **Within Stories**: Implement `Task` model changes -> `TaskManager` logic -> `CLI` interaction -> Tests.

## Implementation Strategy

- **MVP First**: Complete Phases 1, 2, and 3 to have a functional MVP with basic task management.
- **Incremental Delivery**: After the MVP, implement Phase 4, then Phase 5, testing each user story independently.
- **Polish**: Complete Phase 6 last to refine the application.
