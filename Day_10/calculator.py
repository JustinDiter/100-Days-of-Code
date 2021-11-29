# arithmetic functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# dictionary to store the functions to be called when the user inputs the corresponding key
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    # first number the user wants to use for calculation
    num1 = float(input("What's the first number ?: "))
    # loop flag
    should_continue = True

    while should_continue:
        for operation in operations:
            print(operation)
        # user chooses the operation symbol for the arithmetic they want to perform from the list
        operation_symbol = input("Pick an operation from the list above: ")

        num2 = float(input("What's the next number ?: "))
        # if operation symbol matches dictionary key, perform function associated to key with the numbers as inputs
        for operation in operations:
            if operation_symbol == operation:
                answer = operations[operation](n1=num1, n2=num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        # allows user to futher calculate or start new calculation
        response_continue = input("Would you like to further calculate with {answer} ? If yes, type 'y', or type 'n' to start a new calculation\n").lower()
        if response_continue == "y":
            num1 = answer
        else:
            should_continue = False
            # recursion allowing new calculation
            calculator()

calculator()
