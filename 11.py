def sum_of_digits_power(base, power):
    result = base**power
    sum_digits = sum(int(digit) for digit in str(result))
    return sum_digits

# Input
base_number = int(input("Base Number = "))
power_number = int(input("Power Number = "))

# Calculate the sum of digits
sum_of_digits = sum_of_digits_power(base_number, power_number)

# Display the result
print(f'Sum of digits = {sum_of_digits}')
