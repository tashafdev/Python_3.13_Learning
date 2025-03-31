"""
strings.py

🔰 Purpose:
This file explains how to work with strings in Python.

👩‍💻 Created for personal Python 3.13 learning

📘 What is a String?
A string is a sequence of characters, like text or words.
It can be written in single ('') or double ("") quotes.

📘 Common String Operations:
------------------------------------------------
- Accessing characters using indexes
- Slicing
- Using built-in string methods like upper(), lower(), replace(), etc.
"""

# 🎯 Creating strings
name = "Tashy"
greeting = 'Hello, world!'

# 🎯 Accessing characters by index (starts at 0)
print("First letter of name:", name[0])     # T
print("Last letter of name:", name[-1])     # y

# 🎯 Slicing strings
print("First 3 letters:", name[0:3])        # Tas
print("From 2nd to end:", name[1:])         # ashy

# 🎯 String length
print("Length of greeting:", len(greeting))

# 🛠️ Common string methods
print("Uppercase:", name.upper())           # TASHY
print("Lowercase:", name.lower())           # tashy
print("Replace:", greeting.replace("world", "Tashy"))  # Hello, Tashy!
print("Split:", greeting.split(","))        # ['Hello', ' world!']
print("Check if alphabetic:", name.isalpha())   # True
print("Check if numeric:", name.isnumeric())    # False

# ➕ String concatenation
first = "Smart"
second = "Coder"
full = first + " " + second
print("Concatenated:", full)

# 📐 String formatting
age = 25
print(f"{name} is {age} years old.")   # Using f-string
print("{} is {} years old.".format(name, age))  # Using format()
