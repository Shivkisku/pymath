string = "Hello, world!"
twice_chars = {char for char in string if string.count(char) == 2}

print("Original string: ", string)
print("Set of characters appearing exactly twice: ", twice_chars)
