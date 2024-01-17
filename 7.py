import math

def arc_length(angle_degrees, radius):
    # Convert angle from degrees to radians
    angle_radians = math.radians(angle_degrees)
    
    # Calculate arc length
    arc_length = radius * angle_radians
    return arc_length

# Sample input
angle_input = 35
radius_input = 25

# Calculate arc length
arc_length_output = arc_length(angle_input, radius_input)

# Display the result
print(f'Angle in Degrees = {angle_input}')
print(f'Radius = {radius_input}')
print(f'Arc Length = {arc_length_output}')
