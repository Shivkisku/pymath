def sum_of_powers(end, power=2, start=1):
    # Use range() and list comprehension to create a list of elements raised to the given power
    numbers_powered = [num ** power for num in range(start, end + 1)]

    # Use sum() to add the values together
    result_sum = sum(numbers_powered)

    return result_sum

# Input from the user
start_value = int(input("Enter the start value: "))
end_value = int(input("Enter the end value: "))
power_value = int(input("Enter the power value (default is 2): ") or 2)

# Calculate and display the sum of powers
result = sum_of_powers(end_value, power_value, start_value)
print(f"The sum of powers from {start_value} to {end_value} (inclusive) with power {power_value} is: {result}")
