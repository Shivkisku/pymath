# Generate a list of strings with vowels removed
strings = ["apple", "banana", "cherry"]

# Use list comprehension to remove vowels from each word
no_vowels = [''.join([char for char in word if char.lower() not in 'aeiou']) for word in strings]

# Print the original list of strings
print("Original strings:", strings)

# Print the list of strings with vowels removed
print("No vowels:", no_vowels)
