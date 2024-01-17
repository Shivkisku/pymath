# Initialize a string containing the input sentence
sentence = "This is a sample sentence with repeated words is"

# Create a tuple of unique words using a set and then converting it to a tuple
unique_words_tuple = tuple(set(sentence.split()))

# Print the original sentence
print(sentence)

# Print the tuple containing unique words
print(unique_words_tuple)
