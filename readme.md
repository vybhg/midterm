# **Midterm Project.**

**1. Design Patterns Used:**
**a. Command Pattern:** The Command Pattern encapsulates a request as an object, thereby allowing parameterization of clients with different requests, queuing, logging, and supporting undoable operations. It promotes loose coupling between the sender and receiver of a request. The classes Command, CommandHandler, and concrete command classes like AdditionCommand, SubtractionCommand, etc., demonstrate the Command Pattern.
Here is the link to the implementation of the Command Pattern in the code: https://github.com/vybhg/midterm/blob/main/app/commands/__init__.py
```
**b. Factory Pattern:** The Factory Pattern is employed within the AppFactory class to dynamically generate instances of command objects based on specified packages. This pattern abstracts the process of object creation, allowing the client code (in this case, the AppFactory) to create objects without needing to know the specific class or implementation details. By using the Factory Pattern, the code gains flexibility and extensibility, as new command objects can be added or modified without directly modifying the client code.

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

*c. Facade Pattern:* In the AppFacade class, the Facade Pattern is utilized to offer a simplified interface, perform_data_manipulation(), which hides the complexity of underlying Pandas data manipulation operations. This pattern provides a high-level, user-friendly interface that encapsulates multiple steps or operations into a single method call. By using the Facade Pattern, the codebase becomes more organized, easier to understand, and less coupled to the intricacies of Pandas data manipulation, promoting better maintainability and readability.

*Code snipped:*

```python
class AppFacade:
    @staticmethod
    def perform_data_manipulation(data):
        # Perform complex Pandas data manipulations here
        # This could involve operations like filtering, transformation, aggregation, etc.
        pass
    ```
