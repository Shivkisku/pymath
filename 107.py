# Create a list of words with their lengths greater than 3 from a sentence
sentence = "This is a sample sentence."
long_words = [word for word in sentence.split() if len(word) > 3]

# Print the original sentence and the list of long words
print(sentence)
print(long_words)
