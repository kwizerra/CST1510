"""
BOOLEAN LOGIC
=============
Combining more than one condition with and / or / not.   Run:  python 02_boolean_logic.py
"""

# --- 1. and -------------------------------------------------------------
# True only when BOTH sides are True.

percent = 95.0

print(percent >= 90 and percent < 100)   # True  - inside the warning band
print(percent >= 90 and percent > 100)   # False - second half is False


# --- 2. or ----------------------------------------------------------------
# True when AT LEAST ONE side is True.

failed_logins = 0
locked_out    = True

print(failed_logins >= 3 or locked_out)   # True - locked_out alone is enough


# --- 3. not -----------------------------------------------------------------
# Flips True to False and False to True.

within_limit = percent < 100

print(within_limit)       # False
print(not within_limit)   # True


# --- 4. Bracket each comparison ----------------------------------------------
# Costs nothing, removes all doubt about what is being combined.

value = 87
limit = 100

print((value / limit * 100 >= 90) and (value / limit * 100 < 100))


# --- 5. and / or short-circuit -----------------------------------------------
# Python stops checking as soon as the answer is certain.
# This print never runs the right-hand side, because the left side is already False.

print(False and 1 / 0 == 1)   # False - no ZeroDivisionError, Python never got that far


# --- 6. Same idea, three fields -----------------------------------------------
# A comparison is the universal "does this cross a line?" check.

missing_pct = 7.5
print(missing_pct > 5)                     # AI / Data Science - is the missing-data rate too high?

failed_logins2 = 3
print(failed_logins2 >= 3)                 # Cyber Security - should this account be locked?

disk_used_pct = 92
print(disk_used_pct >= 90)                 # IT - is storage nearly full?


# --- TRY IT ------------------------------------------------------------------
# 1. Write one line that checks whether percent is between 90 and 100 inclusive.
# 2. Set locked = False and attempts = 5. Print True if the account should be
#    locked because EITHER locked is already True OR attempts is 3 or more.
# 3. Predict, then check: not (3 > 2)
