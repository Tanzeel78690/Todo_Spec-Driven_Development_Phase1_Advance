import src.tasks as tasks
import src.cli as cli

def handle_add():
    """Handles the 'add' command."""
    title, description = cli.prompt_for_new_task()
    if not title:
        print("Error: Title cannot be empty.")
        return
    tasks.add_task(title, description)
    print("Task added successfully.")

def handle_view():
    """Handles the 'view' command."""
    all_tasks = tasks.get_all_tasks()
    cli.display_tasks(all_tasks)

def handle_mark():
    """Handles the 'mark' command."""
    task_id = cli.prompt_for_task_id("mark")
    if task_id is None:
        print("Error: Invalid ID format.")
        return
    
    updated_task = tasks.toggle_task_status(task_id)
    
    if updated_task:
        print(f"Task {task_id} marked as {updated_task.status}.")
    else:
        print(f"Error: Task with ID {task_id} not found.")

def handle_update():
    """Handles the 'update' command."""
    task_id = cli.prompt_for_task_id("update")
    if task_id is None:
        print("Error: Invalid ID format.")
        return
        
    new_title, new_description = cli.prompt_for_task_updates()
    
    if new_title is None and new_description is None:
        print("No updates provided.")
        return

    updated_task = tasks.update_task(task_id, new_title, new_description)

    if updated_task:
        print(f"Task {task_id} updated successfully.")
    else:
        print(f"Error: Task with ID {task_id} not found.")

def handle_delete():
    """Handles the 'delete' command."""
    task_id = cli.prompt_for_task_id("delete")
    if task_id is None:
        print("Error: Invalid ID format.")
        return
    
    deleted_task = tasks.delete_task(task_id)
    
    if deleted_task:
        print(f"Task {task_id} deleted successfully.")
    else:
        print(f"Error: Task with ID {task_id} not found.")

def display_menu():
    """Displays the main menu to the user."""
    print("\n" + "="*20 + " Todo Menu " + "="*20)
    print("- add    : Add a new task")
    print("- view   : View all tasks")
    print("- mark   : Mark a task as complete/incomplete")
    print("- update : Update a task")
    print("- delete : Delete a task")
    print("- help   : Show this menu")
    print("- exit   : Exit the application")
    print("="*51 + "\n")

def run():
    """Main application entry point."""
    commands = {
        "add": handle_add,
        "view": handle_view,
        "mark": handle_mark,
        "update": handle_update,
        "delete": handle_delete,
        "help": display_menu,
        "exit": lambda: print("Goodbye!") or exit()
    }

    display_menu()
    while True:
        command = input("Enter command: ").lower().strip()
        if command in commands:
            commands[command]()
        else:
            print("Error: Unknown command. Type 'help' to see available commands.")

