def hamming_distance(value1, value2):
    # Use XOR to find the bit difference between the two numbers
    xor_result = value1 ^ value2

    # Convert the XOR result to a binary string
    binary_string = bin(xor_result)[2:]

    # Count the number of 1s in the binary string
    distance = binary_string.count('1')

    return distance

# Input from the user
value1 = int(input("Enter the first value: "))
value2 = int(input("Enter the second value: "))

# Calculate and display the Hamming distance
distance = hamming_distance(value1, value2)
print(f"The Hamming distance between {value1} and {value2} is: {distance}")
