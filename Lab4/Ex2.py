#Define a list of survey response values [5, 7, 3, and 8] and store them in a variable. 
# Next define a tuple of respondent ID values (1012, 1035, 1021, and 1053). 
# Use the .append() method to append the tuple to the list. Print out the list.

#responses = [5, 7, 3, 8]
#respondent_ids = (1012, 1035, 1021, 1053)
#responses.append(respondent_ids)
#print("Survey responses with respondent IDs:", responses)

response_values= [(1012, 5), (1035, 7), (1021, 3), (1053, 8)]

# List vs String comparison:
# - List: mutable (can change elements), holds any object types, ordered collection
# - String: immutable (cannot change chars), holds only characters, ordered sequence
# - List methods: .append(), .sort(), .remove() modify the list in place
# - String methods: .upper(), .split(), .replace() return new strings (original unchanged)
# - List indexing: list[0] returns an element; string indexing: string[0] returns a character
# - Lists support heterogeneous data (mixed types); strings are homogeneous (all chars)

response_values.sort()
print("Sorted survey responses with respondent IDs:", response_values)


