# Initialize a string containing the input sentence
sentence = "This is a sample sentence with various words."

# Create a tuple of words with 'a' or 'e' using a generator expression
ae_words = tuple(word for word in sentence.split() if 'a' in word or 'e' in word)

# Print the original sentence
print(sentence)

# Print the tuple containing words with 'a' or 'e'
print(ae_words)
