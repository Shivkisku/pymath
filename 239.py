words = ["radar", "hello", "level", "world"]
palindromes = {word for word in words if word == word[::-1]}

print("Original words list: ", words)
print("Palindromic words: ", palindromes)
