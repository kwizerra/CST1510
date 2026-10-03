"""
INDENTATION
===========
Python uses indentation to mark a block. There are no { } to fall back on.
Run:  python 02_indentation.py
"""

# --- 1. The indented lines belong to the if ----------------------------

value = 23.7
limit = 20

if value > limit:
    print("checking...")     # indented - part of the if
    print("OVER")            # indented - also part of the if
print("done")                 # NOT indented - runs either way


# --- 2. Consistency, not amount ------------------------------------------
# 4 spaces is the standard. What matters is that every line in the SAME
# block is indented by the SAME amount. Most editors do this for you
# automatically after a colon.

if value > limit:
    print("line one")
    print("line two")


# --- 3. What goes wrong -----------------------------------------------------
# Uncomment each block below one at a time and run the file to see the error.

# if value > limit:
# print("OVER")
# IndentationError: expected an indented block after 'if' statement

# if value > limit:
#     print("OVER")
#      print("still over")
# IndentationError: unexpected indent


# --- 4. else and elif line up with if ----------------------------------
# The if, elif and else keywords themselves are NOT indented - only the
# lines inside each block are.

if value > limit:
    print("OVER")
elif value == limit:
    print("EXACT")
else:
    print("OK")


# --- TRY IT ------------------------------------------------------------------
# 1. Uncomment the two broken blocks in section 3, run the file, read the
#    error, then comment them out again.
# 2. Write an if / elif / else where every keyword lines up in the same column.
# 3. Deliberately indent one line by one extra space and see what happens.
