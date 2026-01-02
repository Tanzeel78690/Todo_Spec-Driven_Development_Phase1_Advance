import unittest
from datetime import datetime, timedelta
from src.tasks import Task, TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_manager = TaskManager()

    def test_add_task(self):
        task = self.task_manager.add_task("Test Task", "Description for test task")
        self.assertIsInstance(task, Task)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Description for test task")
        self.assertFalse(task.completed)
        self.assertEqual(len(self.task_manager.tasks), 1)

    def test_get_all_tasks(self):
        self.task_manager.add_task("Task 1")
        self.task_manager.add_task("Task 2")
        tasks = self.task_manager.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].title, "Task 1")
        self.assertEqual(tasks[1].title, "Task 2")

    def test_update_task(self):
        self.task_manager.add_task("Task to Update")
        updated = self.task_manager.update_task(1, "Updated Title", "Updated Description")
        self.assertTrue(updated)
        task = self.task_manager.tasks[1]
        self.assertEqual(task.title, "Updated Title")
        self.assertEqual(task.description, "Updated Description")

        updated_title_only = self.task_manager.update_task(1, title="New Title Only")
        self.assertTrue(updated_title_only)
        task = self.task_manager.tasks[1]
        self.assertEqual(task.title, "New Title Only")
        self.assertEqual(task.description, "Updated Description") # Description should remain unchanged

        updated_description_only = self.task_manager.update_task(1, description="New Description Only")
        self.assertTrue(updated_description_only)
        task = self.task_manager.tasks[1]
        self.assertEqual(task.title, "New Title Only") # Title should remain unchanged
        self.assertEqual(task.description, "New Description Only")

        not_found = self.task_manager.update_task(99, "Non Existent")
        self.assertFalse(not_found)

    def test_delete_task(self):
        self.task_manager.add_task("Task to Delete")
        deleted = self.task_manager.delete_task(1)
        self.assertTrue(deleted)
        self.assertEqual(len(self.task_manager.tasks), 0)

        not_found = self.task_manager.delete_task(99)
        self.assertFalse(not_found)

    def test_toggle_task_completion(self):
        self.task_manager.add_task("Task to Toggle")
        task = self.task_manager.tasks[1]
        self.assertFalse(task.completed)

        toggled = self.task_manager.toggle_task_completion(1)
        self.assertTrue(toggled)
        self.assertTrue(task.completed)

        toggled_again = self.task_manager.toggle_task_completion(1)
        self.assertTrue(toggled_again)
        self.assertFalse(task.completed)

        not_found = self.task_manager.toggle_task_completion(99)
        self.assertFalse(not_found)

    def test_search_tasks(self):
        self.task_manager.add_task("Buy milk", "Remember to get 2% milk")
        self.task_manager.add_task("Walk dog", "Take the dog for a walk")
        self.task_manager.add_task("Clean house", "Vacuum and dust")
        
        results = self.task_manager.search_tasks("milk")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Buy milk")

        results_case_insensitive = self.task_manager.search_tasks("DOG")
        self.assertEqual(len(results_case_insensitive), 1)
        self.assertEqual(results_case_insensitive[0].title, "Walk dog")

        results_no_match = self.task_manager.search_tasks("nonexistent")
        self.assertEqual(len(results_no_match), 0)

    def test_filter_tasks_by_status(self):
        task1 = self.task_manager.add_task("Complete task")
        task2 = self.task_manager.add_task("Incomplete task")
        self.task_manager.toggle_task_completion(task1.id)

        completed_tasks = self.task_manager.filter_tasks_by_status(True)
        self.assertEqual(len(completed_tasks), 1)
        self.assertTrue(completed_tasks[0].completed)

        incomplete_tasks = self.task_manager.filter_tasks_by_status(False)
        self.assertEqual(len(incomplete_tasks), 1)
        self.assertFalse(incomplete_tasks[0].completed)

    def test_filter_tasks_by_priority(self):
        task1 = self.task_manager.add_task("High priority", priority="high")
        task2 = self.task_manager.add_task("Medium priority", priority="medium")
        task3 = self.task_manager.add_task("Low priority", priority="low")

        high_priority_tasks = self.task_manager.filter_tasks_by_priority("high")
        self.assertEqual(len(high_priority_tasks), 1)
        self.assertEqual(high_priority_tasks[0].priority, "high")

    def test_filter_tasks_by_tag(self):
        task1 = self.task_manager.add_task("Work task", tags=["work", "urgent"])
        task2 = self.task_manager.add_task("Home task", tags=["home"])
        task3 = self.task_manager.add_task("Urgent task", tags=["urgent"])

        work_tasks = self.task_manager.filter_tasks_by_tag("work")
        self.assertEqual(len(work_tasks), 1)
        self.assertIn("work", work_tasks[0].tags)

        urgent_tasks = self.task_manager.filter_tasks_by_tag("urgent")
        self.assertEqual(len(urgent_tasks), 2)
        self.assertIn("urgent", urgent_tasks[0].tags)
        self.assertIn("urgent", urgent_tasks[1].tags)

    def test_sort_tasks_by_priority(self):
        self.task_manager.add_task("Task A", priority="medium")
        self.task_manager.add_task("Task B", priority="high")
        self.task_manager.add_task("Task C", priority="low")

        sorted_tasks = self.task_manager.sort_tasks_by_priority()
        self.assertEqual(len(sorted_tasks), 3)
        self.assertEqual(sorted_tasks[0].title, "Task B") # High
        self.assertEqual(sorted_tasks[1].title, "Task A") # Medium
        self.assertEqual(sorted_tasks[2].title, "Task C") # Low

    def test_sort_tasks_by_title(self):
        self.task_manager.add_task("Zebra Task")
        self.task_manager.add_task("Apple Task")
        self.task_manager.add_task("Banana Task")

        sorted_tasks = self.task_manager.sort_tasks_by_title()
        self.assertEqual(len(sorted_tasks), 3)
        self.assertEqual(sorted_tasks[0].title, "Apple Task")
        self.assertEqual(sorted_tasks[1].title, "Banana Task")
        self.assertEqual(sorted_tasks[2].title, "Zebra Task")

    def test_add_task_with_due_date_and_recurrence(self):
        now = datetime.now()
        task = self.task_manager.add_task("Recurring Task", due_date=now, recurrence="daily")
        self.assertIsInstance(task, Task)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.due_date, now)
        self.assertEqual(task.recurrence, "daily")

    def test_update_task_due_date_and_recurrence(self):
        self.task_manager.add_task("Task with Due Date")
        original_due_date = datetime(2026, 1, 1, 10, 0)
        new_due_date = datetime(2026, 1, 2, 11, 0)
        
        updated = self.task_manager.update_task(1, due_date=new_due_date, recurrence="weekly")
        self.assertTrue(updated)
        task = self.task_manager.tasks[1]
        self.assertEqual(task.due_date, new_due_date)
        self.assertEqual(task.recurrence, "weekly")

    @patch('src.tasks.datetime') # Mock datetime to control now()
    def test_toggle_recurring_task_completion_daily(self, mock_datetime):
        # Set a fixed 'now' for consistent testing
        fixed_now = datetime(2026, 1, 1, 12, 0)
        mock_datetime.now.return_value = fixed_now
        mock_datetime.side_effect = lambda *args, **kw: datetime(*args, **kw) # Allow normal datetime object creation
        mock_datetime.timedelta = timedelta

        task = self.task_manager.add_task("Daily Task", due_date=fixed_now - timedelta(hours=1), recurrence="daily")
        task_id = task.id
        self.assertFalse(task.completed)
        self.assertEqual(len(self.task_manager.tasks), 1)

        # Mark as complete (should re-create)
        toggled = self.task_manager.toggle_task_completion(task_id)
        self.assertTrue(toggled)
        self.assertEqual(len(self.task_manager.tasks), 1) # Still one task, old one deleted, new one added

        new_task = list(self.task_manager.tasks.values())[0]
        self.assertNotEqual(new_task.id, task_id)
        self.assertFalse(new_task.completed)
        self.assertEqual(new_task.due_date, fixed_now - timedelta(hours=1) + timedelta(days=1))
        self.assertEqual(new_task.recurrence, "daily")

    @patch('src.tasks.datetime') # Mock datetime to control now()
    def test_toggle_recurring_task_completion_weekly(self, mock_datetime):
        fixed_now = datetime(2026, 1, 1, 12, 0)
        mock_datetime.now.return_value = fixed_now
        mock_datetime.side_effect = lambda *args, **kw: datetime(*args, **kw)
        mock_datetime.timedelta = timedelta

        task = self.task_manager.add_task("Weekly Task", due_date=fixed_now - timedelta(hours=1), recurrence="weekly")
        task_id = task.id

        toggled = self.task_manager.toggle_task_completion(task_id)
        self.assertTrue(toggled)
        self.assertEqual(len(self.task_manager.tasks), 1)

        new_task = list(self.task_manager.tasks.values())[0]
        self.assertEqual(new_task.due_date, fixed_now - timedelta(hours=1) + timedelta(weeks=1))
        self.assertEqual(new_task.recurrence, "weekly")

    def test_toggle_non_recurring_task_completion(self):
        task = self.task_manager.add_task("Normal Task")
        self.assertFalse(task.completed)
        self.task_manager.toggle_task_completion(task.id)
        self.assertTrue(task.completed)
        self.task_manager.toggle_task_completion(task.id)
        self.assertFalse(task.completed)


if __name__ == '__main__':
    unittest.main()
