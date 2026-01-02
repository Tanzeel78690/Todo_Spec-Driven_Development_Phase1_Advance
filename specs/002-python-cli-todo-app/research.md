# Research: Python CLI Todo App

This document records the research and decisions made during the planning phase.

## 1. CLI Menu Structure

### Decision

A nested, numbered menu structure will be used. The main menu will present high-level options (e.g., "Manage Tasks", "Search/Filter Tasks"). Sub-menus will provide specific actions.

### Rationale

This approach is intuitive for new users and provides a clear path to all functionalities. It aligns with the "Clarity and simplicity" principle from the constitution.

### Alternatives Considered

-   **Flat Menu**: A single, long menu with all options. This can be overwhelming for users.
-   **Command-based Interface**: Requires users to learn commands. While powerful, it's less discoverable than a menu.

## 2. Date and Time Handling

### Decision

The standard Python `datetime` module will be used for all date and time operations. Dates and times will be stored as `datetime` objects.

### Rationale

The `datetime` module is part of the standard library, adhering to the project constraints. It provides all necessary functionality for handling due dates, recurrence, and reminders.

### Alternatives Considered

-   **External Libraries (e.g., `arrow`, `pendulum`)**: These offer more features and a simpler API, but are not allowed by the project constraints.
-   **Storing dates as strings or timestamps**: This would require manual parsing and conversion, leading to more complex and error-prone code. Using `datetime` objects is cleaner and more robust.
