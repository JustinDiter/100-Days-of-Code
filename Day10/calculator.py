# The basic arithmetic functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Dictionary to store the functions in to use in relation to user input
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    num1 = int(input("What's the first number ?: "))
    # loop flag
    should_continue = True
    
    while should_continue:
        # prints the keys in the operation dictionary so that the user knows the list of possible operations they can choose from
        for operation in operations:
            print(operation)
        
        operation_symbol = input("Pick an operation from the list above: ")
        
        num2 = int(input("What's the next number ?: "))
        # goes through the dictionary and calls the correct function for the choice that the user made, while inputing the numbers into the function
        for operation in operations:
            if operation_symbol == operation:
                answer = operations[operation](n1=num1, n2=num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        # allows user to have multiple steps of a calculation or to start a new one
        response_continue = input("Would you like to further calculate with {answer} ? If yes, type 'y', or type 'n' to start a new calculation\n").lower()
        if response_continue == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
