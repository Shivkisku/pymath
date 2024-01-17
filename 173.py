# Initialize two strings
word1 = "apple"
word2 = "cherry"

# Create a tuple of pairs of common letters using a generator expression
common_letter_tuples = tuple((char, char) for char in word1 if char in word2)

# Print the original words
print(word1)
print(word2)

# Print the tuple containing pairs of common letters
print(common_letter_tuples)
