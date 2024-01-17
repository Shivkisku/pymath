# Generate a list of strings with their lengths from another list
words = ["apple", "banana", "cherry"]

# Create a list of tuples containing each word and its length
word_lengths = [(word, len(word)) for word in words]

# Print the original words list
print("Original words list:", words)

# Print the list of tuples containing each word and its length
print("Word lengths:", word_lengths)
