def multiply_without_operator(num1, num2):
    result = 0
    for _ in range(abs(num2)):
        result += num1 if num2 > 0 else -num1
    return result

# Input
number1 = int(input("Number 1 = "))
number2 = int(input("Number 2 = "))

# Multiply without using *
multiplication_result = multiply_without_operator(number1, number2)

# Display the result
print(f'Multiplication = {multiplication_result}')
