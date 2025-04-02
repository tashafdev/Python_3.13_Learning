


"""
classes_objects.py

🔰 Purpose:
This file explains how to define and use classes and objects in Python.

👩‍💻 Created for personal Python 3.13 learning

📘 What is a Class?
A class is a blueprint for creating objects.

📘 What is an Object?
An object is an instance of a class.

📘 Why use OOP?
- Organize code better
- Reuse with inheritance
- Encapsulate logic
"""

# ✅ Defining a class
class Person:
    # Constructor (called when object is created)
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age

    # Method (function inside class)
    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

# ✅ Creating objects
person1 = Person("Tashy", 25)
person2 = Person("Alice", 30)

# ✅ Calling methods
person1.greet()
person2.greet()

# ✅ Accessing object attributes
print("Name of person1:", person1.name)
print("Age of person2:", person2.age)

# ✅ Changing attribute value
person1.age = 26
print("Updated age of person1:", person1.age)

# ✅ Deleting an attribute
del person2.age
# print(person2.age)  # ❌ Will raise AttributeError

# ✅ Deleting an object
# del person1
# print(person1)  # ❌ Will raise NameError

class Dog:
    # 🐾 Class variable (shared by all dogs)
    species = "Canis familiaris"

    def __init__(self, name, age):
        # 🐶 Instance variables (unique for each dog)
        self.name = name
        self.age = age

    def describe(self):
        print(f"{self.name} is {self.age} years old and belongs to species {Dog.species}")

# ✅ Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Rocky", 5)

# ✅ Accessing class variable
print(dog1.species)  # Canis familiaris
print(dog2.species)  # Canis familiaris

# ✅ Changing instance variable
dog1.age = 4
print(f"{dog1.name}'s new age:", dog1.age)

# ✅ Changing class variable (affects all unless overridden)
Dog.species = "Canis lupus"
print(dog1.species)  # Canis lupus
print(dog2.species)  # Canis lupus

# ❗️ Overriding class variable for one object (not recommended unless needed)
dog1.species = "Wolf Dog"
print("dog1:", dog1.species)   # Wolf Dog
print("dog2:", dog2.species)   # Canis lupus
