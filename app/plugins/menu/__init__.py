import sys
import logging
from app.commands import Command
from app.plugins.addition import AdditionCommand
from app.plugins.subtraction import SubtractionCommand
from app.plugins.multiplication import MultiplicationCommand
from app.plugins.division import DivisionCommand
import sys
from app.commands import Command

# Configure logging
import logging
logger = logging.getLogger(__name__)

class MenuCommand(Command):
    def __init__(self, history_manager):
        self.history_manager = history_manager

    def execute(self, args):
        logger.info("Menu command executed.")
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
        logger.info(f"User choice: {choice}")
        
        if choice == "1":
            logger.info("User chose Addition")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = AdditionCommand().execute([num1, num2])  # Call execute method of AdditionCommand
            print("result of addition is ", result)
            self.history_manager.add_entry('Addition', num1, num2, result)
            logger.info("Addition operation performed.")
            
        elif choice == "2":
            logger.info("User chose Subtraction")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = SubtractionCommand().execute([num1, num2])  # Call execute method of SubtractionCommand
            print("result of subtraction is ", result)
            self.history_manager.add_entry('Subtraction', num1, num2, result)
            logger.info("Subtraction operation performed.")
            
        elif choice == "3":
            logger.info("User chose Multiplication")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = MultiplicationCommand().execute([num1, num2])  # Call execute method of MultiplicationCommand
            print("result of multiplication is ", result)
            self.history_manager.add_entry('Multiplication', num1, num2, result)
            logger.info("Multiplication operation performed.")
           
        elif choice == "4":
            logger.info("User chose Division")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = DivisionCommand().execute([num1, num2])  # Call execute method of DivisionCommand
            print("result of division is ", result)
            self.history_manager.add_entry('Division', num1, num2, result)
            logger.info("Division operation performed.")
            
        elif choice == "5":
            logger.info("User chose to display history")
            self.history_manager.display_history()

        elif choice == "6":
            logger.info("User chose to save history")
            filename = input("Enter filename to save history: ")
            self.history_manager.save_history(filename)

        elif choice == "7":
            logger.info("User chose to clear history")
            confirm = input("Are you sure you want to clear the history? (y/n): ")
            if confirm.lower() == 'y':
                self.history_manager.clear_history()
                print("History cleared successfully.")
                logger.info("History cleared.")
            else:
                print("Operation cancelled.")

        elif choice == "8":
            logger.info("User chose to delete entry")
            index = int(input("Enter index of entry to delete: "))
            self.history_manager.delete_entry(index)

        elif choice == "9":
            logger.info("User chose to exit")
            print("Exiting...")
            sys.exit()

       
