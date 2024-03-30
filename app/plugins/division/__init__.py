from app.commands import Command

class DivisionCommand(Command):
    def execute(self, args):
        if args:
            try:
                a = float(args[0])
                b = float(args[1])
                if b != 0:
                    result = a / b
                    return result
                else:
                    print("Error: Division by zero is not allowed")
            except (ValueError, ZeroDivisionError, IndexError):
                print("Error: Please provide two valid numbers as arguments.")
        else:
            print("Error: No numbers provided for division")
