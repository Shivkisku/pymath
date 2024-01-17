import random

def generate_random_integers(num_samples, start_range, end_range):
    random_integers = [random.randint(start_range, end_range) for _ in range(num_samples)]
    return random_integers

# Specify the range for random integers
start_range = 0
end_range = 100

# Number of random integers to generate
num_samples = 10

# Generate and print random integer numbers
random_integer_numbers = generate_random_integers(num_samples, start_range, end_range)

print(f"Generate and print {num_samples} random integer numbers.")
print("You'll get different sets of random integer numbers each time, with each number being within its specified range.")
print("\nRandom Integer Numbers:")
print(random_integer_numbers)
