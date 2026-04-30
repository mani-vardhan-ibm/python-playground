# Python Variables & Data Types
# --------------------------------

# Strings
name = "Python Playground"
greeting = f"Welcome to {name}!"
print(greeting)

# Numbers
age = 25
height = 1.75
complex_num = 2 + 3j

# Booleans
is_learning = True
is_expert = False

# None
result = None

# Type checking
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(height))     # <class 'float'>
print(type(is_learning)) # <class 'bool'>

# Type conversion
age_str = str(age)
height_int = int(height)

print(f"Age as string: '{age_str}', Height as int: {height_int}")

# Multiple assignment
x = y = z = 0
a, b, c = 1, 2, 3

print(f"x={x}, y={y}, z={z}")
print(f"a={a}, b={b}, c={c}")
