from art import logo
exec_continue = True
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
valid_operators=["+","-","*","/"]
while exec_continue == True:
    num1=float(input("What is your first number?: "))
    num2=float(input("What is your second number?: "))
    
    for key in operations:
        print(key)
    operation_symbol=input("pick an operation from above options: ")
    if operation_symbol in valid_operators:
        calculation_function = operations[operation_symbol]
        result= calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
    else:
        print("It is not a valid operator")
    choice=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if choice == "n":
        exec_continue = False
  