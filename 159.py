# Initialize a list of words
words = ["apple", "banana", "cherry", "date"]

# Create a tuple of pairs of words and their lengths using a generator expression
word_lengths = tuple((word, len(word)) for word in words)

# Print the original words list
print(words)

# Print the tuple containing pairs of words and their lengths
print(word_lengths)
