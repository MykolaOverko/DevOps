class Calculator:
    def __init__(self):
        self.operations = {}

    def add_operation(self, operation):
        operation_name = operation.get_name()
        self.operations[operation_name] = operation

    def calculate(self, operand1, operand2, operation_name):
        if operation_name in self.operations:
            operation = self.operations[operation_name]
            result = operation.execute(operand1, operand2)
            return result
        else:
            raise ValueError(f"Operation '{operation_name}' is not supported.")