strings = {"apple", "banana", "cherry"}
no_vowels = {''.join([char for char in word if char.lower() not in 'aeiou']) for word in strings}

print("Original set of strings: ", strings)
print("Set of strings with vowels removed: ", no_vowels)
