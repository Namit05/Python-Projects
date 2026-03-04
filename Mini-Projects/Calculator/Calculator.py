import art
def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": sub, "*": multiply, "/": divide}
def calculator() :
    print(art.logo)
    should_accumulate=True
    a = float(input("Enter first number :"))
    while should_accumulate:
        for operators in operations:
            print(operators)
        operator = input("Choose the operation you want to perform (+,-,*,/) :")
        b = float(input("Enter second number :"))
        answer = operations[operator](a, b)
        print(f"{a} {operator} {b} = {answer}")

        choice=input(f"Type 'y' if you want to continue with {answer}, or type 'no' to start new calculation :")
        
        if choice=='y' :
            a=answer
        else :
            should_accumulate=False
            print("\n"*5)
            calculator() #recursion
calculator()
