#ask the use for a number between 1 and 100, square the number and print the number and its square
#name: Harrison Phan
#Date: 01/20/2026

print ("Welcome to the Program")
value_entered =input ("Please enter a number between 1 and 100")
print ("You entered:", value_entered)

value_as_interger = int (value_entered)
value_squared = value_as_interger ** 2
#print("The square of", value_as_interger, "is", sqaured_value)
print (f"The square of {value_as_interger} is {value_squared}")
