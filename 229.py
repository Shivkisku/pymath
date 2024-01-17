words = ["apple", "banana", "elppa", "race", "care", "cherry"]
anagrams = {''.join(sorted(word)) for word in words}

print("Original list of words: ", words)
print("Set of anagrams: ", anagrams)
