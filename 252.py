words = ['apple', 'banana', 'cherry']
vowel_counts = {word: sum(1 for char in word if char.lower() in 'aeiou') for word in words}

print("Original Words:", words)
print("Vowel Counts Dictionary:", vowel_counts)
