"""
WHILE LOOPS
===========
Repeat while a condition is True.   Run:  python 01_while_basics.py
"""

# --- 1. The basic shape ------------------------------------------------

count = 1

while count <= 3:
    print(count)
    count += 1     # <- without this line, count never changes and the
                    #    condition is True forever

print("done")


# --- 2. Same rule as if: indentation marks the block ------------------

total = 0
n = 1

while n <= 5:
    total += n
    n += 1

print(total)   # 15


# --- 3. while True + break ----------------------------------------------
# Loop until something inside the loop decides to stop, instead of
# counting in advance. This is the shape you use when you do not know how
# many times you will repeat.

while True:
    answer = input("Another? (y/n): ")
    if answer == "n":
        break
    print("okay, again")


# --- 4. THE INFINITE LOOP -----------------------------------------------
# Do not run this one. Read it and say why it never stops.
#
#     count = 1
#     while count <= 3:
#         print(count)
#     # count is never updated, so the condition is True forever
#
# If this happens to you: interrupt the kernel (Kernel -> Interrupt, or the
# stop button) rather than waiting. There is no error message to read -
# the program is just still running.


# --- TRY IT ------------------------------------------------------------------
# 1. Print the numbers 5 down to 1 using a while loop.
# 2. Before running it, say out loud what makes section 2's loop stop.
# 3. Write a while loop that keeps asking for a password until it equals
#    "python123".
