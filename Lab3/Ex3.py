#The program takes a number and returns the squareroot of that number
#Name: Harrison Phan
#Date: 2024-02-05

def squareroot(num): 
    return num ** 0.5

number = float(input("Enter a number to find its squareroot: "))
result = squareroot(number)
print(f"The squareroot of {number} is: {result}")
