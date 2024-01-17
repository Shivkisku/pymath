def calculate_difference(n=2):
    sum_of_squares = 0
    square_of_sum = 0

    for num in range(1, n + 1):
        # Calculate the sum of the squares of each number
        sum_of_squares += num**2

        # Calculate the sum of the numbers
        square_of_sum += num

    # Square the final sum obtained
    square_of_sum = square_of_sum**2

    # Calculate the difference between the square of sum and the sum of squares
    difference = square_of_sum - sum_of_squares

    return difference

# Input
n = int(input("N = "))

# Calculate the difference
calculated_difference = calculate_difference(n)

# Display the result
print(f'Calculated difference = {calculated_difference}')
