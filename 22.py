import cmath

def find_roots(a, b, c):
    # Calculate the discriminant
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    
    # Calculate the roots using the quadratic formula
    root1 = (-b + discriminant) / (2*a)
    root2 = (-b - discriminant) / (2*a)
    
    return root1, root2

# Sample inputs
a = 2
b = 5
c = 3

# Find the roots
roots = find_roots(a, b, c)

# Display the inputs and the result
print(f"Quadratic function = ({a} * x^2) + {b} * x + {c}")
print(f"A Number = {a}")
print(f"B Number = {b}")
print(f"C Number = {c}")

# Check if roots are real or complex
if roots[0].imag == 0:
    print(f"There are Two Roots = {roots[0].real:.1f} and {roots[1].real:.1f}")
else:
    print(f"There are Two Complex Roots = {roots[0]:.1f} and {roots[1]:.1f}")
