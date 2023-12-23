import tkinter as tk
from operations.addition import Addition
from operations.subtraction import Subtraction
from operations.multiplication import Multiplication
from operations.division import Division
from calculator import Calculator

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.calculator = Calculator()

        self.create_gui()

    def create_gui(self):
        self.entry = tk.Entry(self.root, width=20, font=("Arial", 14))
        self.entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'  
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.root, text=button, width=5, height=2, command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        current_text = self.entry.get()

        if button == '=':
            try:
                result = eval(current_text)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif button == 'C':
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, button)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
