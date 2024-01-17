sentence = "Hello, how are you?"

# Create a tuple of word-length pairs for words with lengths divisible by 3
divisible_by_3_length_word_length_tuples = tuple((word, len(word)) for word in set(sentence.split()) if len(word) % 3 == 0)

# Print the original sentence
print(sentence)

# Print the tuple containing word-length pairs for words with lengths divisible by 3
print(divisible_by_3_length_word_length_tuples)
