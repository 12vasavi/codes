from art import logo

# Function for addition
def add(n1, n2):
    return n1 + n2

# Function for subtraction
def subtract(n1, n2):
    return n1 - n2

# Function for multiplication
def multiply(n1, n2):
    return n1 * n2

# Function for division
def divide(n1, n2):
    return n1 / n2

# Dictionary containing the operator symbols and corresponding functions
operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Main calculator function
def calculator():
    print(logo)
    
    # Get the first number from the user
    num1 = float(input("What is the first number? "))

    # Display the available operators
    for key in operators:
        print(key)

    should_continue = True

    # Loop for multiple calculations until the user decides to stop
    while should_continue:
        operation = input("Pick an operation: ")  # Get the operator symbol from the user
        num2 = float(input("What is the next number? "))  # Get the second number from the user

        # Retrieve the corresponding function from the dictionary based on the operator symbol
        calculation_function = operators[operation]
        
        # Perform the calculation using the selected operator function
        result = calculation_function(num1, num2)

        print(f"{num1} {operation} {num2} = {result}")

        # Check if the user wants to continue with the last result or start a new calculation
        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == "y":
            num1 = result
        else:
            should_continue = False
            calculator()  # Call the calculator function again to start a new calculation

# Start the calculator
calculator()
