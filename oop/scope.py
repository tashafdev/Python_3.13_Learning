"""
scope.py

🔰 Purpose:
This file explains variable scope in Python.

👩‍💻 Created for personal Python 3.13 learning

📘 What is Scope?
Scope defines where a variable is accessible.

📘 Python Scope Types (LEGB Rule):
------------------------------------------------
L → Local         (inside function)
E → Enclosing     (in nested functions)
G → Global        (top-level module)
B → Built-in      (Python’s internal names)
"""

# ✅ Global Scope (outside any function)
name = "Tashy"

def say_hello():
    print("Hello", name)  # Can access global 'name'

say_hello()

# ✅ Local Scope (inside a function)
def show():
    message = "This is local"
    print(message)

show()
# print(message)  # ❌ Error: 'message' is not defined outside

# ✅ Enclosing Scope (nested function)
def outer():
    outer_msg = "outer"

    def inner():
        print("Enclosing:", outer_msg)  # Accessing enclosing variable

    inner()

outer()

# ✅ Global keyword (to modify global variable)
count = 0

def increase():
    global count
    count += 1
    print("Updated count:", count)

increase()

# ✅ Nonlocal keyword (to modify enclosing variable)
def outer_func():
    value = 5

    def inner_func():
        nonlocal value
        value += 1
        print("Inner modified value:", value)

    inner_func()
    print("Outer sees:", value)

outer_func()

# ✅ Built-in Scope
print("Length of list:", len([1, 2, 3]))  # 'len' is a built-in function
