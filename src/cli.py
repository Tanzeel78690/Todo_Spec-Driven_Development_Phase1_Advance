from typing import List, Tuple
from src.tasks import Task

def prompt_for_new_task() -> Tuple[str, str]:
    """
    Prompts the user for a new task's title and description.
    
    Returns:
        A tuple containing the title and description.
    """
    title = input("Enter task title: ")
    description = input("Enter task description (optional): ")
    return title, description

def display_tasks(tasks: List[Task]):
    """
    Prints the list of tasks in a formatted table.
    
    Args:
        tasks: A list of Task objects.
    """
    if not tasks:
        print("No tasks to show.")
        return
    
    print("\n" + "="*50)
    print(f"{'ID':<5} {'Status':<12} {'Title':<20} {'Description'}")
    print("-"*50)
    
    for task in tasks:
        print(f"{task.id:<5} {task.status:<12} {task.title:<20} {task.description}")
        
    print("="*50 + "\n")

def prompt_for_task_id(action: str) -> int | None:
    """
    Prompts the user for a task ID for a specific action.
    
    Args:
        action: The action being performed (e.g., "mark", "delete").
        
    Returns:
        The task ID as an integer, or None if the input is invalid.
    """
    try:
        id_str = input(f"Enter the ID of the task you want to {action}: ")
        return int(id_str)
    except ValueError:
        return None

def prompt_for_task_updates() -> Tuple[str | None, str | None]:
    """
    Prompts the user for a new title and/or description.
    
    Returns:
        A tuple containing the new title and description.
        If the user enters nothing, the value is None.
    """
    new_title = input("Enter new title (or press Enter to skip): ")
    new_description = input("Enter new description (or press Enter to skip): ")
    
    return new_title or None, new_description or None
