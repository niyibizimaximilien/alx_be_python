# File: fns_and_dsa/arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform basic arithmetic operations.

    Parameters:
    - num1 (float): First number
    - num2 (float): Second number
    - operation (str): One of 'add', 'subtract', 'multiply', 'divide'

    Returns:
    - Result of the operation or a specific message if an error occurs
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
