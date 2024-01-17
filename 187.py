strings = ["apple", "Banana", "Cherry"]

# Create a tuple of distinct characters (case-insensitive) from the list of strings
distinct_case_insensitive_chars = tuple(set(char.lower() for string in strings for char in string))

# Print the original list of strings
print(strings)

# Print the tuple containing distinct case-insensitive characters
print(distinct_case_insensitive_chars)
