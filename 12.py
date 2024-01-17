def sum_of_divisors(number):
    divisor_sum = 0
    for i in range(1, number + 1):
        if number % i == 0:
            divisor_sum += i
    return divisor_sum

# Input
number = int(input("Enter the Number = "))

# Calculate the sum of divisors
sum_of_divisors_result = sum_of_divisors(number)

# Display the result
print(f'Sum of All Divisors = {sum_of_divisors_result}')
