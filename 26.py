import cmath

# Sample complex number
complex_number = complex(3, 4)

# Extract real and imaginary parts
real_part = complex_number.real
imaginary_part = complex_number.imag

# Calculate length (magnitude)
length = abs(complex_number)

# Calculate angle (phase)
angle = cmath.phase(complex_number)

# Display the input and the results
print(f"Real = {real_part}")
print(f"Imaginary = {imaginary_part}")

print(f"\nLength of a Complex Number = {length}")
print(f"Complex Number Angle = {angle}")
