# Control Flow: if/elif/else, loops
# -----------------------------------

# if / elif / else
temperature = 30

if temperature > 35:
    print("It's very hot outside!")
elif temperature > 25:
    print("It's a warm day.")
elif temperature > 15:
    print("It's a mild day.")
else:
    print("It's cool outside.")

# for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# for loop with range
for i in range(1, 6):
    print(f"Count: {i}")

# while loop
count = 0
while count < 3:
    print(f"While loop iteration: {count}")
    count += 1

# loop control: break and continue
for num in range(10):
    if num == 3:
        continue  # skip 3
    if num == 7:
        break     # stop at 7
    print(num)

# list comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# Ternary expression
score = 75
grade = "Pass" if score >= 60 else "Fail"
print(f"Grade: {grade}")
