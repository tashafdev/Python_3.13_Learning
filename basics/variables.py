"""
variables.py

🔰 Purpose:
This file explains how to create and use variables in Python.

🧠 What is a variable?
A variable is like a labeled box in memory that stores data.

👩‍💻 Created for personal Python 3.13 learning

📘 Key Points:
-------------------------------------
- No need to declare data types.
- Variable names should be meaningful.
- Variables can be reassigned anytime.
"""

# 📦 Assigning values to variables
name = "Tashy"         # A string value
age = 25               # An integer (whole number)
height = 5.4           # A float (decimal number)
is_active = True       # A boolean value

# 🔍 Displaying variable values using print()
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Active:", is_active)

# ✏️ Variables can change anytime (reassignment)
age = 26
print("Updated Age:", age)

# 📛 Invalid variable names (❌ avoid these)
# 1name = "Invalid"     → Can't start with a number
# my-age = 25           → Can't use hyphens
# class = "Python"      → Can't use reserved words like class, def, etc.

# ✅ Valid naming examples
my_name = "Tashy"
userAge = 30
_user_id = 123

# 🧪 You can also assign the same value to multiple variables
a = b = c = "Python"
print(a, b, c)   # Output: Python Python Python

# 🧃 Assign different values in one line
x, y, z = "Apple", "Banana", "Cherry"
print(x)
print(y)
print(z)
