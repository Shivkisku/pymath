# Initialize a list of words
words = ["apple", "banana", "cherry", "date"]

# Create a tuple of distinct vowels using a generator expression
vowels = tuple(char for word in words for char in word if char.lower() in 'aeiou')

# Create a tuple of distinct consonants using a generator expression
consonants = tuple(char for word in words for char in word if char.lower() not in 'aeiou')

# Print the original words list
print(words)

# Print the tuple containing distinct vowels
print(vowels)

# Print the tuple containing distinct consonants
print(consonants)
