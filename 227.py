words = ["apple", "banana", "cherry"]
unique_vowels = {char for word in words for char in word if char.lower() in 'aeiou'}

print("Original list of words: ", words)
print("Set of unique vowels: ", unique_vowels)
