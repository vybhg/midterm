from abc import ABC, abstractmethod

class Command(ABC):
    """Abstract base class for commands."""
    
    @abstractmethod
    def execute(self, *args):
        """Abstract method to execute the command."""
        pass

class NoSuchCommandError(Exception):
    """Exception raised when a command is not found."""
    
    def __init__(self, command_name):
        super().__init__(f"No such command: {command_name}")

class CommandHandler:
    """Class to handle registration and execution of commands."""
    
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command_class):
        """Register a command with the handler."""
        self.commands[command_name] = command_class

    def execute_command(self, command_name: str, *args):
        """Execute a registered command."""
        try:
            command_class = self.commands[command_name]
            command_instance = command_class()
            command_instance.execute(*args)
        except KeyError:
            raise NoSuchCommandError(command_name)

def main():
    # Example usage of the CommandHandler class
    handler = CommandHandler()
    handler.register_command("my_command", MyCommandClass)
    handler.execute_command("my_command", arg1, arg2)

if __name__ == "__main__":
    main()



