# Initialize a string containing a single word
word = "hello"

# Create a tuple of distinct substrings using a nested generator expression
substrings = tuple(word[i:j+1] for i in range(len(word)) for j in range(i, len(word)))

# Print the original word
print(word)

# Print the tuple containing distinct substrings
print(substrings)
