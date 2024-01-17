words = ['python', 'programming', 'language']
sorted_letters = {word: ''.join(sorted(word)) for word in words}

print("Original Words:", words)
print("Sorted Letters Dictionary:", sorted_letters)
