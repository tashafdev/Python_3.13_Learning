"""
regex_usage.py

🔰 Purpose:
This file explains how to use Regular Expressions (regex) in Python using the `re` module.

👩‍💻 Created for personal Python 3.13 learning

📘 What is Regex?
Regex = Pattern matching tool for strings. Use it to:
- Validate inputs (email, phone, etc.)
- Search/replace patterns
- Extract specific parts of text

📘 Common Regex Patterns:
------------------------------------------------
.       → Any character except newline
^abc    → Start with "abc"
abc$    → Ends with "abc"
a|b     → Either "a" or "b"
[]      → Range or set of characters
\d      → Digit (0-9)
\w      → Word (a-z, A-Z, 0-9, _)
\s      → Whitespace
+       → One or more
*       → Zero or more
{n,m}   → Between n and m repetitions
"""

import re

# ✅ re.search() → Finds first match
text = "Boss level: Tashy2025"
match = re.search(r"Tashy\d+", text)
if match:
    print("🔍 Found match:", match.group())

# ✅ re.findall() → Returns all matches as a list
sentence = "The year 2023 was okay, 2024 is better, 2025 is best."
years = re.findall(r"\d{4}", sentence)
print("📅 All years:", years)

# ✅ re.sub() → Replace matching pattern
email_text = "Please contact at tashy@example.com"
cleaned = re.sub(r"\S+@\S+", "[email hidden]", email_text)
print("🔧 Replaced:", cleaned)

# ✅ re.match() → Only matches if pattern starts from beginning
line = "hello world"
result = re.match(r"hello", line)
if result:
    print("✅ Starts with 'hello'")

# ✅ Using raw strings (r"") to avoid escape issues
path = r"C:\Users\Boss"
print("Windows Path:", path)

# ✅ Validate email (basic pattern)
email = "tashy@domain.com"
pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
if re.match(pattern, email):
    print("✅ Valid email format")

# ✅ Extract all hashtags from a string
tweet = "Loving #Python and #AI in #2025!"
hashtags = re.findall(r"#\w+", tweet)
print("🔥 Hashtags found:", hashtags)
