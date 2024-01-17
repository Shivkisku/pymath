text = "hello world"
char_frequency = {char: text.count(char) for char in set(text)}

print("Original Text:", text)
print("Character Frequency Dictionary:", char_frequency)
