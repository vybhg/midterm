# **Midterm Project.**

**1. Design Patterns Used:**
*a. Command Pattern:*In my implementation, I’ve used the Command Pattern for handling different commands within the application. The Command interface defines an execute() method, and concrete command classes implement this method.
You can find the implementation of the Command Pattern in my code here: 

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

**2. Environment Variables Usage:**
In my application, I load environment variables using the load_dotenv() function from the dotenv library. These variables are stored in the self.settings dictionary.
You can see how I load environment variables in my code here.

```python
def getEnvironmentVariable(self, envvar: str = 'ENVIRONMENT'):
   return self.settings[envvar]
```
**3. Logging:**
I configure logging using the logging module. I set up a log file (app.log) and log messages with timestamps, log levels, and custom messages.
You can find my logging setup in my code here: https://github.com/vybhg/midterm/tree/main/logs

**4.Exception Handling (LBYL and EAFP):**
a.LBYL
LBYL involves checking conditions before performing an action to prevent exceptions.
In my code, I use LBYL when checking if a command exists before executing it. 


```   def create_command(self, command_name: str):
    if command_name in self.commands:
        return self.commandscommand_name
    else:
        logger.error(f"No such command: {command_name}")
        return None
```
b.EAFP
EAFP encourages trying an action and handling exceptions if they occur.
In my code, I use EAFP when executing commands. If a command doesn’t exist, I catch the exception and log an error.
``` def execute_command(self, command_name: str):
    command = self.create_command(command_name)
    if command:
        command.execute()
```

    
**5.video demonstration of using the calculator:**
https://njit0-my.sharepoint.com/:v:/g/personal/vg498_njit_edu/EVc9n5omwTBFm7OgckQaOtoBTltSv09cb4KUxQK5uFJHMA?e=vlGeKH
