"""
read_files.py

🔰 Purpose:
This file explains different ways to read files in Python.

👩‍💻 Created for personal Python 3.13 learning

📘 Reading Modes:
------------------------------------------------
"r"   → Read text
"rb"  → Read binary

📘 Common Read Methods:
------------------------------------------------
.read()       → Read entire content as string
.readline()   → Read one line at a time
.readlines()  → Read all lines into a list
for loop      → Best for line-by-line processing
"""

# ✅ 1. Read full content using .read()
with open("sample.txt", "r") as file:
    content = file.read()
    print("🔹 .read():\n", content)

# ✅ 2. Read one line using .readline()
with open("sample.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print("🔹 .readline():")
    print("Line 1:", line1.strip())
    print("Line 2:", line2.strip())

# ✅ 3. Read all lines using .readlines()
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print("🔹 .readlines() as list:", lines)

# ✅ 4. Loop through lines (best practice for large files)
print("\n🔹 Looping line-by-line:")
with open("sample.txt", "r") as file:
    for i, line in enumerate(file, start=1):
        print(f"Line {i}:", line.strip())

# ✅ 5. Read binary file (e.g., image) (optional example)
# with open("example.jpg", "rb") as img_file:
#     data = img_file.read()
#     print("Binary file read successfully. Bytes:", len(data))
