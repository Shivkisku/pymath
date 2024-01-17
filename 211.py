string = "Hello, world!"
consonants = {char for char in string if char.isalpha() and char.lower() not in 'aeiou'}

print("Original String:", string)
print("Consonants Set:", consonants)
