def calculate_wind_chill_index(temperature, wind_speed):
    wci = 13.12 + 0.6215 * temperature - 11.37 * (wind_speed ** 0.16) + 0.3965 * temperature * (wind_speed ** 0.16)
    return wci

# Sample inputs
wind_speed_kph = 21.3
temperature_celsius = 34.5

# Calculate Wind Chill Index
wind_chill_index = calculate_wind_chill_index(temperature_celsius, wind_speed_kph)

# Display the inputs and the result
print(f"Wind Speed in kilometers/hour = {wind_speed_kph}")
print(f"Temperature in Degrees Celsius = {temperature_celsius}")
print(f"The wind chill index is {wind_chill_index:.1f}")
