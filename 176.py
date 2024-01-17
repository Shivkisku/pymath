# Initialize a string containing the input sentence
sentence = "This is a sample sentence with words of various lengths."

# Create a tuple of words with length greater than 4 using a generator expression
long_word_tuples = tuple(word for word in sentence.split() if len(word) > 4)

# Print the original sentence
print(sentence)

# Print the tuple containing words with length greater than 4
print(long_word_tuples)
