import pytest
from unittest.mock import MagicMock
from app.commands import CommandHandler, Command, NoSuchCommandError

# Define a mock command class for testing
class MockCommand(Command):
    def execute(self):
        return "Mock Command Executed"
def test_register_command():
    # Arrange
    handler = CommandHandler()
    mock_command = MockCommand()
    # Act
    handler.register_command('mock', mock_command)
    # Assert
    assert 'mock' in handler.commands
    assert handler.commands['mock'] == mock_command
def test_execute_command_nonexistent():
    # Arrange
    handler = CommandHandler()
    # Act & Assert
    with pytest.raises(NoSuchCommandError):
        handler.execute_command('nonexistent')
if __name__ == '__main__':
    pytest.main()




import unittest
from unittest.mock import patch, MagicMock
from app.commands import Command, CommandHandler, NoSuchCommandError
from app import App
class MockCommand(Command):
    def execute(self):
        pass

class TestCommandHandler(unittest.TestCase):
    def test_register_command(self):
        handler = CommandHandler()
        handler.register_command("mock_command", MockCommand)
        self.assertTrue("mock_command" in handler.commands)

    def test_execute_command(self):
        handler = CommandHandler()
        mock_command = MagicMock(spec=Command)
        handler.register_command("mock_command", mock_command)
        handler.execute_command("mock_command")
        mock_command().execute.assert_called_once()

class TestApp(unittest.TestCase):
    def test_get_environment_variable(self):
        app = App()
        self.assertEqual(app.getEnvironmentVariable(), "TESTING")

    @patch('builtins.input', side_effect=['exit'])
    def test_start_exit_command(self, mock_input):
        pass

    @patch('builtins.input', side_effect=['menu', 'exit'])
    @patch('app.plugins.menu.MenuCommand')  # Mocking MenuCommand
    def test_start_menu_command(self, mock_menu_command, mock_input):
        pass

    @patch('builtins.input', side_effect=['some_command', 'exit'])
    def test_start_execute_command(self, mock_input):
        pass

if __name__ == '__main__':
    unittest.main()

