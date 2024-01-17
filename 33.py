import random

def generate_random_even_integers(num_samples, start_range, end_range):
    random_even_integers = [random.randrange(start_range, end_range, 2) for _ in range(num_samples)]
    return random_even_integers

# Specify the range for random even integers
start_range = 0
end_range = 100

# Number of random even integers to generate
num_samples = 10

# Generate and print random even integer numbers
random_even_integer_numbers = generate_random_even_integers(num_samples, start_range, end_range)

print(f"Generate and print {num_samples} random even integer numbers.")
print("You'll get different sets of random even integer numbers each time, with each number being within its specified range.")
print("\nRandom Even Integer Numbers:")
print(random_even_integer_numbers)
