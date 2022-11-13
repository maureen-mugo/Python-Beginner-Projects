# function to add
def add(n1, n2):
  return n1 + n2

# function to subtract
def subtract(n1, n2):
  return n1 - n2

# function to multiply
def multiply(n1, n2):
  return n1 * n2

# function to divide
def divide(n1, n2):
  return n1 / n2

# arithemetic operations
operations = {
                "+": add,
                "-": subtract,
                "*": multiply,
                "/": divide
            }

# function to calculate and display the output of the calculation
def calculator():
    calculate = True
    while calculate:
        num1 = float(input("What's the first number?: "))
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        if operation_symbol not in operations:
            print("Wrong symbol!")  
            continue
        

        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        calculate_again = False
        while  not calculate_again:
            again = input("Do you want to continue calculating(yes, no)? ")
            if again.lower() == "yes":
                calculate = True
            elif again.lower() == "no":
                calculate = False
                break
            else:
                calculate = False
                break


calculator()

