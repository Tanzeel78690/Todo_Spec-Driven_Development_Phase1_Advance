# Quickstart: Core Todo Application

**Purpose**: This guide provides the basic steps to set up and run the Todo console application.

## Prerequisites
- Python 3.13+
- Windows Subsystem for Linux (WSL) 2 with Ubuntu 22.04 installed.
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

- **`add`**: Prompts you to enter a title and description for a new task.
- **`view`**: Shows a list of all current tasks.
- **`mark`**: Prompts you for a task ID to toggle its status (complete/incomplete).
- **`update`**: Prompts you for a task ID to update its title or description.
- **`delete`**: Prompts you for a task ID to delete a task.
- **`help`**: Displays the command menu again.
- **`exit`**: Closes the application.
