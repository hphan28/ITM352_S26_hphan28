def midpoint(num1, num2):
    return (num1 + num2) / 2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = midpoint(num1, num2)
print(f"\nThe midpoint between {num1} and {num2} is: {result}")

def squareroot(num): 
    return num ** 0.5

number = float(input("Enter a number to find its squareroot: "))
result = squareroot(number)
print(f"The squareroot of {number} is: {result}")

def exponentiate(x, y):
    return x ** y

x = float(input("Enter the base number: "))
y = float(input("Enter the exponent: "))

result = exponentiate(x, y)
print(f"{x} raised to the power of {y} is: {result}")

def maximum(a, b):
    return max(a, b)

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

result = maximum(a, b)
print(f"The maximum between {a} and {b} is: {result}")

def minimum(a, b):
    return min(a, b)

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

result = minimum(a, b)
print(f"The minimum between {a} and {b} is: {result}")
