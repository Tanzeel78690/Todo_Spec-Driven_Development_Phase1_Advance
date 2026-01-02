# Data Model: Python CLI Todo App

This document defines the data model for the `Task` entity.

## `Task` Entity

Represents a single to-do item in the application.

### Attributes

| Attribute | Type | Description | Validation Rules |
|---|---|---|---|
| `id` | `int` | A unique identifier for the task. | Must be a unique, positive integer. Generated automatically. |
| `title` | `str` | The title of the task. | Required, non-empty string. |
| `description` | `str` | An optional, more detailed description of the task. | Optional. |
| `completed` | `bool` | The completion status of the task. | Defaults to `False`. |
| `priority` | `str` | The priority of the task. | Must be one of "high", "medium", or "low". Defaults to "medium". |
| `tags` | `list[str]` | A list of tags or categories associated with the task. | Optional. |
| `due_date` | `datetime` | An optional due date and time for the task. | Optional. Must be a valid `datetime` object. |
| `recurrence` | `str` | The recurrence rule for the task. | Optional. Must be one of "daily" or "weekly". |

### State Transitions

-   A `Task` is created with a `completed` status of `False`.
-   The `completed` status can be toggled between `True` and `False`.
-   When a recurring task is marked as `completed`, a new task is generated for the next recurrence date, and the original task is removed.
