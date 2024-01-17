from math import radians, sin, cos, sqrt, atan2

def haversine_distance(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Calculate the differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Calculate the distance
    distance = R * c
    return distance

# Input
start_latitude = float(input("Starting latitude = "))
start_longitude = float(input("Starting longitude = "))
end_latitude = float(input("Ending latitude = "))
end_longitude = float(input("Ending longitude = "))

# Calculate the distance
distance = haversine_distance(start_latitude, start_longitude, end_latitude, end_longitude)

# Display the result
print(f'Distance = {distance:.2f} km')
