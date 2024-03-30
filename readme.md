# **Midterm Project.**

**1. Design Patterns Used:**

**a. Command Pattern:** Implemented in the Command and CommandHandler classes, providing a way to encapsulate requests as objects, allowing parameterization of clients with queues, and supporting undoable operations.

*Code snipped:*

```python
from abc import ABC, abstractmethod
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
class CommandHandler:
    def __init__(self):
        self.commands = {}
    def register_command(self, command_name: str, command_class):
        self.commands[command_name] = command_class
    def execute_command(self, command_name: str):
        command = self.create_command(command_name)
        if command:
            command.execute()
```
**b. Factory Pattern:** Utilized in the AppFactory class to dynamically create instances of command objects based on specified packages.

*Code snipped:*
```python
import pkgutil
import importlib
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
        return commands ```

*c. Facade Pattern:* Applied in the AppFacade class to provide a simplified interface (perform_data_manipulation()) to complex operations (Pandas data manipulation).

*Code snipped:*

```python
class AppFacade:
    @staticmethod
    def perform_data_manipulation(data):
        # Perform complex Pandas data manipulations here
        # This could involve operations like filtering, transformation, aggregation, etc.
        pass
    ```