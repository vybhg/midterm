class AdditionCommand(Command):
    def execute(self, args):
        if args:
            try:
                a = float(args[0])
                b = float(args[1])
                result = a + b
                return result
            except (ValueError, IndexError):
                print("Please provide two valid numbers as arguments.")
        else:
            print("No numbers provided to add.")
