"""
modules_intro.py

🔰 Purpose:
This file explains how Python modules work and how to import them.

👩‍💻 Created for personal Python 3.13 learning

📘 What is a Module?
A module is simply a `.py` file containing Python code (functions, variables, classes).

📘 Why use Modules?
- Organize code across multiple files
- Reuse functionality
- Keep projects maintainable

📘 Types of Modules:
------------------------------------------------
1. Built-in Modules (e.g., math, datetime, os)
2. Custom Modules (your own .py files)
3. Third-party Modules (via pip, e.g., numpy, requests)
"""

# ✅ Importing a built-in module
import math
print("Square root using math:", math.sqrt(25))

# ✅ Import specific function from module
from random import randint
print("Random number (1–10):", randint(1, 10))

# ✅ Custom module example (assuming basics/functions.py exists)
# from basics.functions import greet_user
# greet_user("Tashy")

# ✅ Aliasing a module
import datetime as dt
print("Current date:", dt.date.today())

# ✅ Using dir() to explore module contents
import os
print("Contents of os module:", dir(os)[:5])  # Just a few to demo
