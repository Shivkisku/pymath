strings = ["apple", "banana", "cherry"]
capitalized_strings = {' '.join([word.capitalize() for word in string.split()]) for string in strings}

print("Original list of strings: ", strings)
print("Set of strings with capitalized words: ", capitalized_strings)
