"""
dictionaries.py

🔰 Purpose:
This file explains how Python handles dictionaries.

👩‍💻 Created for personal Python 3.13 learning

📘 What is a Dictionary?
A dictionary is a collection of key-value pairs.
Each key must be unique and immutable (e.g., string, number, tuple).

📘 Why use Dictionaries?
- To store related data using meaningful keys
- Fast lookup and flexible data structure

📘 Syntax:
------------------------------------------------
my_dict = {
    "key1": "value1",
    "key2": "value2"
}
"""

# ✅ Creating a dictionary
user = {
    "name": "Tashy",
    "age": 25,
    "is_admin": True
}

# ✅ Accessing values
print("Name:", user["name"])           # Tashy
print("Age:", user.get("age"))         # 25
print("Role:", user.get("role", "User"))  # Default if key doesn't exist

# ✅ Adding new key-value pair
user["country"] = "UAE"
print("Updated user:", user)

# ✅ Updating existing value
user["age"] = 26
print("Age updated:", user["age"])

# ✅ Removing items
user.pop("is_admin")        # Removes 'is_admin'
print("After pop:", user)

del user["country"]         # Deletes 'country'
print("After del:", user)

# ✅ Looping through dictionary
print("\nLooping through keys & values:")
for key, value in user.items():
    print(f"{key} → {value}")

# ✅ Dictionary methods
print("\nAll Keys:", user.keys())
print("All Values:", user.values())
print("All Items:", user.items())

# ✅ Nested dictionaries
people = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 35}
}
print("Nested Dict:", people["person2"]["name"])  # Bob

# ✅ Using dict() constructor
car = dict(brand="Toyota", model="Camry", year=2024)
print("Car info:", car)

# ✅ Dictionary comprehension
squares = {x: x*x for x in range(1, 6)}
print("Squares:", squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
