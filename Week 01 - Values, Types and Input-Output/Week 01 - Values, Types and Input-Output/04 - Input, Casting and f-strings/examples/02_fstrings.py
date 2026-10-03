"""
F-STRINGS AND FORMATTING
========================
Putting values inside text, and making a report line up.
Run:  python 02_fstrings.py
"""

record_id = "R-004"
value = 23.7
limit = 20.0
difference = value - limit
percent = (value / limit) * 100

# --- 1. An f-string puts values inside text --------------------------------
# Put f before the quotes. Anything in { } is worked out and dropped in.

print(f"Record {record_id} has value {value}")
# Output:  Record R-004 has value 23.7

# You can calculate inside the braces too.
print(f"Over the limit by {value - limit}")

# WATCH OUT: forgetting the f is the most common slip. This prints the braces:
print("Record {record_id}")               # Record {record_id}


# --- 2. Decimal places -----------------------------------------------------
# :.2f means "2 digits after the point". The f stands for float.

print(f"{percent}")                       # 118.5
print(f"{percent:.2f}")                   # 118.50
print(f"{percent:.0f}")                   # 118

# This is also how you hide the odd trailing digits floats sometimes produce.
print(f"{difference}")                    # 3.6999999999999993
print(f"{difference:.2f}")                # 3.70


# --- 3. Alignment - what makes a report look like a report -----------------
#   :>10    right-aligned in 10 characters
#   :<10    left-aligned
#   :^10    centred
#   :+      always show the sign, even when positive

print("--- no alignment ---")
print(f"Value : {value}")
print(f"Limit : {limit}")
print(f"Diff  : {difference}")

print("--- aligned ---")
print(f"Value : {value:>10.2f}")
print(f"Limit : {limit:>10.2f}")
print(f"Diff  : {difference:>+10.2f}")
# Output:  Value :      23.70
#          Limit :      20.00
#          Diff  :      +3.70      <- decimal points line up

# Left-align is for names, right-align is for numbers.
print(f"{'srv-01':<12}{87:>6}")           # srv-01          87


# --- 4. A finished report --------------------------------------------------

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {record_id}")
print("=" * 34)
print(f"  Value       : {value:>10.2f}")
print(f"  Limit       : {limit:>10.2f}")
print(f"  Difference  : {difference:>+10.2f}")
print(f"  Of limit    : {percent:>9.1f} %")
print("=" * 34)


# --- 5. Same idea, three fields ---------------------------------------------
# Ask for something, convert it, report it back cleanly.

mean, n = 23.7, 1200
print(f"Mean: {mean:.2f} over {n} rows")                          # AI / Data Science

level, failed, ip = "ALERT", 12, "10.0.0.5"
print(f"[{level}] {failed} failed logins from {ip}")              # Cyber Security

hostname, used = "srv-01", 87
print(f"{hostname:<12} disk {used:>3} %")                         # IT


# --- TRY IT ----------------------------------------------------------------
# 1. Print 7 / 3 to exactly three decimal places.
# 2. Print your name left-aligned in 15 characters, then a number right-
#    aligned in 8. Do it for three different names and check they line up.
# 3. Remove the f from one line above. Run it. Put it back.
