"""
sets.py

🔰 Purpose:
This file explains how Python handles sets.

👩‍💻 Created for personal Python 3.13 learning

📘 What is a Set?
A set is an unordered collection of **unique** items.
Duplicates are automatically removed.

📘 Why use Sets?
- To remove duplicates
- To perform set operations (union, intersection, etc.)
- Faster membership testing

📘 Syntax:
------------------------------------------------
my_set = {1, 2, 3}
or using set():
my_set = set([1, 2, 3])
"""

# ✅ Creating sets
fruits = {"apple", "banana", "cherry", "apple"}  # 'apple' appears only once
print("Fruits set:", fruits)

# ✅ Adding items
fruits.add("mango")
print("After add:", fruits)

# ✅ Adding multiple items
fruits.update(["orange", "grape"])
print("After update:", fruits)

# ✅ Removing items
fruits.remove("banana")   # ❌ Raises error if item doesn't exist
fruits.discard("pineapple")  # ✅ No error if item doesn't exist
print("After remove & discard:", fruits)

# ✅ Set length
print("Number of fruits:", len(fruits))

# ✅ Looping through a set
print("Looping through set:")
for item in fruits:
    print(item)

# ✅ Membership testing
if "apple" in fruits:
    print("🍎 Apple is in the set")

# ✅ Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print("Union:", set_a.union(set_b))           # {1, 2, 3, 4, 5}
print("Intersection:", set_a.intersection(set_b))  # {3}
print("Difference (A - B):", set_a.difference(set_b))  # {1, 2}
print("Symmetric Difference:", set_a.symmetric_difference(set_b))  # {1, 2, 4, 5}

# ✅ Clearing a set
set_a.clear()
print("After clear:", set_a)

# ✅ Set comprehension
squares = {x**2 for x in range(1, 6)}
print("Squares set:", squares)  # {1, 4, 9, 16, 25}
