"""
file_handling_intro.py

🔰 Purpose:
This file introduces the basics of file handling in Python.

👩‍💻 Created for personal Python 3.13 learning

📘 Why File Handling?
- Store and retrieve data permanently
- Read config files, logs, documents
- Process text and automation

📘 File Modes in Python:
------------------------------------------------
"r"  → Read (default), error if file not found
"w"  → Write, creates file if not exists, **overwrites**
"a"  → Append, creates file if not exists
"x"  → Create, **fails** if file exists
"b"  → Binary mode
"+"  → Read and write

📘 Common Functions:
------------------------------------------------
open()      → Opens the file
read()      → Reads content
write()     → Writes string
readlines() → Reads all lines into a list
close()     → Closes file (not needed with `with` block)
"""

# ✅ Open and close manually
file = open("sample.txt", "w")      # Create file if not exists
file.write("Hello, Boss!\n")
file.write("This is Python 3.13 file handling.\n")
file.close()  # Always close to save changes

# ✅ Using 'with' (auto-closes even if error occurs)
with open("sample.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)

# ✅ Appending new line
with open("sample.txt", "a") as file:
    file.write("Appended line using append mode.\n")

# ✅ Reading line-by-line
with open("sample.txt", "r") as file:
    print("\nLine-by-line reading:")
    for line in file:
        print(line.strip())
