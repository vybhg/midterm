import unittest
import pandas as pd
from unittest.mock import MagicMock, patch
from io import StringIO
from app.plugins.addition import AdditionCommand
from app.plugins.subtraction import SubtractionCommand
from app.plugins.multiplication import MultiplicationCommand
from app.plugins.division import DivisionCommand
from app.commands import Command
from app.plugins.claculation_history import claculation_history
from app.plugins.menu import MenuCommand


class TestAdditionCommand(unittest.TestCase):
    def test_execute_with_args(self):
        """Test execute method with arguments."""
        command = AdditionCommand()
        result = command.execute(["2", "3"])
        self.assertEqual(result, 5.0)

    def test_execute_no_args(self):
        """Test execute method with no arguments."""
        command = AdditionCommand()
        result = command.execute([])
        self.assertIsNone(result)
        # You can also check if the expected message is printed
        # by capturing stdout using `unittest.mock.patch`

class TestSubtractionCommand(unittest.TestCase):
    def test_execute_with_args(self):
        """Test execute method with arguments."""
        command = SubtractionCommand()
        result = command.execute(["5", "3"])
        self.assertEqual(result, 2.0)

    def test_execute_no_args(self):
        """Test execute method with no arguments."""
        command = SubtractionCommand()
        result = command.execute([])
        self.assertIsNone(result)
        # You can also check if the expected message is printed
        # by capturing stdout using `unittest.mock.patch`


class TestMultiplicationCommand(unittest.TestCase):
    def test_execute_with_args(self):
        """Test execute method with arguments."""
        command = MultiplicationCommand()
        result = command.execute(["2", "3"])
        self.assertEqual(result, 6.0)

    def test_execute_no_args(self):
        """Test execute method with no arguments."""
        command = MultiplicationCommand()
        result = command.execute([])
        self.assertIsNone(result)
        # You can also check if the expected message is printed
        # by capturing stdout using `unittest.mock.patch`


class TestDivisionCommand(unittest.TestCase):
    def test_execute_with_args(self):
        """Test execute method with arguments."""
        command = DivisionCommand()
        result = command.execute(["6", "2"])
        self.assertEqual(result, 3.0)

    def test_execute_division_by_zero(self):
        """Test execute method with division by zero."""
        command = DivisionCommand()
        result = command.execute(["5", "0"])
        self.assertIsNone(result)
        # You can also check if the expected message is printed
        # by capturing stdout using `unittest.mock.patch`

    def test_execute_no_args(self):
        """Test execute method with no arguments."""
        command = DivisionCommand()
        result = command.execute([])
        self.assertIsNone(result)
        # You can also check if the expected message is printed
        # by capturing stdout using `unittest.mock.patch`



class TestClaculationHistory(unittest.TestCase):
    def setUp(self):
        self.history = claculation_history()

    def test_add_entry(self):
        self.history.add_entry('Addition', 2, 3, 5)
        self.assertEqual(len(self.history.history), 1)

    def test_display_history(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.history.add_entry('Addition', 2, 3, 5)
            self.history.display_history()
            self.assertIn("Addition", mock_stdout.getvalue())

    def test_save_history(self):
        filename = "test_history.csv"
        self.history.add_entry('Addition', 2, 3, 5)
        self.history.save_history(filename)
        data = pd.read_csv(filename)
        self.assertEqual(len(data), 1)

    def test_clear_history(self):
        self.history.add_entry('Addition', 2, 3, 5)
        self.history.clear_history()
        self.assertTrue(self.history.history.empty)

    def test_delete_entry(self):
        self.history.add_entry('Addition', 2, 3, 5)
        self.history.delete_entry(0)
        self.assertTrue(self.history.history.empty)


class TestMenuCommand(unittest.TestCase):
    def setUp(self):
        self.history_manager = claculation_history()

    def test_menu_command_addition(self):
        with patch('builtins.input', side_effect=['1', '2', '3', 'exit']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                menu_command = MenuCommand(self.history_manager)
                menu_command.execute([])
                self.assertIn("result of addition is", mock_stdout.getvalue())

    def test_menu_command_subtraction(self):
        with patch('builtins.input', side_effect=['2', '5', '3', 'exit']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                menu_command = MenuCommand(self.history_manager)
                menu_command.execute([])
                self.assertIn("result of subtraction is", mock_stdout.getvalue())

    def test_menu_command_multiplication(self):
        with patch('builtins.input', side_effect=['3', '2', '3', 'exit']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                menu_command = MenuCommand(self.history_manager)
                menu_command.execute([])
                self.assertIn("result of multiplication is", mock_stdout.getvalue())

    def test_menu_command_division(self):
        with patch('builtins.input', side_effect=['4', '6', '3', 'exit']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                menu_command = MenuCommand(self.history_manager)
                menu_command.execute([])
                self.assertIn("result of division is", mock_stdout.getvalue())

    def test_menu_command_display_history(self):
        with patch('builtins.input', side_effect=['5', 'exit']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                self.history_manager.add_entry('Addition', 2, 3, 5)
                menu_command = MenuCommand(self.history_manager)
                menu_command.execute([])
                self.assertIn("Addition", mock_stdout.getvalue())

    @patch('app.plugins.claculation_history.claculation_history.save_history')
    def test_menu_command_save_history(self, mock_save_history):
        with patch('builtins.input', side_effect=['6', 'test_history.csv', 'exit']):
            menu_command = MenuCommand(self.history_manager)
            menu_command.execute([])
            mock_save_history.assert_called_with('test_history.csv')

    @patch('app.plugins.claculation_history.claculation_history.clear_history')
    def test_menu_command_clear_history(self, mock_clear_history):
        with patch('builtins.input', side_effect=['7', 'y', 'exit']):
            self.history_manager.add_entry('Addition', 2, 3, 5)
            menu_command = MenuCommand(self.history_manager)
            menu_command.execute([])
            mock_clear_history.assert_called()

    @patch('app.plugins.claculation_history.claculation_history.delete_entry')
    def test_menu_command_delete_entry(self, mock_delete_entry):
        with patch('builtins.input', side_effect=['8', '0', 'exit']):
            self.history_manager.add_entry('Addition', 2, 3, 5)
            menu_command = MenuCommand(self.history_manager)
            menu_command.execute([])
            mock_delete_entry.assert_called_with(0)

    def test_menu_command_exit(self):
        with patch('builtins.input', side_effect=['9']):
            with self.assertRaises(SystemExit):
                menu_command = MenuCommand(self.history_manager)
                menu_command.execute([])


if __name__ == "__main__":
    unittest.main()
