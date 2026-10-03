"""
PRINT BASICS
============
Getting your program to say something.   Run:  python 01_print_basics.py
"""

# --- 1. A program runs top to bottom ---------------------------------------
# Nothing clever. The order you write things is the order they happen.

print("Record check starting")
print("Done")
# Output:  Record check starting
#          Done


# --- 2. Python is case sensitive -------------------------------------------
# print works. Print and PRINT do not exist. This applies to everything.
# The brackets are not optional either:  print "hi"  is a SyntaxError.


# --- 3. Printing several values --------------------------------------------
# Commas let you print more than one thing. Each comma adds ONE space.

print("Record", "R-004", "checked")     # Record R-004 checked
print("Checked", 3, "records")          # Checked 3 records
print()                                 # a blank line


# --- 4. Changing the spacing: sep= and end= --------------------------------
print("2026", "09", "14", sep="-")      # 2026-09-14
print("a", "b", sep="")                 # ab

print("Loading", end="")
print("... done")                       # Loading... done   (one line)


# --- 5. Joining with + -----------------------------------------------------
# + glues strings together, but adds NO space and breaks on numbers.

print("Record" + "R-004")               # RecordR-004   <- no space
print("Record" + " " + "R-004")         # Record R-004

# WATCH OUT:  "Value: " + 23.7  is a TypeError. + needs two strings.


# --- 6. The one you should actually use: f-strings -------------------------
# Preview - Topic 4 covers it fully. Put f before the quotes, values in { }.

record_id = "R-004"
value = 23.7

print(f"Record {record_id} has value {value}")   # Record R-004 has value 23.7
print(f"Double that is {value * 2}")             # Double that is 47.4

# Rule for this module: if a human reads the output, use an f-string.


# --- 7. Comments -----------------------------------------------------------
# Anything after # is ignored. Good comments say WHY, not WHAT.

print("visible")    # this bit is ignored


# --- 8. Same idea, three fields ---------------------------------------------
# print() is how a program reports what it found. Different job, same tool.

print("Rows loaded: 1200")                            # AI / Data Science
print("[ALERT] failed login from 10.0.0.5")           # Cyber Security
print("Backup complete - 4 of 4 servers")             # IT


# --- TRY IT ----------------------------------------------------------------
# 1. Print your name and age using commas, then again using an f-string.
# 2. Print today's date as 14/09/2026 using sep="/".
# 3. Add the line  print("Value: " + 23.7)  - read the error, then fix it.
