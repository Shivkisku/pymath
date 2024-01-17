# Initialize a list of numbers
numbers = [10, 15, 20, 25]

# Create a tuple of sets of distinct divisors using a generator expression
distinct_divisors = tuple({divisor for divisor in range(1, num+1) if num % divisor == 0} for num in numbers)

# Print the original numbers list
print(numbers)

# Print the tuple containing sets of distinct divisors for each number
print(distinct_divisors)
