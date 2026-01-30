def midpoint(num1, num2):
    return (num1 + num2) / 2
def squareroot(num): 
    return num ** 0.5
def exponentiate(x, y):
    return x ** y
def maximum(a, b):
    return max(a, b)
def minimum(a, b):
    return min(a, b)
def squareroot(num): 
    return num ** 0.5

def exponentiate(x, y):
    return x ** y

def maximum(a, b):
    return max(a, b)

def minimum(a, b):
    return min(a, b)


if __name__ == "__main__":
    # Demo / interactive behavior when run directly
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = midpoint(num1, num2)
    print(f"\nThe midpoint between {num1} and {num2} is: {result}")

    number = float(input("Enter a number to find its squareroot: "))
    result = squareroot(number)
    print(f"The squareroot of {number} is: {result}")

    x = float(input("Enter the base number: "))
    y = float(input("Enter the exponent: "))
    result = exponentiate(x, y)
    print(f"{x} raised to the power of {y} is: {result}")

    a = float(input("Enter the first number for max/min: "))
    b = float(input("Enter the second number for max/min: "))
    result = maximum(a, b)
    print(f"The maximum between {a} and {b} is: {result}")
    result = minimum(a, b)
    print(f"The minimum between {a} and {b} is: {result}")
