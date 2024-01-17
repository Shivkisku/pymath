words = ["apple", "banana", "cherry", "date"]
prefix = "ba"
words_with_prefix = {word for word in words if word.startswith(prefix)}

print("Original words:", words)
print("Prefix:", prefix)
print("Words with prefix:", words_with_prefix)
