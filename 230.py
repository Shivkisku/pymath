words = ["apple", "banana", "cherry"]
sorted_descending = {''.join(sorted(word, reverse=True)) for word in words}

print("Original list of words: ", words)
print("Set of words with characters sorted in descending order: ", sorted_descending)
