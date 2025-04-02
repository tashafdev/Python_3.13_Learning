"""
conditions.py

🔰 Purpose:
This file explains all conditional statements in Python.

👩‍💻 Created for personal Python 3.13 learning

📘 What are Conditions?
Conditions allow you to execute certain code only when a specific requirement is met.

📘 Where are Conditions used?
- Decision making (if/else)
- Loops
- Validations
- Logical flows

📘 Common Comparison Operators:
------------------------------------------------
==    → Equal to
!=    → Not equal to
>     → Greater than
<     → Less than
>=    → Greater than or equal to
<=    → Less than or equal to

📘 Logical Operators:
------------------------------------------------
and   → True if both conditions are True
or    → True if at least one condition is True
not   → Reverses the result
"""

# ✅ Basic if statement
x = 10
if x > 5:
    print("x is greater than 5")  # ✅ This will be printed


# ✅ if...else statement
age = 17
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")  # ✅ This will be printed


# ✅ if...elif...else ladder
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")  # ✅ This will be printed
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")


# ✅ Nested if statement
num = 15
if num > 10:
    if num < 20:
        print("Number is between 10 and 20")  # ✅ Nested condition is also true


# ✅ One-line if statement
score = 95
if score > 90: print("Excellent score!")  # ✅ One-liner if


# ✅ One-line if...else (Ternary Operator)
value = 30
status = "High" if value > 20 else "Low"
print("Status:", status)  # ✅ Will print "High"


# ✅ Logical Operators
a = 5
b = 10
if a < 10 and b > 5:
    print("Both conditions are True")  # ✅ and condition

if a > 3 or b < 3:
    print("At least one condition is True")  # ✅ or condition

if not a > b:
    print("a is not greater than b")  # ✅ not condition


# ✅ Using 'in' with if
colors = ['red', 'green', 'blue']
if 'green' in colors:
    print("Green is available")  # ✅ True


# ✅ Using 'is' with if
x = None
if x is None:
    print("x is None")  # ✅ Checks object identity


# ✅ Comparing variables
x = 10
y = 20
if x == y:
    print("x and y are equal")
elif x < y:
    print("x is less than y")  # ✅ True
else:
    print("x is greater than y")
