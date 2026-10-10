"""
RECORD CHECK  -  my version
===========================

Name  :  Shaun Michael Tamale
Lane  :  AI     (delete two)
Date  :  3/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#
#    Remember: input() always gives back text.

dataset_name = input('Dataset name : ')    # : replace with an input() call
rows_loaded = float(input('Rows loaded : '))   # : replace with an input() call, converted
rows_expected  = float(input('Rows expected : '))    # : replace with an input() call, converted


# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
#    - percent    : the first as a percentage of the second
#
#    Do not type the answers. Calculate them.

free_rows = rows_expected - rows_loaded   # 
percent = (rows_expected/rows_loaded)  * 100  # 
data_loss_rate = (free_rows/rows_loaded) * 100 #This shows a percentage of expected data that was not found.

# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

print()
print("=" * 34)
print(f"  RECORD CHECK   -  {dataset_name}")
print("=" * 34)

print(f'  {'Rows loaded':<15}: {rows_loaded:>10.2f}')
print(f'  {'Rows expected':<15}: {rows_expected:>10.2f}')
print(f'  {'Free rows':<15}: {free_rows:>+10.2f}')
print(f'  {'Percent':<15}: {percent:>10.2f} %')
print(f'  {'Data loss rate':<15}: {data_loss_rate:>10.2f} %')
print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
