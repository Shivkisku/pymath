# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate a list of prime numbers from 1 to 50
prime_numbers = [x for x in range(1, 51) if is_prime(x)]

# Print the list of prime numbers
print("Prime numbers from 1 to 50:", prime_numbers)
