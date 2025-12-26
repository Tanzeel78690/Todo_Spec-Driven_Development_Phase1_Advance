# In tests/unit/test_tasks.py

# First, clear the content of the file to avoid conflicts
# Then, add the new content

import pytest
from src import tasks

# A fixture to ensure each test starts with a clean slate
@pytest.fixture(autouse=True)
def clean_tasks():
    tasks._tasks = []
    tasks._next_id = 1

def test_add_task():
    """
    Tests that a task can be added and it has the correct attributes.
    """
    task = tasks.add_task("Test Title", "Test Description")
    assert task.id == 1
    assert task.title == "Test Title"
    assert task.description == "Test Description"
    assert task.status == "incomplete"
    assert len(tasks._tasks) == 1
    assert tasks._tasks[0] == task

def test_get_all_tasks():
    """
    Tests that all added tasks can be retrieved.
    """
    task1 = tasks.add_task("First", "First Desc")
    task2 = tasks.add_task("Second", "Second Desc")
    
    all_tasks = tasks.get_all_tasks()
    
    assert len(all_tasks) == 2
    assert task1 in all_tasks
    assert task2 in all_tasks

def test_toggle_task_status():
    """
    Tests that a task's status can be toggled.
    """
    task = tasks.add_task("Toggle Test", "")
    assert task.status == "incomplete"
    
    # Toggle to complete
    updated_task = tasks.toggle_task_status(task.id)
    assert updated_task.status == "complete"
    
    # Toggle back to incomplete
    updated_task_again = tasks.toggle_task_status(task.id)
    assert updated_task_again.status == "incomplete"

def test_toggle_nonexistent_task():
    """
    Tests that toggling a non-existent task returns None.
    """
    assert tasks.toggle_task_status(999) is None

def test_update_task():
    """
    Tests that a task's title and description can be updated.
    """
    task = tasks.add_task("Original Title", "Original Desc")
    
    updated_task = tasks.update_task(task.id, "New Title", "New Desc")
    assert updated_task.title == "New Title"
    assert updated_task.description == "New Desc"
    
    # Test updating only title
    updated_task_2 = tasks.update_task(task.id, "Second New Title", None)
    assert updated_task_2.title == "Second New Title"
    assert updated_task_2.description == "New Desc" # Description should remain from previous update
    
    # Test updating only description
    updated_task_3 = tasks.update_task(task.id, None, "Second New Desc")
    assert updated_task_3.title == "Second New Title" # Title should remain
    assert updated_task_3.description == "Second New Desc"

def test_update_nonexistent_task():
    """
    Tests that updating a non-existent task returns None.
    """
    assert tasks.update_task(999, "title", "desc") is None

def test_delete_task():
    """
    Tests that a task can be deleted.
    """
    task1 = tasks.add_task("Delete Me", "")
    task2 = tasks.add_task("Keep Me", "")
    
    deleted_task = tasks.delete_task(task1.id)
    
    assert deleted_task == task1
    assert len(tasks._tasks) == 1
    assert task1 not in tasks._tasks
    assert task2 in tasks._tasks

def test_delete_nonexistent_task():
    """
    Tests that deleting a non-existent task returns None.
    """
    assert tasks.delete_task(999) is None

def test_delete_task():
    """
    Tests that a task can be deleted.
    """
    task1 = tasks.add_task("Delete Me", "")
    task2 = tasks.add_task("Keep Me", "")
    
    deleted_task = tasks.delete_task(task1.id)
    
    assert deleted_task == task1
    assert len(tasks._tasks) == 1
    assert task1 not in tasks._tasks
    assert task2 in tasks._tasks

def test_delete_nonexistent_task():
    """
    Tests that deleting a non-existent task returns None.
    """
    assert tasks.delete_task(999) is None
