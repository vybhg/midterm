# **Midterm Project.**

**1. Design Patterns Used:**
**a. Command Pattern:** The Command Pattern encapsulates a request as an object, thereby allowing parameterization of clients with different requests, queuing, logging, and supporting undoable operations. It promotes loose coupling between the sender and receiver of a request. The classes Command, CommandHandler, and concrete command classes like AdditionCommand, SubtractionCommand, etc., demonstrate the Command Pattern.
Here is the link to the implementation of the Command Pattern in the code: https://github.com/vybhg/midterm/blob/main/app/commands/__init__.py
```
b.Factory pattern:The Factory Pattern is employed within the AppFactory class to dynamically generate instances of command objects based on specified packages. This pattern abstracts the process of object creation, allowing the client code (in this case, the AppFactory) to create objects without needing to know the specific class or implementation details. By using the Factory Pattern, the code gains flexibility and extensibility, as new command objects can be added or modified without directly modifying the client code.
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
```
c.Facade Pattern:In the AppFacade class, the Facade Pattern is utilized to offer a simplified interface, perform_data_manipulation(), which hides the complexity of underlying Pandas data manipulation operations. This pattern provides a high-level, user-friendly interface that encapsulates multiple steps or operations into a single method call. By using the Facade Pattern, the codebase becomes more organized, easier to understand, and less coupled to the intricacies of Pandas data manipulation, promoting better maintainability and readability.
*Code snipped:*

```python
class AppFacade:
    @staticmethod
    def perform_data_manipulation(data):
        # Perform complex Pandas data manipulations here
        # This could involve operations like filtering, transformation, aggregation, etc.
        pass
    ```

**2. Environment Variables Usage:**an example of using environment variables can be seen where a method getEnvironmentVariable()
```python
def getEnvironmentVariable(self, envvar: str = 'ENVIRONMENT'):
   return self.settings[envvar]
```
**3. Logging:**logging is used to record various events such as user choices in the menu, execution of commands, errors, etc. The logging module is imported and used to create logs.
Here is the link to the implementation of the logging  in thecode: https://github.com/vybhg/midterm/tree/main/logs

b. Setup the python environment

```python
sudo apt update -y
sudo apt install python3-pip
pip3 --version
(the above commands will update the wsl-2 and installs the python-3 packages)
pip3 install virtualenv (This command will install virtual environment)
virtualenv venv (This command will create a virtual environment venu)
source ./venv/bin/activate (This command will activate the virtual environment.)
pip3 install -r requirments.txt (This command will install all the required packages)
pytest (Runs the tests)
pytest --pylint  (Runs tests with pylint static code analysis)
pytest --pylint --cov (Runs tests, pylint, and coverage to check if you have all your code tested.)
python3 main.py 
```
5.video demonstration of using the calculator:https://njit0-my.sharepoint.com/:v:/g/personal/vg498_njit_edu/EVc9n5omwTBFm7OgckQaOtoBTltSv09cb4KUxQK5uFJHMA?e=vlGeKH
