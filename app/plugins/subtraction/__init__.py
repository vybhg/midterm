from app.commands import Command

class SubtractionCommand(Command):
    def execute(self, args):
        if args:
            a = float(args[0])
            b = float(args[1])
            result = a - b  # Perform subtraction
            return result  # Return the result
        else:
            print("Nothing to subtract")
            return None  # Return None if no arguments are provided
