"""
FOR VS WHILE
============
Same job, two tools. Picking the right one.   Run:  python 02_for_vs_while.py
"""

# --- 1. Know the count in advance -> for -------------------------------
# Checking exactly 3 records, whatever the values turn out to be.

for i in range(3):
    label = input("Record ID: ")
    value = float(input("Value: "))
    limit = float(input("Limit: "))

    if value > limit:
        print(f"{label}: OVER LIMIT")
    else:
        print(f"{label}: OK")


# --- 2. Do NOT know the count -> while -----------------------------------
# Checking records until the user is done. Could be 1, could be 50.

while True:
    label = input("Record ID (or 'quit'): ")
    if label == "quit":
        break
    value = float(input("Value: "))
    limit = float(input("Limit: "))

    if value > limit:
        print(f"{label}: OVER LIMIT")
    else:
        print(f"{label}: OK")


# --- 3. The tell -----------------------------------------------------------
# If you can say the exact number before the loop starts: for.
# If the loop should stop because of something that happens DURING it: while.


# --- 4. for can still stop early with break ---------------------------------
# Even with a known count, you can leave before it finishes.

for i in range(10):
    value = float(input("Value (or -1 to stop early): "))
    if value == -1:
        break
    print(value)


# --- TRY IT ------------------------------------------------------------------
# 1. Which tool would you use to print the 12 times table? Write it.
# 2. Which tool would you use to keep retrying a password until it is
#    correct? Write it.
# 3. Rewrite section 1 as a while loop that also works for any number of
#    records, not just exactly 3.
