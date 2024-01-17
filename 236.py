import random

words = ["apple", "banana", "cherry"]
shuffled_chars = {''.join(random.sample(word, len(word))) for word in words}

print("Original list of words: ", words)
print("Set of words with shuffled characters: ", shuffled_chars)
