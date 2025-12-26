# Quickstart Guide: Full-Stack Todo App

This guide provides instructions for quickly setting up and running the Full-Stack Todo Application locally.

## Prerequisites

Before you begin, ensure you have the following installed:

*   **Git**: For cloning the repository.
*   **Python 3.11+**: For the FastAPI backend.
*   **uv**: Python package manager. If not installed, you can install it via `pip install uv`.
*   **Node.js 18+ & npm/yarn**: For the Next.js frontend.
*   **Docker Desktop**: (Optional, but recommended for local PostgreSQL setup if not using Neon directly).
*   **Neon Serverless PostgreSQL Account**: (Required for persistent storage).

## 1. Clone the Repository

First, clone the project repository:

```bash
git clone <repository_url>
cd <repository_name>
```

## 2. Backend Setup (FastAPI)

1.  **Navigate to the backend directory**:
    ```bash
    cd backend
    ```
2.  **Create a Python virtual environment and install dependencies**:
    ```bash
    uv venv
    uv pip install -r requirements.txt # (assuming requirements.txt will be generated)
    # Alternatively, if pyproject.toml is used:
    # uv pip install
    ```
3.  **Configure Environment Variables**:
    Create a `.env` file in the `backend/` directory with your database connection string and JWT secret:
    ```
    DATABASE_URL="postgresql+psycopg://<user>:<password>@<host>/<database>"
    JWT_SECRET_KEY="your_super_secret_jwt_key"
    ALGORITHM="HS256" # Or other chosen algorithm for JWT
    ACCESS_TOKEN_EXPIRE_MINUTES=30 # Example value
    ```
    *Replace `<user>`, `<password>`, `<host>`, and `<database>` with your Neon PostgreSQL credentials.*
4.  **Run Database Migrations (if applicable)**:
    (Details will be provided once SQLModel migration strategy is defined, e.g., using `alembic` or direct SQLModel synchronization).
    ```bash
    # Example:
    # alembic upgrade head
    ```
5.  **Start the FastAPI backend server**:
    ```bash
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
    ```
    The backend API will be available at `http://localhost:8000`.

## 3. Frontend Setup (Next.js)

1.  **Navigate to the frontend directory**:
    ```bash
    cd frontend
    ```
2.  **Install Node.js dependencies**:
    ```bash
    npm install # or yarn install
    ```
3.  **Configure Environment Variables**:
    Create a `.env.local` file in the `frontend/` directory with the backend API URL:
    ```
    NEXT_PUBLIC_API_URL="http://localhost:8000/api"
    ```
4.  **Start the Next.js development server**:
    ```bash
    npm run dev # or yarn dev
    ```
    The frontend application will be available at `http://localhost:3000` (or another port if 3000 is in use).

## 4. Using the Application

1.  Open your web browser and navigate to `http://localhost:3000`.
2.  Sign up for a new user account.
3.  Sign in with your new credentials.
4.  Start creating, viewing, updating, and deleting your todo items.
    
*Note: Ensure both the backend and frontend servers are running concurrently.*
