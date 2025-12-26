# API Contracts for Full-Stack Todo App

This document details the RESTful API endpoints, their request/response formats, and expected HTTP status codes, as derived from the functional requirements in `spec.md`. All API endpoints will be prefixed with `/api/`.

## Authentication Endpoints

### 1. User Signup

*   **Endpoint**: `POST /api/signup`
*   **Description**: Registers a new user account.
*   **Request Body**:
    ```json
    {
        "email": "user@example.com",
        "password": "securepassword"
    }
    ```
    *   `email`: (string, required) Unique email address for the new user.
    *   `password`: (string, required) Password for the new user.
*   **Responses**:
    *   `201 Created`:
        ```json
        {
            "message": "User registered successfully"
        }
        ```
    *   `400 Bad Request`:
        ```json
        {
            "detail": "Email already registered"
        }
        ```
        or
        ```json
        {
            "detail": "Invalid input"
        }
        ```
        (e.g., malformed email, weak password if enforced by auth library)

### 2. User Signin

*   **Endpoint**: `POST /api/signin`
*   **Description**: Authenticates a user and issues a JWT.
*   **Request Body**:
    ```json
    {
        "email": "user@example.com",
        "password": "securepassword"
    }
    ```
    *   `email`: (string, required) Registered email address.
    *   `password`: (string, required) User's password.
*   **Responses**:
    *   `200 OK`:
        ```json
        {
            "access_token": "jwt_token_string",
            "token_type": "bearer"
        }
        ```
        *   `access_token`: (string) The JWT for authenticated requests.
        *   `token_type`: (string) Type of token, always "bearer".
    *   `401 Unauthorized`:
        ```json
        {
            "detail": "Incorrect email or password"
        }
        ```

## Todo Endpoints

All Todo endpoints require a valid JWT passed in the `Authorization` header: `Authorization: Bearer <JWT>`.

### 1. Create Todo

*   **Endpoint**: `POST /api/todos`
*   **Description**: Creates a new todo item for the authenticated user.
*   **Authentication**: Required (JWT)
*   **Request Body**:
    ```json
    {
        "title": "Buy groceries",
        "is_completed": false
    }
    ```
    *   `title`: (string, required) Title or description of the todo item.
    *   `is_completed`: (boolean, optional, default: `false`) Initial completion status.
*   **Responses**:
    *   `201 Created`:
        ```json
        {
            "id": "uuid",
            "title": "Buy groceries",
            "is_completed": false,
            "owner_id": "uuid"
        }
        ```
        *   `id`: (UUID) Unique identifier for the created todo.
        *   `title`: (string) Title of the todo.
        *   `is_completed`: (boolean) Completion status.
        *   `owner_id`: (UUID) ID of the owning user.
    *   `401 Unauthorized`: `{"detail": "Not authenticated"}`
    *   `400 Bad Request`: `{"detail": "Invalid input"}`

### 2. List Todos

*   **Endpoint**: `GET /api/todos`
*   **Description**: Retrieves all todo items belonging to the authenticated user.
*   **Authentication**: Required (JWT)
*   **Request Body**: None
*   **Responses**:
    *   `200 OK`:
        ```json
        [
            {
                "id": "uuid",
                "title": "Buy groceries",
                "is_completed": false,
                "owner_id": "uuid"
            },
            ...
        ]
        ```
    *   `401 Unauthorized`: `{"detail": "Not authenticated"}`

### 3. Retrieve Single Todo

*   **Endpoint**: `GET /api/todos/{id}`
*   **Description**: Retrieves a specific todo item by its ID, if it belongs to the authenticated user.
*   **Authentication**: Required (JWT)
*   **Path Parameters**:
    *   `id`: (UUID, required) The ID of the todo item.
*   **Responses**:
    *   `200 OK`:
        ```json
        {
            "id": "uuid",
            "title": "Buy groceries",
            "is_completed": false,
            "owner_id": "uuid"
        }
        ```
    *   `401 Unauthorized`: `{"detail": "Not authenticated"}`
    *   `404 Not Found`: `{"detail": "Todo not found"}` (or not found for this user)
    *   `403 Forbidden`: `{"detail": "Not authorized to access this todo"}`

### 4. Update Todo

*   **Endpoint**: `PUT /api/todos/{id}`
*   **Description**: Updates an existing todo item by its ID, if it belongs to the authenticated user.
*   **Authentication**: Required (JWT)
*   **Path Parameters**:
    *   `id`: (UUID, required) The ID of the todo item to update.
*   **Request Body**:
    ```json
    {
        "title": "Buy milk",
        "is_completed": true
    }
    ```
    *   `title`: (string, optional) New title for the todo item.
    *   `is_completed`: (boolean, optional) New completion status.
*   **Responses**:
    *   `200 OK`:
        ```json
        {
            "id": "uuid",
            "title": "Buy milk",
            "is_completed": true,
            "owner_id": "uuid"
        }
        ```
    *   `401 Unauthorized`: `{"detail": "Not authenticated"}`
    *   `404 Not Found`: `{"detail": "Todo not found"}`
    *   `403 Forbidden`: `{"detail": "Not authorized to modify this todo"}`
    *   `400 Bad Request`: `{"detail": "Invalid input"}`

### 5. Delete Todo

*   **Endpoint**: `DELETE /api/todos/{id}`
*   **Description**: Deletes a specific todo item by its ID, if it belongs to the authenticated user.
*   **Authentication**: Required (JWT)
*   **Path Parameters**:
    *   `id`: (UUID, required) The ID of the todo item to delete.
*   **Request Body**: None
*   **Responses**:
    *   `204 No Content`: (Empty body) Indicates successful deletion.
    *   `401 Unauthorized`: `{"detail": "Not authenticated"}`
    *   `404 Not Found`: `{"detail": "Todo not found"}`
    *   `403 Forbidden`: `{"detail": "Not authorized to delete this todo"}`

## Common Error Taxonomy

*   `400 Bad Request`: Invalid request payload or parameters.
*   `401 Unauthorized`: Authentication credentials are missing or invalid.
*   `403 Forbidden`: Authenticated user does not have permission to access the resource.
*   `404 Not Found`: The requested resource does not exist.
*   `422 Unprocessable Entity`: Validation error due to semantic issues with the request.
*   `500 Internal Server Error`: Generic server-side error.
