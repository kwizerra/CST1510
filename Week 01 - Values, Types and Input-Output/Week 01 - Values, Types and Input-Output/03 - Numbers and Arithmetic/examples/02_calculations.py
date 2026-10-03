"""
CALCULATIONS
============
The sums you will actually write.   Run:  python 02_calculations.py
"""

# --- 1. The calculation you will write most often --------------------------
# "What share of the whole is this?"     (part / total) * 100

value = 23.7
limit = 20

difference = value - limit
percent = (value / limit) * 100

print("Difference:", difference)      # 3.6999999999999993
print("Percent   :", percent)         # 118.5

# WATCH OUT: look at the difference - 3.6999999999999993, not 3.7.
# That is not a bug. Computers store decimals approximately, so some sums
# come out slightly off. It stops mattering once you format the output:
print(f"{percent:.1f} %")             # 118.5 %


# --- 2. The same sum, three different jobs ---------------------------------
# AI / Data Science - what share of rows are missing a value
missing_rows = 38
total_rows = 250
print("missing:", (missing_rows / total_rows) * 100, "%")

# Cyber - what share of login attempts failed
failed = 12
attempts = 400
print("failed :", (failed / attempts) * 100, "%")

# IT - what share of the disk is used
used_gb = 87
total_gb = 120
print("disk   :", (used_gb / total_gb) * 100, "%")

# One formula, three fields. This is most of first-year data work.


# --- 3. Building on a result -----------------------------------------------
# Once a value is stored you can use it in the next calculation.

free_gb = total_gb - used_gb
percent_free = (free_gb / total_gb) * 100

print("free   :", free_gb, "GB")
print("free % :", percent_free)


# --- 4. Shorthand: changing a variable using itself -------------------------
# So common it has a short form. These two lines do exactly the same thing.

count = 0
count = count + 1        # the long way
count += 1               # the short way
print(count)             # 2

total = 100
total -= 30              # 70
total *= 2               # 140
print(total)             # 140

# -=  *=  /=  //=  %=  all work the same way.


# --- TRY IT ----------------------------------------------------------------
# 1. A batch of 250 records ran, 38 failed. Print how many passed, the
#    percentage that failed, and the percentage that passed.
# 2. Do it without typing any number you could calculate.
# 3. Start total at 100. Subtract 30, then double it, using short forms.
