string = "Hello, world!"

non_vowels = {char for char in string if char.lower() not in 'aeiou'}

print("Original String:", string)
print("Non-vowel Characters Set:", non_vowels)
