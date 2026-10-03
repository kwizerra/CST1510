"""
IF / ELIF / ELSE
================
Choosing which lines actually run.   Run:  python 01_if_elif_else.py
"""

# --- 1. if -------------------------------------------------------------
# The indented block only runs when the condition is True.

value = 23.7
limit = 20

if value > limit:
    print("OVER")


# --- 2. else -----------------------------------------------------------
# Runs when the if condition was False. Exactly one of the two branches runs.

if value > limit:
    print("OVER")
else:
    print("OK")


# --- 3. elif -------------------------------------------------------------
# Checked top to bottom. The first True one runs, the rest are skipped -
# even if they are also True.

percent = 95.0

if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"

print(status)   # WARNING - the 100 check was False, so Python moved on


# --- 4. Order matters ---------------------------------------------------
# Put the most specific condition first. This is WRONG:

percent = 105.0

if percent >= 90:            # True first - so this branch runs
    status = "WARNING"       # ...even though 105 should be OVER LIMIT
elif percent >= 100:
    status = "OVER LIMIT"

print(status)   # WARNING - wrong. Should check >= 100 first.


# --- 5. Same idea, three fields -----------------------------------------------

missing_pct = 7.5
if missing_pct > 5:
    print("check pipeline")                     # AI / Data Science

failed_logins = 3
if failed_logins >= 3:
    print("LOCKED")                              # Cyber Security

disk_used_pct = 92
if disk_used_pct >= 90:
    print("ALERT")                               # IT


# --- TRY IT ------------------------------------------------------------------
# 1. Fix section 4 by swapping the order of the two conditions.
# 2. Given attempts = 3 and max_attempts = 3, print "LOCKED" if attempts is at
#    or over the max, otherwise "OK".
# 3. Add a WARNING branch that fires when attempts is exactly one below the max.
