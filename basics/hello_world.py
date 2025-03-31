"""
hello_world.py

🔰 Purpose:
This file introduces the basics of Python:
- How to print messages using print()
- How to use variables
- How to define and call functions
- How to use f-strings for dynamic output
- What __name__ == "__main__" means

👩‍💻 Created for personal Python 3.13 learning

📘 Python Basics Reference:
-------------------------------------
def                  → Used to define a function in Python
print()              → Displays output on the screen
variable = value     → Stores data (like text or numbers) in a variable
f"Hello, {name}"     → Formatted string (f-string) to include variables inside text
if __name__ == "__main__":
                     → Makes sure code runs only when the file is run directly
"""

# A simple function that prints "Hello, World!" when called
def simple_hello():
    print("Hello, World!")

# Another function that uses a variable to store the message
def hello_with_variable():
    message = "Hello, World!"
    print(message)

# A function that takes a name as input and prints a personalized message
def hello_with_name(name):
    print(f"Hello, {name}!")

# This part only runs when this file is run directly (not imported)
if __name__ == "__main__":
    simple_hello()
    hello_with_variable()
    hello_with_name("Tashy")
