"""
json_usage.py

🔰 Purpose:
This file explains how to work with JSON in Python using the `json` module.

👩‍💻 Created for personal Python 3.13 learning

📘 What is JSON?
JSON (JavaScript Object Notation) is a lightweight data format used for:
- Storing structured data
- Exchanging data between systems (e.g., APIs)

📘 JSON ⇄ Python Mapping:
------------------------------------------------
JSON            → Python
-----------------------------
object          → dict
array           → list
string          → str
number          → int/float
true/false      → True/False
null            → None
"""

import json

# ✅ Python dict → JSON string (serialization)
person = {
    "name": "Tashy",
    "age": 25,
    "is_admin": False,
    "skills": ["Python", "Android", "ML"]
}

json_str = json.dumps(person)
print("Serialized JSON string:\n", json_str)

# ✅ JSON string → Python dict (deserialization)
parsed_data = json.loads(json_str)
print("Deserialized back to dict:\n", parsed_data)
print("Name:", parsed_data["name"])

# ✅ Writing JSON to a file
with open("user.json", "w") as file:
    json.dump(person, file, indent=4)
print("✅ JSON written to file.")

# ✅ Reading JSON from a file
with open("user.json", "r") as file:
    loaded_data = json.load(file)
print("📂 Loaded from file:", loaded_data)

# ✅ Handling JSON errors
invalid_json = '{"name": "Tashy", "age": 25,'  # Invalid due to comma

try:
    result = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print("❌ JSON error:", e)
