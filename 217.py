words = ["apple", "banana", "cherry"]
unique_chars = {char for word in words for char in word}

print("Original list of words: ", words)
print("Set of unique characters: ", unique_chars)
