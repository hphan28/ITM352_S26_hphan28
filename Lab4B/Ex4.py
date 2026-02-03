email = input("Enter your email address: ")

parts = email.split("@")

username = parts[0]

domain = parts[1]

print("Username:", username)
print("Domain:", domain)

#Method 2: Using index() and slicing

at_symbol_index = email.index("@")

username_slice = email[:at_symbol_index]

domain_slice = email[at_symbol_index + 1 :]

print ("Username (sliced):", username_slice)
print ("Domain (sliced):", domain_slice)
