#string manipulation example

first = input("Enter your first name: ")
middleIn = input("Enter your middle initial: ")
last = input("Enter your last name: ")

full_name = first + " " + middleIn + ". " + last

parts = [first, middleIn + ".", last]

parts_unpack = [first, middleIn, last]

print("Your full name is: " + full_name)

print(f"Your full name is: {first} {middleIn}. {last}")

print("Your full name is: %s %s. %s" % (first, middleIn, last))

print("Your full name is: {} {}. {}".format(first, middleIn, last))

print("Your full name is: " + " ".join(parts))

print("Your full name is: {} {}. {}".format(*parts_unpack))

