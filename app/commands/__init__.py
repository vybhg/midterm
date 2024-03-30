from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class NoSuchCommandError(Exception):
    pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command_class):
        self.commands[command_name] = command_class

    def execute_command(self, command_name: str, *args):
        try:
            command_class = self.commands[command_name]
            command_instance = command_class()
            command_instance.execute(*args)
        except KeyError:
            raise NoSuchCommandError(f"No such command: {command_name}")
