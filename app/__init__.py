import os
import pkgutil
import importlib
import sys
import logging
from abc import ABC, abstractmethod
from dotenv import load_dotenv
from app.plugins.menu import MenuCommand
import warnings
from app.plugins.claculation_history import claculation_history

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.resetwarnings()

# Ensure the 'logs' directory exists
log_dir = os.path.join(os.getcwd(), 'logs')
os.makedirs(log_dir, exist_ok=True)

# Configure logging
log_file = os.path.join(log_dir, 'app.log')
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command_class):
        self.commands[command_name] = command_class

    def create_command(self, command_name: str):
        if command_name in self.commands:
            return self.commands[command_name]()
        else:
            logger.error(f"No such command: {command_name}")
            return None

    def execute_command(self, command_name: str):
        command = self.create_command(command_name)
        if command:
            command.execute()

class AppFacade:
    @staticmethod
    def perform_data_manipulation(data):
        # Perform complex Pandas data manipulations here
        # This could involve operations like filtering, transformation, aggregation, etc.
        pass

class AppFactory:
    @staticmethod
    def create_command_objects():
        commands = {}
        plugins_packages = [
            'app.plugins.addition',
            'app.plugins.subtraction',
            'app.plugins.multiplication',
            'app.plugins.division'
        ]
        for plugins_package in plugins_packages:
            for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
                if is_pkg:  
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    for item_name in dir(plugin_module):
                        item = getattr(plugin_module, item_name)
                        try:
                            if issubclass(item, Command):  
                                commands[plugin_name] = item
                        except TypeError:
                            continue
        return commands

class App:
    def __init__(self):
        load_dotenv()
        self.settings = {}
        for key, value in os.environ.items():
            self.settings[key] = value
        self.settings.setdefault('ENVIRONMENT', 'TESTING')
        self.command_handler = CommandHandler()
        self.history_manager = claculation_history()

    def getEnvironmentVariable(self, envvar: str = 'ENVIRONMENT'):
        return self.settings[envvar]
    
    def load_plugins(self):
        commands = AppFactory.create_command_objects()
        for command_name, command_class in commands.items():
            self.command_handler.register_command(command_name, command_class)

    def start(self):
        self.load_plugins()
        logger.info("Application started.")
        print("Type 'menu to get menu.")
        while True:
            user_input = input(">>> ").strip()
            if user_input.lower() == 'menu':
                logger.info("Menu command executed.")
                MenuCommand(self.history_manager).execute([])  # Pass history_manager to MenuCommand
            else:
                self.command_handler.execute_command(user_input)

if __name__ == "__main__":
    app = App()
    try:
        app.start()
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        sys.exit(1)