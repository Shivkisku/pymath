import math

def regular_polygon_area(num_sides, side_length):
    area = (num_sides * side_length**2) / (4 * math.tan(math.pi / num_sides))
    return area

# Input
num_sides = int(input("Number of Sides = "))
side_length = float(input("Length of a Side = "))

# Calculate the area of the regular polygon
polygon_area = regular_polygon_area(num_sides, side_length)

# Display the result
print(f'Area of the Polygon = {polygon_area:.4f}')
