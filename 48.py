def aliquot_sum(number):
    # Initialize the sum to 0
    aliquot_sum_result = 0

    # Find the divisors and add them to the sum
    for i in range(1, number):
        if number % i == 0:
            aliquot_sum_result += i

    return aliquot_sum_result

# Input from the user
input_number = int(input("Enter the Integer: "))

# Calculate and display the aliquot sum
result = aliquot_sum(input_number)
print(f"Integer = {input_number}")
print(f"Aliquot sum = {result}")
