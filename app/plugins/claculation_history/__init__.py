import pandas as pd

class claculation_history:
    def __init__(self):
        self.history = pd.DataFrame()

    def add_entry(self, operation, num1, num2, result):
        new_entry = pd.DataFrame({'Operation': [operation], 'Number1': [num1], 'Number2': [num2], 'Result': [result]})
        if self.history.empty:
            self.history = new_entry
        else:
            self.history = pd.concat([self.history, new_entry], ignore_index=True)

    def display_history(self):
        print(self.history)

    def save_history(self, filename):
        if not filename.endswith('.csv'):
            filename += '.csv'
        self.history.to_csv(filename, index=False)
        print(f"History saved to {filename}.")

    def clear_history(self):
        self.history = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])
        print("History cleared.")

    def delete_entry(self, index):
        try:
            self.history.drop(index, inplace=True)
            print("Entry deleted.")
        except KeyError:
            print("Invalid index. Entry does not exist.")
