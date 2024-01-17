strings = ["apple", "banana", "cherry"]
merged_chars = {char for string in strings for char in string}

print("Original strings:", strings)
print("Merged characters:", merged_chars)
