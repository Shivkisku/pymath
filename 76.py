class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def __add__(self, other):
        real_sum = self.real + other.real
        imag_sum = self.imag + other.imag
        return ComplexNumber(real_sum, imag_sum)

# Creating two complex number objects
complex1 = ComplexNumber(3, 4)
complex2 = ComplexNumber(1, 2)

# Adding complex numbers using the + operator
result = complex1 + complex2

# Displaying the result
print("Result of Addition:", result)
