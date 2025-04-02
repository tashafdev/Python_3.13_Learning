"""
abstract_classes.py

🔰 Purpose:
This file explains how Python supports abstract classes and interface-like behavior using the `abc` module.

👩‍💻 Created for personal Python 3.13 learning

📘 What is an Abstract Class?
An abstract class cannot be instantiated directly. It can define abstract methods that must be implemented by subclasses.

📘 Does Python support Interfaces?
- No native interface keyword.
- Abstract base classes (ABCs) with only abstract methods behave like interfaces.

📘 Use-case:
Use abstract classes to enforce structure across subclasses.
"""

from abc import ABC, abstractmethod

# ✅ Abstract Base Class (ABC)
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# ❌ Can't instantiate abstract class
# shape = Shape()  # TypeError

# ✅ Subclass implementing all abstract methods
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(4, 5)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())

# ✅ Abstract Class behaving like Interface
class Flyer(ABC):
    @abstractmethod
    def fly(self):
        pass

class Swimmer(ABC):
    @abstractmethod
    def swim(self):
        pass

# ✅ Multiple Inheritance from interface-like abstract classes
class Duck(Flyer, Swimmer):
    def fly(self):
        print("Duck flies")

    def swim(self):
        print("Duck swims")

donald = Duck()
donald.fly()
donald.swim()
