# Initialize a list of characters
characters = ['a', 'b', 'c', 'd', 'e']

# Create a tuple of pairs of characters and their ASCII values using a generator expression
char_ascii_pairs = tuple((char, ord(char)) for char in characters)

# Print the original characters list
print(characters)

# Print the tuple containing pairs of characters and their ASCII values
print(char_ascii_pairs)
