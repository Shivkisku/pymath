# Create a list of words with their lengths from a sentence
sentence = "This is a sample sentence."
word_lengths = [(word, len(word)) for word in sentence.split()]

# Print the original sentence and the word lengths list
print("Original sentence:", sentence)
print("Word lengths:", word_lengths)
