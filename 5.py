import math

def cylinder_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def cylinder_lateral_surface_area(radius, height):
    lateral_surface_area = 2 * math.pi * radius * height
    return lateral_surface_area

def cylinder_total_surface_area(radius, height):
    base_area = math.pi * radius**2
    lateral_surface_area = 2 * math.pi * radius * height
    total_surface_area = 2 * base_area + lateral_surface_area
    return total_surface_area

# Sample input
radius_input = 2.4
height_input = 3

# Calculate volume and surface areas
volume_output = cylinder_volume(radius_input, height_input)
lateral_surface_area_output = cylinder_lateral_surface_area(radius_input, height_input)
total_surface_area_output = cylinder_total_surface_area(radius_input, height_input)

# Display the result
print(f'Radius of the Cylinder = {radius_input}')
print(f'Height of the Cylinder = {height_input}')
print(f'Volume of the Cylinder = {volume_output} cubic units')
print(f'Lateral surface area of the Cylinder = {lateral_surface_area_output} square units')
print(f'Total surface area of the Cylinder = {total_surface_area_output} square units')
