sentence = "Hello, how are you?"

# Create a tuple of pairs of distinct words and their reversed forms
distinct_reversed_word_tuples = tuple((word, word[::-1]) for word in set(sentence.split()))

# Print the original sentence
print(sentence)

# Print the tuple containing pairs of distinct words and their reversed forms
print(distinct_reversed_word_tuples)
