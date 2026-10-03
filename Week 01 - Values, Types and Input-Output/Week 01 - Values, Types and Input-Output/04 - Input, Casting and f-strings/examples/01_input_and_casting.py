"""
INPUT AND CASTING
=================
Asking the user for something, and converting what you get back.
Run:  python 01_input_and_casting.py
"""

# --- 1. input() asks the person running the program ------------------------
# Whatever is in the brackets is shown as the prompt.

record_id = input("Record ID : ")
print("You entered:", record_id)


# --- 2. THE RULE THAT CATCHES EVERYONE -------------------------------------
#
#     input() ALWAYS gives you text. Always. Even when they type a number.
#
# Type 23.7 when this runs, then look at the type.

value_text = input("Value     : ")

print("You typed :", value_text)
print("Its type  :", type(value_text))     # <class 'str'>   - text!

# WATCH OUT: this is why  value_text + 1  is a TypeError. Python genuinely
# received the characters 2, 3, . and 7 - not the number twenty-three point seven.


# --- 3. Casting - converting a type ----------------------------------------
#     int()    -> whole number
#     float()  -> decimal number
#     str()    -> text

text = "20"
print(int(text), type(int(text)))          # 20 <class 'int'>
print(float(text), type(float(text)))      # 20.0 <class 'float'>
print(str(20), type(str(20)))              # 20 <class 'str'>

# WATCH OUT: int() cannot cope with a decimal point in text.
#     int("23.7")     ValueError: invalid literal for int()
# Use float() unless you are certain the number is whole.


# --- 4. The form you will actually write -----------------------------------
# Do the conversion in the same line as the input.
# Read it INSIDE OUT:  ask -> get text -> convert -> store.

value = float(input("Value again : "))

print(value + 1)              # works, because value is now a number
print(type(value))            # <class 'float'>


# --- 5. Which one to use ---------------------------------------------------
#   a name, an ID, a hostname, an IP   -> leave it as text, no conversion
#   anything you will calculate with   -> float(), almost always
#   a count of whole things            -> int() is fine


# --- TRY IT ----------------------------------------------------------------
# 1. Ask for GB used and GB total, convert both, print how many GB are free.
# 2. Change one float() to int() and enter 87.5. Read the error.
# 3. What happens if you just press Enter without typing anything?
