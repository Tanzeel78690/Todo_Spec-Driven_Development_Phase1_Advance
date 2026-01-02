from datetime import datetime, timedelta
from src.utils import get_unique_id

class Task:
    def __init__(self, id: int, title: str, description: str = "", priority: str = "medium", tags: list[str] = None,
                 due_date: datetime = None, recurrence: str = None):
        self.id = id
        self.title = title
        self.description = description
        self.completed = False
        self.priority = priority
        self.tags = tags if tags is not None else []
        self.due_date = due_date
        self.recurrence = recurrence

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, title: str, description: str = "", priority: str = "medium", tags: list[str] = None,
                 due_date: datetime = None, recurrence: str = None) -> Task:
        task_id = next(get_unique_id)
        task = Task(task_id, title, description, priority, tags, due_date, recurrence)
        self.tasks[task_id] = task
        return task

    def get_all_tasks(self) -> list[Task]:
        return list(self.tasks.values())

    def update_task(self, task_id: int, title: str = None, description: str = None, priority: str = None, tags: list[str] = None,
                    due_date: datetime = None, recurrence: str = None) -> bool:
        if task_id not in self.tasks:
            return False
        task = self.tasks[task_id]
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if priority is not None:
            task.priority = priority
        if tags is not None:
            task.tags = tags
        if due_date is not None:
            task.due_date = due_date
        if recurrence is not None:
            task.recurrence = recurrence
        return True

    def delete_task(self, task_id: int) -> bool:
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def toggle_task_completion(self, task_id: int) -> bool:
        if task_id not in self.tasks:
            return False
        task = self.tasks[task_id]
        
        # If the task is recurring and being marked as complete
        if not task.completed and task.recurrence:
            # Recreate the task for the next recurrence
            new_due_date = None
            if task.due_date:
                if task.recurrence == "daily":
                    new_due_date = task.due_date + timedelta(days=1)
                elif task.recurrence == "weekly":
                    new_due_date = task.due_date + timedelta(weeks=1)
            
            # Create a new task with the same details but updated due_date
            # The old task is implicitly "removed" by deleting it
            self.add_task(task.title, task.description, task.priority, task.tags, new_due_date, task.recurrence)
            del self.tasks[task_id] # Remove the old recurring task
            return True
        else: # Standard task or recurring task being marked incomplete
            task.completed = not task.completed
            return True

    def search_tasks(self, keyword: str) -> list[Task]:
        keyword_lower = keyword.lower()
        return [
            task for task in self.tasks.values()
            if keyword_lower in task.title.lower() or keyword_lower in task.description.lower()
        ]

    def filter_tasks_by_status(self, status: bool) -> list[Task]:
        return [task for task in self.tasks.values() if task.completed == status]

    def filter_tasks_by_priority(self, priority: str) -> list[Task]:
        return [task for task in self.tasks.values() if task.priority == priority]

    def filter_tasks_by_tag(self, tag: str) -> list[Task]:
        return [task for task in self.tasks.values() if tag in task.tags]

    def sort_tasks_by_priority(self) -> list[Task]:
        priority_order = {"high": 1, "medium": 2, "low": 3}
        return sorted(self.tasks.values(), key=lambda task: priority_order.get(task.priority, 99))

    def sort_tasks_by_title(self) -> list[Task]:
        return sorted(self.tasks.values(), key=lambda task: task.title.lower())