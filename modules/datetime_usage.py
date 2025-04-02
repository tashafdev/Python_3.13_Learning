"""
datetime_usage.py

🔰 Purpose:
This file explains how to use the datetime module in Python.

👩‍💻 Created for personal Python 3.13 learning

📘 Why use datetime?
- Work with dates and times
- Build timestamps, countdowns, schedulers
- Format for logs and reports

📘 Core Classes:
------------------------------------------------
datetime.date      → Deals with dates (Y-M-D)
datetime.time      → Deals with time (H:M:S)
datetime.datetime  → Combines both
datetime.timedelta → For date/time math
"""

from datetime import date, time, datetime, timedelta

# ✅ Current date and time
print("Current date:", date.today())
print("Current datetime:", datetime.now())

# ✅ Creating custom date/time objects
custom_date = date(2025, 4, 2)
custom_time = time(14, 30, 15)
custom_dt = datetime(2025, 4, 2, 14, 30)

print("Custom date:", custom_date)
print("Custom time:", custom_time)
print("Custom datetime:", custom_dt)

# ✅ Formatting dates (strftime)
now = datetime.now()
print("Formatted date:", now.strftime("%d-%b-%Y"))
print("Formatted time:", now.strftime("%H:%M:%S"))
print("Day name:", now.strftime("%A"))

# ✅ Parsing strings to date (strptime)
date_str = "2025-04-02"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
print("Parsed datetime:", parsed_date)

# ✅ Time difference using timedelta
today = date.today()
future = today + timedelta(days=5)
past = today - timedelta(weeks=2)

print("5 days later:", future)
print("2 weeks ago:", past)

# ✅ Countdown Example
event_date = datetime(2025, 12, 31, 23, 59)
remaining = event_date - datetime.now()
print("⏳ Days until New Year:", remaining.days)
