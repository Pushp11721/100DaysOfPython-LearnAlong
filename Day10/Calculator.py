import art

#define all operations
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

#Create a dictionary for all 4 function with their keys
operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
    print(art.calc_diag)
    should_accumulate = True
    # ask to enter first number
    num1 = float(input("What is the first number : "))
    while should_accumulate:
        # print operation
        for symbol in operations:
            print(symbol)
        # pick operation
        operation_symbol = input("Pick an operation : ")
        # ask for second number
        num2 = float(input("what is the next number : "))

        # example
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # ask to continue or not
        choice = input(f"Type 'Y' to continue with {answer}, or type 'N' to start a new calculation : ").lower()

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 50)
            calculator()

calculator()