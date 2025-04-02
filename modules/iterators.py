"""
iterators.py

🔰 Purpose:
This file explains how iterators work in Python.

👩‍💻 Created for personal Python 3.13 learning

📘 What is an Iterator?
An iterator is an object that allows you to **loop** through a collection one item at a time.

📘 Iterator Protocol:
------------------------------------------------
1. __iter__() → returns the iterator object
2. __next__() → returns the next value, or raises StopIteration

📘 Why use Iterators?
- Build custom looping logic
- Handle infinite sequences
- Lazy evaluation (memory efficient)
"""

# ✅ Example: using iterator on a list
my_list = [1, 2, 3]
iterator = iter(my_list)

print("Next item:", next(iterator))  # 1
print("Next item:", next(iterator))  # 2
print("Next item:", next(iterator))  # 3
# print(next(iterator))  # ❌ Raises StopIteration

# ✅ Custom iterator class
class CountDown:
    def __init__(self, start):
        self.num = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 0:
            raise StopIteration
        current = self.num
        self.num -= 1
        return current

print("\n🔁 Custom CountDown:")
for number in CountDown(5):
    print(number)

# ✅ Looping with generators (simpler alternative)
def count_up(limit):
    n = 1
    while n <= limit:
        yield n
        n += 1

print("\n🔁 Generator count_up:")
for val in count_up(3):
    print(val)
