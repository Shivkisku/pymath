words = {"apple", "banana", "cherry"}
sorted_chars = {''.join(sorted(word)) for word in words}

print("Original set: ", words)
print("Set with sorted characters: ", sorted_chars)
