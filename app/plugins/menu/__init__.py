import sys
import logging

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class MenuCommand(Command):
    def __init__(self, history_manager):
        self.history_manager = history_manager

    def execute(self, args):
        print("Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Display History")
        print("6. Save History")
        print("7. Clear History")
        print("8. Delete Entry")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = AdditionCommand().execute([num1, num2])
            print("Result:", result)
            self.history_manager.add_entry('Addition', num1, num2, result)
        elif choice == "2":
            # Implement Subtraction logic
            pass
        # Implement other menu options

# Main application loop
def main():
    command_handler = CommandHandler()
    history_manager = CalculationHistory()

    # Register commands with command handler
    command_handler.register_command("menu", MenuCommand)
    command_handler.register_command("add", AdditionCommand)
    command_handler.register_command("subtract", SubtractionCommand)
    command_handler.register_command("multiply", MultiplicationCommand)
    command_handler.register_command("divide", DivisionCommand)

    while True:
        user_input = input("Enter command (menu/add/subtract/multiply/divide/exit): ")
        if user_input.lower() == 'exit':
            print("Exiting...")
            sys.exit()
        command_handler.execute_command(user_input, history_manager)

if __name__ == "__main__":
    main()

          
            

       
