"""
loops.py

🔰 Purpose:
This file explains how Python handles loops and iterations.

👩‍💻 Created for personal Python 3.13 learning

📘 What are Loops?
Loops allow you to repeat a block of code multiple times.

📘 Types of Loops in Python:
------------------------------------------------
1. for loop     → Iterates over sequences (lists, strings, etc.)
2. while loop   → Repeats as long as a condition is True

📘 Control Keywords:
------------------------------------------------
- break    → Exits the loop early
- continue → Skips the current iteration
- pass     → Placeholder; does nothing
"""

# ✅ for loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# ✅ for loop with range()
for i in range(1, 6):  # 1 to 5
    print("Number:", i)

# ✅ for loop with else block
for i in range(3):
    print("Looping", i)
else:
    print("✅ Loop completed without break")

# ✅ Nested for loop (loop inside loop)
for i in range(1, 3):
    for j in range(1, 4):
        print(f"i={i}, j={j}")

# ✅ while loop
count = 0
while count < 3:
    print("Count is", count)
    count += 1

# ✅ Infinite while loop with break (⚠️ careful!)
x = 1
while True:
    print("Breaking at 3:", x)
    if x == 3:
        break
    x += 1

# ✅ continue statement (skip current loop iteration)
for i in range(5):
    if i == 2:
        continue  # Skip 2
    print("i:", i)

# ✅ break statement (exit loop early)
for letter in "Tashy":
    if letter == "s":
        break
    print("Letter:", letter)

# ✅ pass statement (does nothing, just a placeholder)
for i in range(3):
    pass  # Reserved for future logic

# ✅ Looping through dictionary
user = {"name": "Tashy", "role": "Boss", "age": 25}
for key, value in user.items():
    print(f"{key} → {value}")
