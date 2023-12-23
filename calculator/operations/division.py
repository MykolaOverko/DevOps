class Division:
    def execute(self, operand1, operand2):
        if operand2 != 0:
            return operand1 / operand2
        else:
            return "Cannot divide by zero."

    def get_name(self):
        return "division"