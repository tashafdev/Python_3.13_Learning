"""
functions.py

🔰 Purpose:
This file explains how to define and use functions in Python.

👩‍💻 Created for personal Python 3.13 learning

📘 What are Functions?
Functions are reusable blocks of code that perform a specific task.

📘 Why use Functions?
- Avoid code repetition
- Improve readability
- Enable modular programming

📘 Function Types:
------------------------------------------------
1. Built-in functions (e.g., print(), len(), type())
2. User-defined functions (created using def)
3. Lambda (anonymous) functions

📘 Function Components:
------------------------------------------------
- def → Keyword to define a function
- parameters → Input values
- return → Output of the function (optional)
"""

# ✅ Defining a simple function
def greet():
    print("Hello, Boss!")

# ✅ Calling a function
greet()  # Output: Hello, Boss!

# ✅ Function with parameters
def greet_user(name):
    print("Hello,", name)

greet_user("Tashy")  # Output: Hello, Tashy

# ✅ Function with multiple parameters
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 7)
print("Sum:", result)  # Output: Sum: 12

# ✅ Function with default parameters
def power(base, exponent=2):
    return base ** exponent

print(power(4))        # 4^2 = 16
print(power(2, 3))     # 2^3 = 8

# ✅ Function with return statement
def get_full_name(first, last):
    return f"{first} {last}"

name = get_full_name("Tashy", "Boss")
print("Full Name:", name)

# ✅ Function with *args (variable number of arguments)
def total(*numbers):
    return sum(numbers)

print("Total:", total(1, 2, 3, 4, 5))  # Output: 15

# ✅ Function with **kwargs (keyword arguments as dict)
def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

display_info(name="Tashy", age=25, role="Boss")

# ✅ Lambda (anonymous) function
square = lambda x: x * x
print("Square of 6:", square(6))  # Output: 36

# ✅ Function calling another function
def outer():
    def inner():
        print("Inner function called!")
    print("Calling inner from outer...")
    inner()

outer()

# ✅ Pass statement in empty function (placeholder)
def future_feature():
    pass  # To be implemented later
