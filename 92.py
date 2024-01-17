# Create a list of reversed strings from another list
words = ["apple", "banana", "cherry"]

# Using list comprehension to reverse each word
reversed_words = [word[::-1] for word in words]

# Print the original words list
print("Original words:", words)

# Print the reversed_words list
print("Reversed words:", reversed_words)
