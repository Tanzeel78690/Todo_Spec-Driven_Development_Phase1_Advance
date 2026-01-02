from datetime import datetime

class CLI:
    def __init__(self, task_manager):
        self.task_manager = task_manager

    def _get_task_input(self):
        title = input("Enter task title: ")
        description = input("Enter task description (optional): ")
        return title, description

    def _get_task_id(self):
        while True:
            try:
                task_id = int(input("Enter task ID: "))
                return task_id
            except ValueError:
                print("Invalid ID. Please enter a number.")

    def _display_tasks(self, tasks):
        if not tasks:
            print("No tasks found.")
            return

        print("\n--- Your Tasks ---")
        for task in tasks:
            status = "✓" if task.completed else " "
            priority = task.priority if hasattr(task, 'priority') else 'N/A'
            tags = ", ".join(task.tags) if hasattr(task, 'tags') and task.tags else 'N/A'
            
            due_date_str = task.due_date.strftime("%Y-%m-%d %H:%M") if task.due_date else 'N/A'
            recurrence_str = task.recurrence if task.recurrence else 'N/A'

            print(f"[{status}] ID: {task.id}, Title: {task.title}, Description: {task.description}, "
                  f"Priority: {priority}, Tags: {tags}, Due: {due_date_str}, Recurrence: {recurrence_str}")
        print("------------------")

    def _handle_add_task(self):
        title = input("Enter task title: ")
        description = input("Enter task description (optional): ")
        priority = input("Enter priority (high, medium, low, default medium): ").lower()
        if priority not in ["high", "medium", "low"]:
            priority = "medium"
        tags_input = input("Enter tags (comma-separated, optional): ")
        tags = [tag.strip() for tag in tags_input.split(',') if tag.strip()] if tags_input else []
        
        due_date_str = input("Enter due date (YYYY-MM-DD HH:MM, optional): ")
        due_date = None
        if due_date_str:
            try:
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d %H:%M")
            except ValueError:
                print("Invalid date format. Due date not set.")

        recurrence = input("Enter recurrence (daily, weekly, optional): ").lower()
        if recurrence not in ["daily", "weekly"]:
            recurrence = None

        if title:
            self.task_manager.add_task(title, description, priority, tags, due_date, recurrence)
            print("Task added successfully!")
        else:
            print("Task title cannot be empty.")

    def _handle_view_tasks(self):
        tasks = self.task_manager.get_all_tasks()
        self._display_tasks(tasks)

    def _handle_update_task(self):
        task_id = self._get_task_id()
        title = input("Enter new title (leave blank to keep current): ")
        description = input("Enter new description (leave blank to keep current): ")
        priority = input("Enter new priority (high, medium, low, leave blank to keep current): ").lower()
        if priority not in ["high", "medium", "low", ""]:
            priority = None # To not update if invalid
        tags_input = input("Enter new tags (comma-separated, leave blank to keep current): ")
        tags = [tag.strip() for tag in tags_input.split(',') if tag.strip()] if tags_input else None
        
        due_date_str = input("Enter new due date (YYYY-MM-DD HH:MM, leave blank to keep current): ")
        due_date = None
        if due_date_str:
            try:
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d %H:%M")
            except ValueError:
                print("Invalid date format. Due date not updated.")
                due_date = None # Ensure it doesn't update if invalid

        recurrence = input("Enter new recurrence (daily, weekly, leave blank to keep current): ").lower()
        if recurrence not in ["daily", "weekly", ""]:
            recurrence = None

        if self.task_manager.update_task(task_id, title if title else None, description if description else None, priority, tags, due_date, recurrence):
            print("Task updated successfully!")
        else:
            print("Task not found.")

    def _handle_delete_task(self):
        task_id = self._get_task_id()
        if self.task_manager.delete_task(task_id):
            print("Task deleted successfully!")
        else:
            print("Task not found.")

    def _handle_toggle_complete(self):
        task_id = self._get_task_id()
        if self.task_manager.toggle_task_completion(task_id):
            print("Task completion status updated!")
        else:
            print("Task not found.")

    def _check_and_display_reminders(self):
        overdue_tasks = []
        now = datetime.now()
        for task in self.task_manager.get_all_tasks():
            if task.due_date and not task.completed and task.due_date < now:
                overdue_tasks.append(task)
        
        if overdue_tasks:
            print("\n!!! REMINDER: OVERDUE TASKS !!!")
            self._display_tasks(overdue_tasks)
            print("------------------------------")

    def display_search_filter_menu(self):
        print("\n--- Search & Filter Menu ---")
        print("1. Search by Keyword")
        print("2. Filter by Status")
        print("3. Filter by Priority")
        print("4. Filter by Tag")
        print("5. Sort Tasks")
        print("6. Back to Main Menu")

    def _handle_search_filter_menu(self):
        while True:
            self.display_search_filter_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                keyword = input("Enter keyword to search: ")
                found_tasks = self.task_manager.search_tasks(keyword)
                self._display_tasks(found_tasks)
            elif choice == '2':
                status_input = input("Filter by completed (y/n): ").lower()
                status = True if status_input == 'y' else False
                filtered_tasks = self.task_manager.filter_tasks_by_status(status)
                self._display_tasks(filtered_tasks)
            elif choice == '3':
                priority = input("Filter by priority (high, medium, low): ").lower()
                if priority in ["high", "medium", "low"]:
                    filtered_tasks = self.task_manager.filter_tasks_by_priority(priority)
                    self._display_tasks(filtered_tasks)
                else:
                    print("Invalid priority.")
            elif choice == '4':
                tag = input("Filter by tag: ")
                filtered_tasks = self.task_manager.filter_tasks_by_tag(tag)
                self._display_tasks(filtered_tasks)
            elif choice == '5':
                self._handle_sort_menu()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    def display_sort_menu(self):
        print("\n--- Sort Menu ---")
        print("1. Sort by Priority")
        print("2. Sort by Title")
        print("3. Back to Search & Filter Menu")

    def _handle_sort_menu(self):
        while True:
            self.display_sort_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                sorted_tasks = self.task_manager.sort_tasks_by_priority()
                self._display_tasks(sorted_tasks)
            elif choice == '2':
                sorted_tasks = self.task_manager.sort_tasks_by_title()
                self._display_tasks(sorted_tasks)
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

    def display_main_menu(self):
        print("\n============ Todo Menu ============")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete/Incomplete")
        print("6. Search & Filter Tasks")
        print("7. Exit")
        print("===================================")

    def run(self):
        while True:
            self._check_and_display_reminders() # Call at the beginning of the loop
            self.display_main_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self._handle_add_task()
            elif choice == '2':
                self._handle_view_tasks()
            elif choice == '3':
                self._handle_update_task()
            elif choice == '4':
                self._handle_delete_task()
            elif choice == '5':
                self._handle_toggle_complete()
            elif choice == '6':
                self._handle_search_filter_menu()
            elif choice == '7':
                print("Exiting application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")