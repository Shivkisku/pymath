def rearrange_digits(number):
    # Convert the number to a list of digits
    digits = [int(digit) for digit in str(number)]

    # Sort the digits to create the minimum and maximum numbers
    min_number = int(''.join(map(str, sorted(digits))))
    max_number = int(''.join(map(str, sorted(digits, reverse=True))))

    return min_number, max_number

# Sample input
input_number = 2014

# Display the input
print(f"Number = {input_number}")

# Find and display the minimum and maximum numbers
min_number, max_number = rearrange_digits(input_number)
print(f"Minimum Numbers = {min_number:04d}")
print(f"Maximum Numbers = {max_number:04d}")
