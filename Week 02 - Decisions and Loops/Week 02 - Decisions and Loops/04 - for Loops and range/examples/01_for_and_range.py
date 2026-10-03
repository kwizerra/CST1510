"""
FOR AND RANGE
=============
Repeat a known number of times.   Run:  python 01_for_and_range.py
"""

# --- 1. for i in range(n) -----------------------------------------------
# Repeats exactly n times. i takes 0, 1, 2, ... up to (but not including) n.

for i in range(5):
    print(i)          # 0 1 2 3 4  - five lines, starts at 0


# --- 2. range(start, stop) -----------------------------------------------
# stop is NEVER included. This catches everyone at least once.

for i in range(1, 6):
    print(i)          # 1 2 3 4 5

for i in range(1, 5):
    print(i)          # 1 2 3 4  - NOT 1 2 3 4 5. Off by one if you expected 5.


# --- 3. range(start, stop, step) ------------------------------------------

for i in range(2, 11, 2):
    print(i)           # 2 4 6 8 10  - every other number

for i in range(10, 0, -1):
    print(i)            # 10 9 8 ... 1  - counting down needs a negative step


# --- 4. i does not have to be used ------------------------------------------
# Sometimes you only care about repeating, not the number itself.

for i in range(3):
    print("checking a record")   # runs 3 times, i is ignored


# --- 5. Changing i inside the loop has no effect -----------------------------
# range() already decided every value before the loop started.

for i in range(3):
    print(i)
    i = 100   # has no effect on the next value of i

# still prints 0 1 2, not 0 100 100


# --- 6. enumerate() - the index and the value, together ---------------------
# No counter to track by hand - enumerate() hands you both.

for i, letter in enumerate("cat"):
    print(i, letter)           # 0 c / 1 a / 2 t

for i, host in enumerate(["srv-01", "srv-02", "srv-03"], start=1):
    print(f"server {i}: {host}")     # server 1: srv-01 / server 2: srv-02 / ...

# WATCH OUT: forgetting to unpack both parts.
# for pair in enumerate("cat"):
#     print(pair)   # (0, 'c')  (1, 'a')  (2, 't') - one tuple, not two values


# --- 7. Same idea, three fields ---------------------------------------------
# Same shape - a fixed, known number of repeats - three domains.

n = 5
for row in range(n):
    print("processing row", row)                 # AI / Data Science - a fixed batch of n rows

known_ips = ["10.0.0.5", "10.0.0.9", "192.168.1.1"]
for ip in known_ips:
    print("checking", ip)                        # Cyber Security - a fixed list of known IPs

servers = ["srv-01", "srv-02", "srv-03"]
for host in servers:
    print("pinging", host)                       # IT - a fixed set of servers


# --- TRY IT ------------------------------------------------------------------
# 1. Print "Record 1" through "Record 5" (not 0 through 4).
# 2. Print every multiple of 5 from 5 to 50.
# 3. Print the numbers 20 down to 0, counting by 4s.
