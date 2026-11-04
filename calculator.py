def add(a,b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Cannot divided by Zero!..."
    else:
        return a / b
    
a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))
print("\n Choose an operation:")
print(" 1. Addition(+)")
print(" 2.Subtraction(-)")
print(" 3.Multiplication(*)")
print(" 4.Division(/)")

choice = input("Enter the operation = (1 - 4) or '+' or '-'or '*' '/': ").strip()
if choice == "1" or choice == "+":
    result = add(a, b)
elif choice == "2" or choice == "-":
    result = subtract(a, b)
elif choice == "3" or choice == "*":
    result = multiply(a, b)
elif choice == "4" or choice == "/": 
    result = divide(a, b)
else:
    result = "Error: Wrong Input!..."

print("Result: ", result)