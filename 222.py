string = "Hello, world!"
non_whitespace_chars = {char for char in string if not char.isspace()}

print("Original string: ", string)
print("Set of non-whitespace characters: ", non_whitespace_chars)
