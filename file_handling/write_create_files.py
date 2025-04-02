"""
write_create_files.py

🔰 Purpose:
This file explains how to write or create files in Python.

👩‍💻 Created for personal Python 3.13 learning

📘 File Write Modes:
------------------------------------------------
"w" → Write (creates new or **overwrites** existing)
"a" → Append (adds to end, doesn't delete existing)
"x" → Create (fails if file already exists)

📘 Write Methods:
------------------------------------------------
.write("text")     → Writes a string
.writelines(list)  → Writes list of strings (no \n auto)
"""

# ✅ Writing to a file (overwrite if exists)
with open("write_demo.txt", "w") as file:
    file.write("First line of text.\n")
    file.write("Second line added.\n")
print("✅ File created and overwritten successfully.")

# ✅ Appending to a file
with open("write_demo.txt", "a") as file:
    file.write("Third line using append mode.\n")
print("✅ Appended successfully.")

# ✅ Writing multiple lines with writelines()
lines = ["Line 4\n", "Line 5\n", "Line 6\n"]
with open("write_demo.txt", "a") as file:
    file.writelines(lines)
print("✅ Multiple lines written.")

# ✅ Creating a file using 'x' (throws error if file exists)
# try:
#     with open("new_file_created.txt", "x") as file:
#         file.write("Brand new file created.\n")
#     print("✅ File created using mode 'x'")
# except FileExistsError:
#     print("⚠️ File already exists!")

# ✅ Confirming written content
with open("write_demo.txt", "r") as file:
    print("\n🔍 Final content:")
    print(file.read())
