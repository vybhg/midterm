from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        """Execute the command."""
        pass

class NoSuchCommandError(Exception):
    """Custom exception for handling missing commands."""
    pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command_class):
        """Register a command with its corresponding class."""
        self.commands[command_name] = command_class

    def execute_command(self, command_name: str, *args):
        """Execute the specified command."""
        try:
            command_class = self.commands.get(command_name)
            if command_class:
                command_instance = command_class()
                command_instance.execute(*args)
            else:
                raise NoSuchCommandError(f"No such command: {command_name}")
        except Exception as e:
            raise NoSuchCommandError(f"Error executing command: {str(e)}")

# Example usage:
class MyCustomCommand(Command):
    def execute(self):
        print("Executing MyCustomCommand!")

if __name__ == "__main__":
    handler = CommandHandler()
    handler.register_command("custom", MyCustomCommand)
    try:
        handler.execute_command("custom")
    except NoSuchCommandError as e:
        print(e)





