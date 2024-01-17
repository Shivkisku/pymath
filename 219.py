words = ["apple", "banana", "cherry"]
duplicated_chars = {''.join([char*2 for char in word]) for word in words}

print("Original list of words: ", words)
print("Set of words with duplicated characters: ", duplicated_chars)
