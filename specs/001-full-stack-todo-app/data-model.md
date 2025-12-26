# Data Model for Full-Stack Todo App

This document outlines the core data entities, their attributes, and relationships as derived from the feature specification. This model will serve as the basis for database schema design using SQLModel.

## Entities

### User

Represents a registered user of the application.

*   **Attributes**:
    *   `id`:
        *   **Type**: Universally Unique Identifier (UUID)
        *   **Constraints**: Primary Key, Required, Unique
        *   **Description**: A unique identifier for the user.
    *   `email`:
        *   **Type**: String
        *   **Constraints**: Required, Unique, Indexed, Valid Email Format
        *   **Description**: The user's email address, used for login and as a unique identifier.
    *   `hashed_password`:
        *   **Type**: String
        *   **Constraints**: Required
        *   **Description**: The securely hashed and salted password for the user.

*   **Relationships**:
    *   One-to-Many with `Todo`: A User can own multiple Todo items.

### Todo

Represents a single todo item belonging to a user.

*   **Attributes**:
    *   `id`:
        *   **Type**: Universally Unique Identifier (UUID)
        *   **Constraints**: Primary Key, Required, Unique
        *   **Description**: A unique identifier for the todo item.
    *   `title`:
        *   **Type**: String
        *   **Constraints**: Required, Non-empty
        *   **Description**: A brief description or title of the todo item.
    *   `is_completed`:
        *   **Type**: Boolean
        *   **Constraints**: Required
        *   **Default**: `false`
        *   **Description**: Indicates whether the todo item has been completed.
    *   `owner_id`:
        *   **Type**: Universally Unique Identifier (UUID)
        *   **Constraints**: Foreign Key referencing `User.id`, Required
        *   **Description**: Links the todo item to its owning user.

*   **Relationships**:
    *   Many-to-One with `User`: Many Todo items can belong to one User.

## Relationships Diagram (Conceptual)

```
+-------+       +-------+
| User  |       | Todo  |
+-------+       +-------+
| id    |<-----| owner_id|
| email |       | id    |
| hashed_password | title |
+-------+       | is_completed |
                +-------+
```

## Validation Rules

*   **User Email**: Must be a unique and valid email format.
*   **User Password**: Must be hashed and salted before storage. Password strength requirements will rely on defaults from the chosen authentication library/framework.
*   **Todo Title**: Cannot be empty.
*   **Todo `owner_id`**: Must reference an existing `User.id`.

## State Transitions (for Todo)

*   A Todo item can transition between `is_completed: false` (incomplete) and `is_completed: true` (completed).
*   Creation: A new Todo item is initially `is_completed: false`.
*   Deletion: A Todo item can be deleted regardless of its completion status.
