"""
delete_files.py

🔰 Purpose:
This file explains how to delete files and directories in Python.

👩‍💻 Created for personal Python 3.13 learning

📘 Deletion Tools:
------------------------------------------------
✅ os.remove(path)        → Deletes a file
✅ os.rmdir(path)         → Deletes an empty folder
✅ shutil.rmtree(path)    → Deletes a folder with all contents

⚠️ Always check if the file/folder exists before deleting.
"""

import os
import shutil

# ✅ Deleting a file
file_path = "write_demo.txt"
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"✅ File '{file_path}' deleted.")
else:
    print(f"⚠️ File '{file_path}' does not exist.")

# ✅ Deleting an empty directory
empty_folder = "temp_folder"
os.makedirs(empty_folder, exist_ok=True)  # Create test folder

if os.path.exists(empty_folder):
    os.rmdir(empty_folder)
    print(f"✅ Empty folder '{empty_folder}' deleted.")

# ✅ Deleting a folder with contents
full_folder = "sample_data"
os.makedirs(full_folder, exist_ok=True)
with open(f"{full_folder}/dummy.txt", "w") as f:
    f.write("Temporary file.")

if os.path.exists(full_folder):
    shutil.rmtree(full_folder)
    print(f"✅ Folder '{full_folder}' with contents deleted.")

# ✅ Try-catch block to avoid crashes
try:
    os.remove("non_existent_file.txt")
except FileNotFoundError:
    print("⚠️ Tried to delete a file that doesn't exist.")
