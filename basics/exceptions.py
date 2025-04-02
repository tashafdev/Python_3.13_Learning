"""
exceptions.py

🔰 Purpose:
This file explains how Python handles exceptions (errors).

👩‍💻 Created for personal Python 3.13 learning

📘 What are Exceptions?
Exceptions are runtime errors that disrupt the normal flow of a program.

📘 Why handle Exceptions?
- Prevents your program from crashing
- Lets you handle specific problems smoothly
- Good for user experience & debugging

📘 Common Exception Types:
------------------------------------------------
ZeroDivisionError       → Division by zero
ValueError              → Wrong value type
TypeError               → Invalid operation between types
IndexError              → List index out of range
KeyError                → Dictionary key not found
FileNotFoundError       → File not found
"""

# ✅ Basic try...except block
try:
    result = 10 / 0
except ZeroDivisionError:
    print("❌ Cannot divide by zero!")

# ✅ Multiple except blocks
try:
    value = int("abc")  # This will fail
except ValueError:
    print("❌ That's not a valid integer!")
except TypeError:
    print("❌ Invalid type used!")

# ✅ Catching multiple errors in one line
try:
    my_list = [1, 2, 3]
    print(my_list[5])  # Index out of range
except (IndexError, KeyError):
    print("❌ Index or Key error caught!")

# ✅ Using else block (runs if no error)
try:
    name = "Tashy"
    print(name.upper())
except Exception:
    print("❌ Something went wrong")
else:
    print("✅ Operation successful")

# ✅ Using finally block (always runs)
try:
    print("🧪 Trying something risky...")
    x = 100 / 10
except:
    print("❌ Error occurred")
finally:
    print("✅ This always runs (cleanup, logs, etc.)")

# ✅ Raising your own exception
age = 15
if age < 18:
    raise Exception("🚫 You must be at least 18 years old.")

# ✅ Custom error message with try...except
try:
    salary = -5000
    if salary < 0:
        raise ValueError("🚫 Salary cannot be negative")
except ValueError as ve:
    print("Caught Error:", ve)
