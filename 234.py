words = ["apple", "banana", "cherry"]
tripled_chars = {''.join([char*3 for char in word]) for word in words}

print("Original list of words: ", words)
print("Set of words with characters repeated three times: ", tripled_chars)
