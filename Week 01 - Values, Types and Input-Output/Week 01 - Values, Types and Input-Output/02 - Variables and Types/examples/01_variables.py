"""
VARIABLES
=========
Storing a value so you can use it again.   Run:  python 01_variables.py
"""

# --- 1. A variable is a name for a value -----------------------------------
# Read = as "gets", not "equals".  value = 23.7  means "put 23.7 into value".

record_id = "R-004"
value = 23.7
limit = 20

print(record_id)                          # R-004
print(record_id, "has value", value)      # R-004 has value 23.7

# The name goes on the LEFT.  23.7 = value  is a SyntaxError.


# --- 2. Names should say what the value is ---------------------------------
# Both of these work. Only one is readable in three weeks' time.

v = 23.7
l = 20
print(v - l)                              # 3.7 - but what are v and l?

sensor_value = 23.7
sensor_limit = 20
print(sensor_value - sensor_limit)        # 3.7 - obvious


# --- 3. Naming rules -------------------------------------------------------
#   lowercase, words joined by underscores      sensor_value
#   no spaces                                   my value   -> SyntaxError
#   cannot start with a digit                   2nd_value  -> SyntaxError
#   cannot be a Python word                     print, if, class, for
#
# WATCH OUT: using a name you never assigned gives a NameError. Nine times
# out of ten it is a typo or a capital letter in the wrong place.


# --- 4. A variable can be given a new value --------------------------------
# The old value is gone. Nothing remembers it.

checks_done = 0
print(checks_done)                        # 0

checks_done = 1
print(checks_done)                        # 1


# --- 5. Order matters ------------------------------------------------------
# Each line finishes completely before the next one starts.

a = 5
b = 10
a = b        # a gets whatever b holds RIGHT NOW, which is 10
b = 3        # changing b now does not change a

print(a, b)                               # 10 3


# --- 6. Same idea, three fields ---------------------------------------------
# A variable holds one fact about one thing.

reading, units = 23.7, "celsius"                  # AI / Data Science
source_ip, port = "10.0.0.5", 443                 # Cyber Security
hostname, disk_used = "srv-01", 87                # IT

print(reading, units)
print(source_ip, port)
print(hostname, disk_used)


# --- TRY IT ----------------------------------------------------------------
# 1. Store your name and course in two well-named variables, print both.
# 2. Rewrite this with good names:   x = "srv-01" ; y = 87 ; print(x, y)
# 3. Before running: what does  p = 1 ; q = p ; p = 9 ; print(p, q)  give?
