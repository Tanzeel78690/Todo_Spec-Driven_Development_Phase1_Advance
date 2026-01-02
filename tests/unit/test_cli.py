import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from datetime import datetime, timedelta
from src.cli import CLI
from src.tasks import Task, TaskManager

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.task_manager = MagicMock(spec=TaskManager)
        self.cli = CLI(self.task_manager)
        # Mocking TaskManager methods to return simple Task objects for display
        self.task_manager.get_all_tasks.return_value = [
            Task(1, "Task 1", "Desc 1", priority="high", tags=["work"]),
            Task(2, "Task 2", "Desc 2", priority="medium", tags=["home"]),
        ]
        self.task_manager.search_tasks.return_value = [
            Task(1, "Task 1", "Desc 1", priority="high", tags=["work"]),
        ]
        self.task_manager.filter_tasks_by_status.return_value = [
            Task(1, "Task 1", "Desc 1", completed=True),
        ]
        self.task_manager.filter_tasks_by_priority.return_value = [
            Task(1, "Task 1", "Desc 1", priority="high"),
        ]
        self.task_manager.filter_tasks_by_tag.return_value = [
            Task(1, "Task 1", "Desc 1", tags=["work"]),
        ]
        self.task_manager.sort_tasks_by_priority.return_value = [
            Task(1, "Task High", priority="high"),
            Task(2, "Task Medium", priority="medium"),
        ]
        self.task_manager.sort_tasks_by_title.return_value = [
            Task(1, "Alpha Task"),
            Task(2, "Beta Task"),
        ]

    @patch('builtins.input', side_effect=[
        '1', 'Test Task', 'Test Description', 'high', 'tag1,tag2',
        '2026-01-01 10:00', 'daily', '7'
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_task_flow_with_advanced_features(self, mock_stdout, mock_input):
        due_date = datetime(2026, 1, 1, 10, 0)
        self.task_manager.add_task.return_value = Task(1, "Test Task", "Test Description", "high", ["tag1", "tag2"], due_date, "daily")
        self.cli.run()
        self.task_manager.add_task.assert_called_with("Test Task", "Test Description", "high", ["tag1", "tag2"], due_date, "daily")
        self.assertIn("Task added successfully!", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['2', '7'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_view_tasks_flow(self, mock_stdout, mock_input):
        self.cli.run()
        self.task_manager.get_all_tasks.assert_called_once()
        self.assertIn("ID: 1, Title: Task 1, Description: Desc 1, Priority: high, Tags: work, Due: N/A, Recurrence: N/A", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=[
        '3', '1', 'Updated Title', 'Updated Desc', 'medium', 'newtag1,newtag2',
        '2026-01-02 11:00', 'weekly', '7'
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_update_task_flow_with_advanced_features(self, mock_stdout, mock_input):
        due_date = datetime(2026, 1, 2, 11, 0)
        self.task_manager.update_task.return_value = True
        self.cli.run()
        self.task_manager.update_task.assert_called_with(1, "Updated Title", "Updated Desc", "medium", ["newtag1", "newtag2"], due_date, "weekly")
        self.assertIn("Task updated successfully!", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['3', '99', 'Any Title', 'Any Desc', 'medium', '', '', '', '7'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_update_task_not_found(self, mock_stdout, mock_input):
        self.task_manager.update_task.return_value = False
        self.cli.run()
        self.assertIn("Task not found.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['4', '1', '7'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_delete_task_flow(self, mock_stdout, mock_input):
        self.task_manager.delete_task.return_value = True
        self.cli.run()
        self.task_manager.delete_task.assert_called_with(1)
        self.assertIn("Task deleted successfully!", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['4', '99', '7'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_delete_task_not_found(self, mock_stdout, mock_input):
        self.task_manager.delete_task.return_value = False
        self.cli.run()
        self.assertIn("Task not found.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['5', '1', '7'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_toggle_complete_flow(self, mock_stdout, mock_input):
        self.task_manager.toggle_task_completion.return_value = True
        self.cli.run()
        self.task_manager.toggle_task_completion.assert_called_with(1)
        self.assertIn("Task completion status updated!", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['5', '99', '7'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_toggle_complete_not_found(self, mock_stdout, mock_input):
        self.task_manager.toggle_task_completion.return_value = False
        self.cli.run()
        self.assertIn("Task not found.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['8', '7'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_main_menu_choice(self, mock_stdout, mock_input):
        self.cli.run()
        self.assertIn("Invalid choice. Please try again.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['6', '1', 'keyword', '6', '7'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_search_by_keyword_flow(self, mock_stdout, mock_input):
        self.cli.run()
        self.task_manager.search_tasks.assert_called_with('keyword')
        self.assertIn("--- Your Tasks ---", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['6', '2', 'y', '6', '7'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_filter_by_status_flow(self, mock_stdout, mock_input):
        self.cli.run()
        self.task_manager.filter_tasks_by_status.assert_called_with(True)
        self.assertIn("--- Your Tasks ---", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['6', '3', 'high', '6', '7'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_filter_by_priority_flow(self, mock_stdout, mock_input):
        self.cli.run()
        self.task_manager.filter_tasks_by_priority.assert_called_with('high')
        self.assertIn("--- Your Tasks ---", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['6', '4', 'work', '6', '7'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_filter_by_tag_flow(self, mock_stdout, mock_input):
        self.cli.run()
        self.task_manager.filter_tasks_by_tag.assert_called_with('work')
        self.assertIn("--- Your Tasks ---", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['6', '5', '1', '3', '6', '7'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_sort_by_priority_flow(self, mock_stdout, mock_input):
        self.cli.run()
        self.task_manager.sort_tasks_by_priority.assert_called_once()
        self.assertIn("--- Your Tasks ---", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['6', '5', '2', '3', '6', '7'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_sort_by_title_flow(self, mock_stdout, mock_input):
        self.cli.run()
        self.task_manager.sort_tasks_by_title.assert_called_once()
        self.assertIn("--- Your Tasks ---", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['6', '5', '4', '3', '6', '7'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_sort_menu_choice(self, mock_stdout, mock_input):
        self.cli.run()
        self.assertIn("Invalid choice. Please try again.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['6', '7', '7'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_search_filter_menu_choice(self, mock_stdout, mock_input):
        self.cli.run()
        self.assertIn("Invalid choice. Please try again.", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['7']) # Exit immediately
    @patch('sys.stdout', new_callable=StringIO)
    @patch('src.cli.datetime') # Mock datetime to control now()
    def test_reminder_display(self, mock_datetime, mock_stdout, mock_input):
        # Setup overdue task
        overdue_task = Task(1, "Overdue Task", due_date=datetime(2025, 1, 1, 0, 0))
        self.task_manager.get_all_tasks.return_value = [overdue_task]
        
        # Set a fixed 'now' for consistent testing
        mock_datetime.now.return_value = datetime(2026, 1, 1, 0, 0)
        mock_datetime.side_effect = lambda *args, **kw: datetime(*args, **kw) # Allow normal datetime object creation
        mock_datetime.timedelta = timedelta # Ensure timedelta also works if needed

        self.cli.run()
        output = mock_stdout.getvalue()
        self.assertIn("!!! REMINDER: OVERDUE TASKS !!!", output)
        self.assertIn("ID: 1, Title: Overdue Task", output)

if __name__ == '__main__':
    unittest.main()