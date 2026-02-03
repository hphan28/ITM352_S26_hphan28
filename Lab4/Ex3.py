# Create the list of responses from Exercise 2 (values 5, 7, 3, 8).
# Next add the response 0 to the end of the list using the .append() method.
# Next add the response 6 to the list between the values 7 and 3 (third position)
# using list slicing and the + operator instead of .insert().

responses = [5, 7, 3, 8]

# 1) Append 0 to the end (in-place)
responses.append(0)
print("Responses after appending 0:", responses)

# 2) Use slicing and + to insert 6 at index 2 (between 7 and 3)
#    responses[:2] -> first two elements; responses[2:] -> rest
responses = responses[:2] + [6] + responses[2:]
print("Responses after adding 6 using slicing and +:", responses)

# Explanation:
# - For lists, + concatenates two lists and returns a new list. Example: [1,2] + [3] -> [1,2,3]
#   This does not modify the original lists; it creates a new one.
# - For strings, + concatenates strings and returns a new string. Example: "a" + "b" -> "ab"
# - For numbers, + performs numeric addition. Example: 2 + 3 -> 5
# - Using .insert() modifies the list in place; using slicing + produces a new list and assigns it.
#Create the list of responses from Exercise 2 (values 5, 7, 3, 8). 
# Next add the response “0” to the end of the list using the .append() method. 
# Next add the response “6” to the list between the values 7 and 3 (in what will be the third position in the list) using the .insert() method. 
# Print out the list to verify that you made the changes 
#correctly.

#responses = [5, 7, 3, 8]
#responses.append(0)
#print("Responses after appending 0:", responses)
#responses.insert(2, 6)
#print ("Responses after inserting 6 at index 2:", responses)


