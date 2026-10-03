"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :   IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
overlimit = 0
while True:
    hostname = input('Hostname :')      # replace with an input() call
    if hostname == 'quit':
           print (f'Over limit number : {overlimit}')
           break
    gb_used = float(input('Used GB :'))     # replace with an input() call, converted with float()
    gb_total = float(input('Total GB :'))     # replace with an input() call, converted with float()


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

    free_gb = gb_total - gb_used  # replace with your calculation
    percent = (gb_used/gb_total) * 100       # replace with your calculation
# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"

    if percent >= 100:
      status = 'OVER LIMIT'
    elif percent >= 90:
       status = 'WARNING'
    else:
      status = 'OK'  # replace with your if / else (or if / elif / else)


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {hostname}")
    print("=" * 34)
    print(f'{'  Used GB':<12}: {gb_used:>12.2f}')
    print(f'{'  Total GB':<12}: {gb_total:>12.2f}')
    print(f'{'  Free GB':<12}: {free_gb:>+12.2f}')
    print(f'{'  Percent':<12}: {percent:>12.2f} %')
    print(f'{'  Status':<12}: {status:>12}')


    print("=" * 34)
    if status == 'OVER LIMIT':
       overlimit += 1


       




# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
