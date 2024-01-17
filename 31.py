import random

def generate_random_floats(num_samples, start_range, end_range):
    random_floats = [random.uniform(start_range, end_range) for _ in range(num_samples)]
    return random_floats

# Specify the range for random float numbers
start_range = 0.0
end_range = 10.0

# Number of random float numbers to generate
num_samples = 10

# Generate and print random float numbers
random_float_numbers = generate_random_floats(num_samples, start_range, end_range)

print(f"Generate and print {num_samples} random float numbers.")
print("You'll get different sets of random float numbers each time, with each number being within its specified range.")
print("\nRandom Float Numbers:")
print(random_float_numbers)
