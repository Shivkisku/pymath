words = ['apple', 'Banana', 'cherry', 'Date']
uppercase_words = {word: word.upper() for word in words if any(char.isupper() for char in word)}

print("Original Words:", words)
print("Uppercase Words Dictionary:", uppercase_words)
