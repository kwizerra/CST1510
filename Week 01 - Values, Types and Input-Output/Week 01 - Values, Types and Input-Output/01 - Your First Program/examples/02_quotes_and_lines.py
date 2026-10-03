"""
QUOTES AND LAYOUT
=================
Making text, and controlling how it sits on the screen.
Run:  python 02_quotes_and_lines.py
"""

# --- 1. Both quote marks make a string -------------------------------------
# There is no difference. Pick one. This module uses double quotes.

print('single quotes')
print("double quotes")
print("hello" == 'hello')      # True - genuinely the same thing


# --- 2. Quotes inside your text --------------------------------------------
# Use the OTHER kind of quote to wrap it. Easiest fix, reach for this first.

print("the log said 'connection refused'")
print("it's over the limit")               # apostrophe inside double quotes

# WATCH OUT: 'it's over' is a SyntaxError - the apostrophe ends the string
# early. This is the most common Week 1 syntax error. Use double quotes.


# --- 3. When you need both kinds -------------------------------------------
# Put a backslash in front of the one you want kept as text ("escaping").

print("she said \"it's fine\"")     # she said "it's fine"


# --- 4. New lines and tabs -------------------------------------------------
# \n means "new line". \t means "tab". Each counts as ONE character.

print("line one\nline two")
# Output:  line one
#          line two

print("ID\tVALUE")
print("R-004\t23.7")
# Output:  ID      VALUE
#          R-004   23.7

# Tabs only line up when entries are similar lengths. For real reports use
# f-string alignment (Topic 4). Tabs are fine for rough working.

print("C:\\Users\\student")        # \\ prints one real backslash


# --- 5. Text over several lines --------------------------------------------
print("""RECORD CHECK
Value : 23.7""")

# Triple quotes at the top of a file are called a docstring - see line 1.


# --- 6. Repeating a string -------------------------------------------------
# The tidy way to draw a separator. Never type thirty equals signs.

print("=" * 30)
print("ab" * 3)                    # ababab

# WATCH OUT: this is repetition, not multiplication.
print("5" * 3)                     # 555   (text repeated)
print(5 * 3)                       # 15    (numbers multiplied)


# --- 7. Putting it together ------------------------------------------------
print()
print("=" * 30)
print("\tRECORD CHECK")
print("=" * 30)


# --- TRY IT ----------------------------------------------------------------
# 1. Print:  The alert said "disk full" on server 'srv-01'
# 2. Print a line of 50 dashes without typing 50 dashes.
# 3. Predict what "7" * 3 and 7 * 3 print. Then check.
