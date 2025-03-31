"""
booleans.py

🔰 Purpose:
This file explains how Python handles boolean values.

👩‍💻 Created for personal Python 3.13 learning

📘 What are Booleans?
Booleans represent one of two values:
- True
- False

📘 Where are Booleans used?
- Conditions (if, while)
- Comparisons
- Logic checks

📘 Common Comparison Operators:
------------------------------------------------
==    → Equal to
!=    → Not equal to
>     → Greater than
<     → Less than
>=    → Greater than or equal to
<=    → Less than or equal to

📘 Logical Operators:
------------------------------------------------
and   → Both conditions must be True
or    → At least one condition is True
not   → Reverses the condition
"""

# ✅ Boolean values
is_online = True
is_admin = False

print("is_online:", is_online)
print("is_admin:", is_admin)

# 📊 Comparisons (result in boolean values)
print("\nComparison Results:")
print("5 == 5:", 5 == 5)             # True
print("10 != 3:", 10 != 3)           # True
print("7 > 3:", 7 > 3)               # True
print("2 < 1:", 2 < 1)               # False
print("4 >= 4:", 4 >= 4)             # True
print("9 <= 10:", 9 <= 10)           # True

# 🔄 Logical operations
print("\nLogical Results:")
print("True and False:", True and False)     # False
print("True or False:", True or False)       # True
print("not True:", not True)                 # False

# 🧠 Booleans in conditions
age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# ⚠️ Truthy and Falsy values in Python
# These values behave like booleans in if-statements

print("\nTruthy / Falsy Examples:")
print("bool(0):", bool(0))         # False
print("bool(1):", bool(1))         # True
print("bool(''):", bool(""))       # False
print("bool('Hello'):", bool("Hello"))  # True
print("bool([]):", bool([]))       # False
print("bool([1, 2]):", bool([1, 2]))  # True
