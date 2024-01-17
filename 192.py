# Process a sentence and create a set of word lengths
sentence = "This is a sample sentence."
word_lengths = {len(word) for word in sentence.split()}

# Print the original sentence
print("Original Sentence:", sentence)

# Print the set of word lengths
print("Word Lengths Set:", word_lengths)
