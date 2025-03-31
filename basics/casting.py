"""
casting.py

🔰 Purpose:
This file explains type casting — converting one data type into another.

👩‍💻 Created for personal Python 3.13 learning

📘 Common Casting Functions:
------------------------------------------------
int()    → Converts to integer
float()  → Converts to float
str()    → Converts to string
bool()   → Converts to boolean
"""

# 🔁 Convert string to integer
num_str = "42"
num_int = int(num_str)
print("String to int:", num_int, "| Type:", type(num_int))

# 🔁 Convert string to float
pi_str = "3.14"
pi_float = float(pi_str)
print("String to float:", pi_float, "| Type:", type(pi_float))

# 🔁 Convert number to string
age = 25
age_str = str(age)
print("Int to string:", age_str, "| Type:", type(age_str))

# 🔁 Convert float to int (removes decimals, doesn't round!)
price = 99.99
price_int = int(price)
print("Float to int:", price_int)  # Output: 99 (not 100!)

# 🔁 Convert any value to boolean
print("\nBool Conversions:")
print("bool(1):", bool(1))       # True
print("bool(0):", bool(0))       # False
print("bool('Hello'):", bool("Hello"))   # True
print("bool(''):", bool(""))     # False
print("bool([]):", bool([]))     # False (empty list)

# ⚠️ Be careful: not all strings can be cast to numbers
bad_str = "Tashy"
# num = int(bad_str)  # ❌ This will raise a ValueError
print("\nCasting only works if the string looks like a number.")
