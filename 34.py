import random

# Sample string
input_string = "Python Exercise"

# Get a single random element from the string
random_element = random.choice(input_string)

# Display the input and the result
print(f"String = {input_string}")
print(f"\nRandom Element = {random_element}")

print("\nIn this example, the random element selected from the string is", f'"{random_element}".')
print("However, since it's a random process, the output may vary each time you run the program,")
print("and you might get a different character as the random element.")
