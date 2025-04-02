"""
polymorphism.py

🔰 Purpose:
This file explains polymorphism in Python OOP.

👩‍💻 Created for personal Python 3.13 learning

📘 What is Polymorphism?
Polymorphism means "many forms" — the ability to use the same method name or operator for different types.

📘 Types of Polymorphism:
------------------------------------------------
1. Duck Typing
2. Operator Overloading
3. Method Overriding
4. Function Overloading (simulated using default args or *args)
"""

# ✅ 1. Duck Typing (if it walks like a duck...)
class Cat:
    def sound(self):
        print("Meow 🐱")

class Dog:
    def sound(self):
        print("Bark 🐶")

def make_sound(animal):
    animal.sound()  # Only cares that 'sound()' exists

cat = Cat()
dog = Dog()
make_sound(cat)
make_sound(dog)

# ✅ 2. Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print("Overloaded + result:", p3)

# ✅ 3. Method Overriding (child changes parent method)
class Vehicle:
    def move(self):
        print("Vehicle moves")

class Car(Vehicle):
    def move(self):
        print("Car drives 🚗")  # Overrides parent method

car = Car()
car.move()  # Uses Car’s version

# ✅ 4. Function Overloading (simulated using *args)
def add(*args):
    return sum(args)

print("Add 2 nums:", add(3, 4))
print("Add 3 nums:", add(1, 2, 3))
