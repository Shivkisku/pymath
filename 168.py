# Initialize a string containing the input sentence
sentence = "Hello, how are you?"

# Create a tuple of words with at least one vowel using a generator expression
vowel_words = tuple(word for word in sentence.split() if any(char.lower() in 'aeiou' for char in word))

# Print the original sentence
print(sentence)

# Print the tuple containing words with at least one vowel
print(vowel_words)
