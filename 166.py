# Initialize a string containing the input sentence
sentence = "Hello, how are you?"

# Create a tuple of pairs of words and their vowel counts using a generator expression
vowel_count_tuples = tuple((word, sum(1 for char in word if char.lower() in 'aeiou')) for word in sentence.split())

# Print the original sentence
print(sentence)

# Print the tuple containing pairs of words and their vowel counts
print(vowel_count_tuples)
