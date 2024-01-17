def find_smallest_multiple(n):
    factors = []
    result = 1
    
    # Function to find the prime factors of a number
    def prime_factors(num):
        prime_factors_list = []
        divisor = 2
        while divisor <= num:
            if num % divisor == 0:
                prime_factors_list.append(divisor)
                num = num / divisor
            else:
                divisor += 1
        return prime_factors_list
    
    # Calculate the smallest multiple
    for i in range(2, n+1):
        prime_factors_list = prime_factors(i)
        for factor in prime_factors_list:
            if factor not in factors or factors.count(factor) < prime_factors_list.count(factor):
                factors.append(factor)
    
    for factor in factors:
        result *= factor
    
    return result, factors

# Input
n = int(input("Enter a positive integer (n) = "))

# Find the smallest multiple and its factors
result, factors = find_smallest_multiple(n)

# Display the result
print(f'The smallest multiple of the first {n} numbers is = {result}')
print(f'Factors of the smallest multiple = {factors}')
