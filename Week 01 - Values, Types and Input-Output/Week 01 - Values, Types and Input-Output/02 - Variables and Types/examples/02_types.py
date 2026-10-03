"""
TYPES
=====
Why "20" and 20 are not the same thing.   Run:  python 02_types.py
"""

# --- 1. Every value has a type ---------------------------------------------
# Three matter this week:
#     str    text            "R-004"   "OK"   "23.7"
#     int    whole number     20   0   -5
#     float  decimal number   23.7   1.0

record_id = "R-004"
value = 23.7
limit = 20

print(type(record_id))        # <class 'str'>
print(type(value))            # <class 'float'>
print(type(limit))            # <class 'int'>


# --- 2. The thing that catches everyone ------------------------------------
# These two print identically. They are NOT the same.

text_twenty = "20"
number_twenty = 20

print(text_twenty)            # 20
print(number_twenty)          # 20

print(type(text_twenty))      # <class 'str'>
print(type(number_twenty))    # <class 'int'>


# --- 3. Why it matters -----------------------------------------------------
# The type decides what an operator DOES.

print("20" + "20")            # 2020   <- text, glued together
print(20 + 20)                # 40     <- numbers, added

print("ab" * 3)               # ababab <- text, repeated
print(2 * 3)                  # 6      <- numbers, multiplied

# WATCH OUT: mixing them is a TypeError.
#     "20" + 20     TypeError: can only concatenate str to str
#
# When something behaves oddly, print the type. It is almost always this.


# --- 4. Whole numbers vs decimals ------------------------------------------
# int has no decimal part at all. float does, even when it is .0

print(type(10))               # <class 'int'>
print(type(10.0))             # <class 'float'>
print(type(10 / 2))           # <class 'float'>  <- division ALWAYS gives float

# So 10 / 2 prints 5.0, not 5. That is not a mistake.
print(10 / 2)                 # 5.0


# --- 5. A variable can change type -----------------------------------------
# Allowed, but usually a sign something has gone wrong in your thinking.

answer = 42
print(type(answer))           # <class 'int'>

answer = "forty two"
print(type(answer))           # <class 'str'>


# --- TRY IT ----------------------------------------------------------------
# 1. Print the type of:  "5"   5   5.0   "5.0"
# 2. Predict, then check:  "3" + "4"   and   3 + 4
# 3. Add the line  print("20" + 20)  - read the error, then fix it two ways.
