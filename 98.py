# Create a list of uppercase words from a sentence
sentence = "This is a sample sentence."

# Use list comprehension to convert words to uppercase
uppercase_words = [word.upper() for word in sentence.split()]

# Print the original sentence
print("Original sentence:", sentence)

# Print the list of uppercase words
print("Uppercase words:", uppercase_words)
