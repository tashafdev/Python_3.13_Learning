"""
tuples.py

🔰 Purpose:
This file explains how Python handles tuples.

👩‍💻 Created for personal Python 3.13 learning

📘 What is a Tuple?
A tuple is an ordered, immutable (unchangeable) collection of items.
Defined using parentheses `()`.

📘 Why use Tuples?
- Protect data from being modified
- Tuples are faster than lists
- Can be used as keys in dictionaries (if elements are immutable)

📘 Syntax:
------------------------------------------------
my_tuple = (1, 2, 3)
"""

# ✅ Creating a tuple
person = ("Tashy", 25, "Boss")

# ✅ Accessing items
print("Name:", person[0])
print("Age:", person[1])

# ✅ Tuple length
print("Length:", len(person))  # 3

# ✅ Tuple with one item (⚠️ needs a comma)
single = ("Hello",)
print("Single item tuple:", single)

# ✅ Tuple without parentheses (packing)
coords = 10, 20, 30
print("Packed tuple:", coords)

# ✅ Unpacking tuples
x, y, z = coords
print("Unpacked values:", x, y, z)

# ✅ Looping through tuple
for item in person:
    print("Tuple item:", item)

# ✅ Checking for item
if "Tashy" in person:
    print("Yes, 'Tashy' is in the tuple")

# ✅ Nested tuples
nested = (("Python", 3.13), ("AI", 2025))
print("Access nested:", nested[1][0])  # AI

# ✅ Tuple methods
numbers = (1, 2, 3, 2, 4, 2)
print("Count of 2:", numbers.count(2))      # 3 times
print("Index of 3:", numbers.index(3))      # First occurrence

# ✅ Converting tuple → list → tuple
temp_list = list(person)
temp_list[1] = 26  # Modifying age
person = tuple(temp_list)
print("Modified person:", person)
