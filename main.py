

print('''

 _____________________
|  _________________  |
| |   Simple Calc.  | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|



''')


def add(n1, n2):
   
    return n1 + n2


def subtract(n1, n2):
   
    return n1 - n2


def multiply(n1, n2):
    
    return n1 * n2


def divide(n1, n2):
    
    return n1 / n2


operations = {

    "+": add,

    "-": subtract,
   
    "/": divide,
  
    "*": multiply,

}

def calculator():

    num1 = float(input("What is the first number?"))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:

        operation_sym = input("Pick an operation:-  ")

        num2 = float(input("What is the next number?"))

        caclculation_fn = operations[operation_sym]

        answer = caclculation_fn(num1, num2)

        print(f"The answer is :- {num1} {operation_sym} {num2} = {answer}")


        if input(f"Type 'y' to continue wit the {answer}, or type 'n' to restart again. :- ") == "y":

            num1 = answer

        else:

            should_continue = False

            calculator()


calculator()

