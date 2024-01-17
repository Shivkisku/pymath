text = "Hello123"
ascii_values = {char: ord(char) for char in text if char.isalpha()}

print("Original Text:", text)
print("ASCII Values Dictionary:", ascii_values)
