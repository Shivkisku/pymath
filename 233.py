words = ["apple", "banana", "cherry"]
vowel_words = {word for word in words if any(char.lower() in 'aeiou' for char in word)}

print("Original list of words: ", words)
print("Set of words with at least one vowel: ", vowel_words)
