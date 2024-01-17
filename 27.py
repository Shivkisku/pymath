import cmath
import math

# Sample polar coordinates (length, angle in radians)
polar_coordinates = (5.0, 0.9272952180016122)

# Extract polar coordinates
r, theta = polar_coordinates

# Convert polar to rectangular coordinates
x = r * math.cos(theta)
y = r * math.sin(theta)

# Create a complex number using rectangular coordinates
rectangular_coordinates = complex(x, y)

# Display the input and the result
print(f"Polar Coordinates = {polar_coordinates}")
print(f"\nConvert Polar to Rectangular Coordinates = {rectangular_coordinates}")
