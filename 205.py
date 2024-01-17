string = "Hello, world!"
vowels = {char.lower() for char in string if char.lower() in 'aeiou'}

print("Original String:", string)
print("Set of Vowels:", vowels)
