# Functions in Python
# --------------------

# Basic function
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))

# Default parameters
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # 9
print(power(2, 10))  # 1024

# *args – variable positional arguments
def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3, 4, 5))  # 15

# **kwargs – variable keyword arguments
def describe_person(**info):
    for key, value in info.items():
        print(f"  {key}: {value}")

describe_person(name="Alice", age=30, city="New York")

# Lambda (anonymous) functions
square = lambda x: x ** 2
print(square(5))  # 25

# Higher-order functions
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda n: n % 2 == 0, numbers))
doubled = list(map(lambda n: n * 2, numbers))

print(f"Evens: {evens}")
print(f"Doubled: {doubled}")

# Nested functions & closures
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

triple = make_multiplier(3)
print(triple(7))  # 21

# Docstrings
def celsius_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit.

    Args:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.
    """
    return celsius * 9 / 5 + 32

print(celsius_to_fahrenheit(100))  # 212.0
