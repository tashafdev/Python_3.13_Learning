"""
math_usage.py

🔰 Purpose:
This file explains how to use the math module for mathematical operations.

👩‍💻 Created for personal Python 3.13 learning

📘 Why use the math module?
- Provides access to common mathematical functions/constants
- More accurate and efficient than manual formulas

📘 Common math functions:
------------------------------------------------
math.sqrt(x)       → Square root
math.pow(x, y)     → x raised to y
math.ceil(x)       → Round up
math.floor(x)      → Round down
math.fabs(x)       → Absolute value
math.factorial(n)  → n!
math.log(x, base)  → Logarithm
math.sin(x)        → Sine (radians)
math.radians(deg)  → Degrees → Radians
math.pi            → 3.141...
"""

import math

# ✅ Square root
print("√25 =", math.sqrt(25))

# ✅ Power
print("2⁵ =", math.pow(2, 5))  # 32.0

# ✅ Rounding
print("Ceil 4.2 →", math.ceil(4.2))
print("Floor 4.8 →", math.floor(4.8))

# ✅ Absolute value (always positive)
print("Absolute of -10:", math.fabs(-10))

# ✅ Factorial
print("Factorial of 5:", math.factorial(5))

# ✅ Logarithms
print("Log base 10 of 1000:", math.log10(1000))
print("Natural log (base e) of 20:", math.log(20))

# ✅ Trigonometry
angle_deg = 90
angle_rad = math.radians(angle_deg)
print("Sin(90°):", math.sin(angle_rad))

# ✅ Math constants
print("π =", math.pi)
print("Euler's number (e) ≈", math.e)
