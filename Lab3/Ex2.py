#This program takes two numbers as input and returns their value halfway between them
#Name: Harrison Phan
#Date: 2024-02-05

def midpoint(num1, num2):
    return (num1 + num2) / 2

# Get input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate and display the midpoint
result = midpoint(num1, num2)
print(f"\nThe midpoint between {num1} and {num2} is: {result}")