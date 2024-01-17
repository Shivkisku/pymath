# Initialize two strings
word1 = "apple"
word2 = "cherry"

# Create a tuple of common letters using a generator expression
common_letters = tuple(char for char in word1 if char in word2)

# Print the original words
print(word1)
print(word2)

# Print the tuple containing common letters
print(common_letters)
