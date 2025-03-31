"""
numbers.py

🔰 Purpose:
This file introduces how Python handles numbers.

👩‍💻 Created for personal Python 3.13 learning

📘 Number Types in Python:
------------------------------------------------
int     → Whole numbers (e.g. 1, 100, -50)
float   → Decimal numbers (e.g. 3.14, -0.5)
complex → Numbers with real + imaginary parts (e.g. 3 + 4j)

📘 Basic Arithmetic Operators:
------------------------------------------------
+       → Addition
-       → Subtraction
*       → Multiplication
/       → Division (float result)
/ /     → Floor division (integer result)
%       → Modulo (remainder)
**      → Power (exponent)
"""

# 🧮 Integers
a = 10
b = 3
print("a =", a)
print("b =", b)

# 🧪 Arithmetic Operations
print("\n📐 Arithmetic Results:")
print("Addition (a + b):", a + b)
print("Subtraction (a - b):", a - b)
print("Multiplication (a * b):", a * b)
print("Division (a / b):", a / b)
print("Floor Division (a // b):", a // b)
print("Modulo (a % b):", a % b)
print("Power (a ** b):", a ** b)

# 💧 Floats
pi = 3.14159
weight = 68.5
print("\npi =", pi, "| type:", type(pi))
print("weight =", weight, "| type:", type(weight))

# 🔮 Complex Numbers
z = 2 + 3j
print("\nz =", z)
print("Real part:", z.real)
print("Imaginary part:", z.imag)
print("Type of z:", type(z))

# 🧠 Tip:
# You can use type() to check what kind of number it is
