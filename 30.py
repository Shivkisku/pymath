from fractions import Fraction

# Sample decimal numbers as strings
decimal_strings = ["2.3", "7.5", "6.32", "5.1"]

# Display the input
print("Convert each Decimal to a Fraction")
print(decimal_strings)

# Convert each decimal to a fraction
for decimal_str in decimal_strings:
    decimal_number = float(decimal_str)
    fraction_representation = Fraction(decimal_number).limit_denominator()
    print(f"\n{decimal_number} = {fraction_representation.numerator}/{fraction_representation.denominator}")
