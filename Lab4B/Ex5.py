sentence = input("Enter a sentence: ")

words = sentence.split(" ")

print("List of words:", words)

words.reverse()

print ("Reversed list of words:", words)

new_sentence = " ".join(words)

print("Reversed sentence:", new_sentence)

