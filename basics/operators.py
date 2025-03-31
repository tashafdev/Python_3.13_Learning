"""
operators.py

🔰 Purpose:
This file explains the different types of operators in Python.

👩‍💻 Created for personal Python 3.13 learning

📘 Types of Operators in Python:
------------------------------------------------
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
"""

a = 10
b = 3

# 1️⃣ Arithmetic Operators
print("Arithmetic Operators:")
print("a + b =", a + b)      # Addition
print("a - b =", a - b)      # Subtraction
print("a * b =", a * b)      # Multiplication
print("a / b =", a / b)      # Division
print("a // b =", a // b)    # Floor Division
print("a % b =", a % b)      # Modulo (remainder)
print("a ** b =", a ** b)    # Exponent (a raised to b)

# 2️⃣ Assignment Operators
print("\nAssignment Operators:")
x = 5
x += 2   # same as x = x + 2
print("x += 2 →", x)

x -= 1
print("x -= 1 →", x)

x *= 3
print("x *= 3 →", x)

x /= 2
print("x /= 2 →", x)

# 3️⃣ Comparison Operators
print("\nComparison Operators:")
print("a == b:", a == b)     # Equal to
print("a != b:", a != b)     # Not equal to
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# 4️⃣ Logical Operators
print("\nLogical Operators:")
print("True and False:", True and False)
print("True or False:", True or False)
print("not True:", not True)

# 5️⃣ Identity Operators
print("\nIdentity Operators:")
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("x is y:", x is y)     # True (same object)
print("x is z:", x is z)     # False (same content but different object)
print("x is not z:", x is not z)

# 6️⃣ Membership Operators
print("\nMembership Operators:")
my_list = [1, 2, 3, 4]
print("2 in my_list:", 2 in my_list)       # True
print("5 not in my_list:", 5 not in my_list)  # True
