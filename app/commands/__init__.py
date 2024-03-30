from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandNotFoundError(Exception):
    pass

class CommandHandler:
    def __init__(self):
        self.commands_mapping = {}

    def register_command(self, command_name: str, command_class):
        self.commands_mapping[command_name] = command_class

    def execute_command(self, command_name: str, *args):
        try:
            command_class = self.commands_mapping[command_name]
            command_instance = command_class()
            command_instance.execute(*args)
        except KeyError:
            raise CommandNotFoundError(f"No such command: {command_name}")





