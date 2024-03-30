from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, args):
        pass

class NoSuchCommandError(Exception):
    pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name, command_class):
        self.commands[command_name] = command_class

    def execute_command(self, command_name, *args):
        try:
            command_class = self.commands.get(command_name)
            if command_class:
                command_instance = command_class()
                command_instance.execute(args)
            else:
                raise NoSuchCommandError(f"No such command: {command_name}")
        except NoSuchCommandError as e:
            print(e)

   


