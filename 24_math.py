import math

# Constants
print("Value of pi:", math.pi)  # The mathematical constant pi (π)

# Basic arithmetic functions
x = 4
y = 3
print("Square root of x:", math.sqrt(x))  # Square root
print("x to the power of y:", math.pow(x, y))  # x^y

# Trigonometric functions (angles in radians)
angle = math.radians(45)  # Convert degrees to radians
print("Sine of 45 degrees:", math.sin(angle))
print("Cosine of 45 degrees:", math.cos(angle))
print("Tangent of 45 degrees:", math.tan(angle))

# Logarithmic functions
num = 100
print("Natural logarithm of num:", math.log(num))  # Natural logarithm (base e)
print("Base 10 logarithm of num:", math.log10(num))  # Base 10 logarithm

# Other mathematical functions
print("Absolute value of -5.5:", math.fabs(-5.5))
print("Ceiling of 5.2:", math.ceil(5.2))  # Smallest integer greater than or equal to x
print("Floor of 5.2:", math.floor(5.2))  # Largest integer less than or equal to x
print("Factorial of 5:", math.factorial(5))  # 5!
print("GCD of 12 and 18:", math.gcd(12, 18))  # Greatest common divisor
