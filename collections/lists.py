"""
lists.py

🔰 Purpose:
This file explains how Python handles lists.

👩‍💻 Created for personal Python 3.13 learning

📘 What is a List?
A list is an ordered, mutable (changeable) collection of items.
It can hold elements of different data types.

📘 Why use Lists?
- Store multiple values in a single variable
- Easily add/remove/update items
- Commonly used in loops, conditions, and data processing

📘 Syntax:
------------------------------------------------
my_list = [item1, item2, item3]
"""

# ✅ Creating lists
numbers = [1, 2, 3, 4, 5]
mixed = [10, "Tashy", True, 3.14]

# ✅ Accessing items (index starts at 0)
print("First item:", numbers[0])     # 1
print("Last item:", numbers[-1])     # 5

# ✅ Modifying items
numbers[2] = 99
print("Updated list:", numbers)      # [1, 2, 99, 4, 5]

# ✅ Adding items
numbers.append(6)                    # Add to end
numbers.insert(1, 100)               # Insert at index 1
print("After append & insert:", numbers)

# ✅ Removing items
numbers.remove(99)                   # Remove specific value
popped_item = numbers.pop()          # Remove last item
print("After remove & pop:", numbers)
print("Popped item:", popped_item)

# ✅ List length
print("Length of list:", len(numbers))

# ✅ Looping through a list
print("Looping through list:")
for num in numbers:
    print(num)

# ✅ Checking if an item exists
if 4 in numbers:
    print("4 is in the list")

# ✅ Sorting and reversing
numbers.sort()                       # Ascending sort
print("Sorted list:", numbers)

numbers.reverse()                    # Reverses list
print("Reversed list:", numbers)

# ✅ Copying a list
copy_list = numbers.copy()
print("Copied list:", copy_list)

# ✅ Slicing a list
print("First 3 items:", numbers[:3])
print("Last 2 items:", numbers[-2:])

# ✅ List comprehension
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)           # [1, 4, 9, 16, 25]

# ✅ Nested lists
matrix = [[1, 2], [3, 4], [5, 6]]
print("Element [1][1]:", matrix[1][1])  # 4
