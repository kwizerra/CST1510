"""
RECORD CHECK  -  Week 2 version
================================
Run it with:    python record_check.py

    Week 1   input, calculate, print
    Week 2   it can make decisions          <- this version
    Week 3   it is built from functions
    Week 4   it reads many records from a file
    Week 5   it becomes a reusable component
    Week 6   it does the whole job in a few lines

Same problem as last week. This time it decides a proper status instead of
printing a raw percentage, and it checks as many records as you like instead
of stopping after one.

Type "quit" as the Record ID to stop.

You are not expected to understand every line today. One line uses an idea
from Week 3 and is marked.
"""

while True:

    # ------------------------------------------------------------------ INPUT
    record_id = input("Record ID (or 'quit') : ")
    if record_id == "quit":
        break

    value = float(input("Value     : "))
    limit = float(input("Limit     : "))

    # ---------------------------------------------------------------- STORE
    # Week 4. For now, one record still lives in three variables.

    # ---------------------------------------------------------------- PROCESS
    difference = value - limit
    percent    = (value / limit) * 100        # <- Week 3 will pull this out into a function

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    # ----------------------------------------------------------------- OUTPUT
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record_id}")
    print("=" * 34)
    print(f"  Value       : {value:>10.2f}")
    print(f"  Limit       : {limit:>10.2f}")
    print(f"  Difference  : {difference:>+10.2f}")
    print(f"  Of limit    : {percent:>9.1f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)
    print()

print("Done. Checked and reported.")
