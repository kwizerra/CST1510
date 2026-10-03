"""
OPERATORS
=========
The seven arithmetic operators.   Run:  python 01_operators.py
"""

# --- 1. All seven, on the same two numbers ---------------------------------

a = 17
b = 5

print("a + b  =", a + b)      # 22        add
print("a - b  =", a - b)      # 12        subtract
print("a * b  =", a * b)      # 85        multiply
print("a / b  =", a / b)      # 3.4       divide
print("a // b =", a // b)     # 3         divide, whole part only
print("a % b  =", a % b)      # 2         remainder
print("a ** b =", a ** b)     # 1419857   a to the power of b


# --- 2. / always gives a float ---------------------------------------------
# Even when it divides exactly. This surprises people.

print(10 / 2)                 # 5.0   <- note the .0, not 5
print(type(10 / 2))           # <class 'float'>


# --- 3. // and % split a number into parts ---------------------------------
# More useful than they look. // gives the whole part, % gives what is left.

print(10 // 3)                # 3
print(10 % 3)                 # 1

total_minutes = 137
hours = total_minutes // 60
minutes = total_minutes % 60
print(total_minutes, "minutes =", hours, "hours", minutes, "minutes")
# Output:  137 minutes = 2 hours 17 minutes


# --- 3b. Chain the split for more than one unit -----------------------------
# One split gives you two units. Do it again on what's left over for a third.
# Always work from the biggest unit down.

total_seconds = 4831

hours = total_seconds // 3600
remaining = total_seconds % 3600      # what's left after removing whole hours

minutes = remaining // 60
seconds = remaining % 60

print(total_seconds, "seconds =", hours, "hours,", minutes, "minutes,", seconds, "seconds")
# Output:  4831 seconds = 1 hours, 20 minutes, 31 seconds


# --- 4. Order of operations ------------------------------------------------
# Normal maths rules:  **  first, then  * / // %  , then  + -

print(2 + 3 * 4)              # 14  - the multiply happens first
print((2 + 3) * 4)            # 20  - brackets happen first

# HABIT WORTH FORMING: use brackets even when you do not need them.
# They cost nothing and remove all doubt about what you meant.

value = 23.7
limit = 20
print(value / limit * 100)      # works, but you have to think about it
print((value / limit) * 100)    # same answer, obvious intent


# --- 5. What goes wrong ----------------------------------------------------
# WATCH OUT: dividing by zero is a ZeroDivisionError, not a warning.
# Your program stops. Always ask whether the bottom number could be 0.
#
#     print(10 / 0)      ZeroDivisionError: division by zero


# --- TRY IT ----------------------------------------------------------------
# 1. Set a = 23, b = 4. Predict all seven answers BEFORE running.
# 2. Fix this so it means "10 plus 6, divided by 2":   print(10 + 6 / 2)
# 3. 500 seconds is how many whole minutes, and how many seconds left over?
# 4. 9137 seconds is how many hours, minutes and seconds? Chain the split
#    the way section 3b does - hours first, then split what's left over.
