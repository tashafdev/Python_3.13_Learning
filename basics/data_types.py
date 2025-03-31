"""
data_types.py

🔰 Purpose:
This file introduces the most common data types in Python.

👩‍💻 Created for personal Python 3.13 learning

📘 Common Python Data Types:
------------------------------------------------
str     → Text (string)
int     → Whole numbers
float   → Decimal numbers
bool    → True or False
list    → Ordered, changeable collection (with duplicates)
tuple   → Ordered, unchangeable collection (with duplicates)
set     → Unordered collection (no duplicates)
dict    → Key-value pair collection
"""

# 🧵 String → Text data
name = "Tashy"
print("Type of name:", type(name))  # str

# 🔢 Integer → Whole number
age = 25
print("Type of age:", type(age))  # int

# 💧 Float → Decimal number
height = 5.6
print("Type of height:", type(height))  # float

# ✅ Boolean → True or False
is_happy = True
print("Type of is_happy:", type(is_happy))  # bool

# 📦 List → Ordered, mutable (can change), allows duplicates
fruits = ["apple", "banana", "apple"]
print("Type of fruits:", type(fruits))  # list

# 🧊 Tuple → Ordered, immutable (can't change), allows duplicates
colors = ("red", "blue", "green")
print("Type of colors:", type(colors))  # tuple

# 🌀 Set → Unordered, unique values only (no duplicates)
unique_numbers = {1, 2, 3, 3}
print("Type of unique_numbers:", type(unique_numbers))  # set

# 🗂️ Dictionary → Key-value pairs
person = {
    "name": "Tashy",
    "age": 25,
    "is_active": True
}
print("Type of person:", type(person))  # dict

# 🧪 Checking all values
print("\nData Type Outputs:")
print(name, age, height, is_happy)
print(fruits)
print(colors)
print(unique_numbers)
print(person)
