words = ["apple", "banana", "cherry"]
sorted_concatenated = {''.join(sorted(word)) for word in words}

print("Original list of words: ", words)
print("Set of words with characters sorted and concatenated: ", sorted_concatenated)
