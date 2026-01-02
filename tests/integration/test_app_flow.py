import unittest
from unittest.mock import patch
from io import StringIO
from src.app import main

class TestAppFlow(unittest.TestCase):

    @patch('builtins.input', side_effect=[
        '1', 'Buy groceries', 'Milk, eggs, bread',  # Add task 1
        '1', 'Pay bills', 'Electricity, internet',  # Add task 2
        '2',                                      # View all tasks
        '5', '1',                                 # Mark task 1 complete
        '3', '2', 'Pay all bills', 'Electricity, internet, water', # Update task 2
        '2',                                      # View all tasks again
        '4', '1',                                 # Delete task 1
        '2',                                      # View all tasks last time
        '7'                                       # Exit
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_full_basic_flow(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()

        # Verify task added
        self.assertIn("Task added successfully!", output)
        self.assertIn("[ ] ID: 1, Title: Buy groceries, Description: Milk, eggs, bread", output)
        self.assertIn("[ ] ID: 2, Title: Pay bills, Description: Electricity, internet", output)

        # Verify task 1 marked complete
        self.assertIn("Task completion status updated!", output)
        
        # Verify task 2 updated
        self.assertIn("Task updated successfully!", output)
        self.assertIn("[ ] ID: 2, Title: Pay all bills, Description: Electricity, internet, water", output)

        # Verify task 1 deleted
        self.assertIn("Task deleted successfully!", output)
        self.assertNotIn("[ ] ID: 1, Title: Buy groceries", output)
        
        # Verify exit
        self.assertIn("Exiting application. Goodbye!", output)

if __name__ == '__main__':
    unittest.main()
