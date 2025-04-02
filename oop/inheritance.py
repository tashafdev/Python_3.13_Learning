"""
inheritance.py

🔰 Purpose:
This file explains how Python supports inheritance in object-oriented programming.

👩‍💻 Created for personal Python 3.13 learning

📘 What is Inheritance?
Inheritance allows a class (child) to inherit attributes and methods from another class (parent).

📘 Why use Inheritance?
- Reuse code
- Extend existing behavior
- Establish relationships between classes

📘 Types of Inheritance:
------------------------------------------------
1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hierarchical Inheritance
"""

# ✅ 1. Single Inheritance
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks 🐶")

dog = Dog()
dog.speak()  # Inherited
dog.bark()   # Own method

# ✅ 2. Multilevel Inheritance
class Animal:
    def move(self):
        print("Animal moves")

class Bird(Animal):
    def fly(self):
        print("Bird flies")

class Parrot(Bird):
    def talk(self):
        print("Parrot talks 🦜")

parrot = Parrot()
parrot.move()  # From Animal
parrot.fly()   # From Bird
parrot.talk()  # From Parrot

# ✅ 3. Multiple Inheritance
class Father:
    def skill(self):
        print("Father: Programming")

class Mother:
    def skill(self):
        print("Mother: Designing")

class Child(Father, Mother):
    def skill(self):
        print("Child: Combines both")

child = Child()
child.skill()  # Will use Child's own method

# ✅ 4. Hierarchical Inheritance
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def drive(self):
        print("Car is driving 🚗")

class Bike(Vehicle):
    def ride(self):
        print("Bike is riding 🏍️")

car = Car()
bike = Bike()
car.start()
bike.start()

# ✅ Using super() to call parent methods
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Person:", self.name)

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)  # Call parent constructor
        self.course = course

    def show(self):
        super().show()
        print("Course:", self.course)

student = Student("Tashy", "Python 3.13 OOP")
student.show()
