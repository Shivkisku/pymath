# Process a string and create a set of unique alphabetical characters
string = "Hello, world!"
chars = {char for char in string if char.isalpha()}

# Print the original string
print("Original String:", string)

# Print the set of unique alphabetical characters
print("Unique Alphabets Set:", chars)
