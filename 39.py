def round_up_to_digits(number, num_digits):
    rounded_number = round(number, num_digits)
    return rounded_number

# Sample number
number = 88.24573

# Display the original number
print("Number =", number)

# Round up to the nearest whole number
print("Round up to the nearest whole number =", round_up_to_digits(number, 0))

# Round up to one decimal place
print("Round up to one decimal place =", round_up_to_digits(number, 1))

# Round up to two decimal places
print("Round up to two decimal places =", round_up_to_digits(number, 2))

# Round up to three decimal places
print("Round up to three decimal places =", round_up_to_digits(number, 3))

# Round up to four decimal places
print("Round up to four decimal places =", round_up_to_digits(number, 4))
