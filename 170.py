# Initialize a list of words
words = ["apple", "banana", "cherry", "date"]

# Create a tuple of pairs of words and their reverses using a generator expression
reversed_tuples = tuple((word, word[::-1]) for word in words)

# Print the original words list
print(words)

# Print the tuple containing pairs of words and their reverses
print(reversed_tuples)
