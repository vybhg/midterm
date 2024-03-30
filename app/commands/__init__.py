import pandas as pd

class CalculationHistory:
    def __init__(self):
        self.history = pd.DataFrame()

    def add_entry(self, operation, num1, num2, result):
        """
        Add a new entry to the calculation history.

        Args:
        - operation: str, the type of operation (e.g., 'Addition', 'Subtraction', etc.).
        - num1: float, the first number used in the operation.
        - num2: float, the second number used in the operation.
        - result: float, the result of the operation.
        """
        new_entry = pd.DataFrame({'Operation': [operation], 'Number1': [num1], 'Number2': [num2], 'Result': [result]})
        self.history = pd.concat([self.history, new_entry], ignore_index=True)

    def display_history(self):
        """
        Display the calculation history.
        """
        print(self.history)

    def save_history(self, filename):
        """
        Save the calculation history to a CSV file.

        Args:
        - filename: str, the name of the CSV file to save.
        """
        if not filename.endswith('.csv'):
            filename += '.csv'
        self.history.to_csv(filename, index=False)
        print(f"History saved to {filename}.")

    def clear_history(self):
        """
        Clear the calculation history.
        """
        self.history = pd.DataFrame(columns=['Operation', 'Number1', 'Number2', 'Result'])
        print("History cleared.")

    def delete_entry(self, index):
        """
        Delete an entry from the calculation history.

        Args:
        - index: int, the index of the entry to delete.
        """
        try:
            self.history.drop(index, inplace=True)
            print("Entry deleted.")
        except KeyError:
            print("Invalid index. Entry does not exist.")


