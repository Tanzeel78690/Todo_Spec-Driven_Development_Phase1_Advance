from dataclasses import dataclass, field
from typing import List

@dataclass
class Task:
    id: int
    title: str
    description: str
    status: str = "incomplete"

# The in-memory "database" of tasks
_tasks: List[Task] = []
_next_id: int = 1

def add_task(title: str, description: str) -> Task:
    """Creates a new task and adds it to the in-memory list."""
    global _next_id
    task = Task(id=_next_id, title=title, description=description)
    _tasks.append(task)
    _next_id += 1
    return task

def get_all_tasks() -> List[Task]:
    """Returns the complete list of tasks."""
    return _tasks

def toggle_task_status(task_id: int) -> Task | None:
    """
    Finds a task by its ID and flips its status.
    
    Args:
        task_id: The ID of the task to update.
        
    Returns:
        The updated Task object, or None if the task was not found.
    """
    for task in _tasks:
        if task.id == task_id:
            if task.status == "incomplete":
                task.status = "complete"
            else:
                task.status = "incomplete"
            return task
    return None

def update_task(task_id: int, new_title: str | None, new_description: str | None) -> Task | None:
    """
    Finds a task by its ID and updates its title and/or description.
    
    Args:
        task_id: The ID of the task to update.
        new_title: The new title. If None, title is not updated.
        new_description: The new description. If None, description is not updated.
        
    Returns:
        The updated Task object, or None if the task was not found.
    """
    for task in _tasks:
        if task.id == task_id:
            if new_title is not None:
                task.title = new_title
            if new_description is not None:
                task.description = new_description
            return task
    return None

def delete_task(task_id: int) -> Task | None:
    """
    Finds a task by its ID and removes it from the list.
    
    Args:
        task_id: The ID of the task to delete.
        
    Returns:
        The deleted Task object, or None if the task was not found.
    """
    global _tasks
    for i, task in enumerate(_tasks):
        if task.id == task_id:
            return _tasks.pop(i)
    return None
