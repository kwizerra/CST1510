"""
SENTINEL LOOPS AND RUNNING TOTALS
==================================
Looping until a signal value appears, and keeping a total as you go.
Run:  python 02_sentinel_and_running_total.py
"""

# --- 1. A sentinel is a value that means "stop" -----------------------------
# "quit" here is not data - it is a signal. Check for it before you use
# the value as a real one.

while True:
    label = input("Record ID (or 'quit'): ")
    if label == "quit":
        break
    print(f"checking {label}...")


# --- 2. Running total ---------------------------------------------------
# Start the total at 0 BEFORE the loop. Add to it INSIDE the loop.

total = 0

while True:
    entry = input("Enter a number (or 'done'): ")
    if entry == "done":
        break
    total += float(entry)

print(f"Total: {total}")


# --- 3. Counting how many times something happened ---------------------
# Same pattern as a running total, but adding 1 instead of a value.

over_limit_count = 0
checked = 0

while checked < 3:
    value = float(input("Value: "))
    limit = float(input("Limit: "))
    if value > limit:
        over_limit_count += 1
    checked += 1

print(f"{over_limit_count} of {checked} were over limit")


# --- 4. continue: skip, do not stop --------------------------------------

n = 0
while n < 5:
    n += 1
    if n == 3:
        continue     # skip printing 3, but keep looping
    print(n)


# --- 5. Same idea, three fields ---------------------------------------------
# Same shape - keep going until a signal says stop - three domains.

batches = [50, 50, 50, 0]                 # AI / Data Science - 0 means no more data
i = 0
while batches[i] > 0:
    print("processing batch of", batches[i], "rows")
    i += 1

log_lines = ["ok", "ok", "FAIL", "END"]   # Cyber Security - stop at a sentinel line
i = 0
while log_lines[i] != "END":
    if log_lines[i] == "FAIL":
        print("suspicious line")
    i += 1

statuses = ["down", "down", "healthy"]    # IT - keep checking until it responds healthy
i = 0
while statuses[i] != "healthy":
    print("still down, checking again")
    i += 1
print("server is healthy")


# --- TRY IT ------------------------------------------------------------------
# 1. Adapt section 2 so it also counts how many numbers were entered.
# 2. Adapt section 3 so it stops on "quit" instead of after exactly 3 checks.
# 3. In section 4, change the condition so it skips every EVEN number instead.
