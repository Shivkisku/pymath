import random

# Number of coin flips
num_flips = 1000

# Initialize counters for heads and tails
heads_count = 0
tails_count = 0

# Simulate flipping a coin 1000 times
for _ in range(num_flips):
    result = random.choice(["Heads", "Tails"])
    if result == "Heads":
        heads_count += 1
    else:
        tails_count += 1

# Display the results
print(f"Flipping a coin {num_flips} times and counting the number of heads and tails.")
print("Randomly select either 'Heads' or 'Tails' for each flip.\n")
print(f"Heads = {heads_count}")
print(f"Tails = {tails_count}")

print(f'"{result}" appeared {heads_count} times, and "{result}" appeared {tails_count} times.')
print("Since it's based on random selection, the actual results may vary each time you run the code.")
