
from HandyMath import midpoint, squareroot, exponentiate, maximum, minimum


def main():
	num1 = float(input("Enter the first number: "))
	num2 = float(input("Enter the second number: "))

	mid = midpoint(num1, num2)
	sqrt_of_square = squareroot(num1 ** 2)
	power = exponentiate(num1, num2)
	max_val = maximum(num1, num2)
	min_val = minimum(num1, num2)

	print(f"\nMidpoint of {num1} and {num2} is: {mid}")
	print(f"Square root of the square of {num1} is: {sqrt_of_square}")
	print(f"{num1} raised to the power of {num2} is: {power}")
	print(f"Maximum of {num1} and {num2} is: {max_val}")
	print(f"Minimum of {num1} and {num2} is: {min_val}")


if __name__ == "__main__":
	main()

