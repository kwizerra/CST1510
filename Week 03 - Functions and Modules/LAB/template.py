"""
RECORD CHECK  -  my version
===========================

Name  : Shaun Michael Tamale
Lane  :  Cyber     (delete two)
Date  : 10/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.

#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.
#    Give each function a one-line docstring saying what it does.

# your function(s) go here
def status_of(percent):
    """ This returns the status of percent"""
    if percent >= 100:
        return 'OVER LIMIT'
    elif percent >= 90:
        return 'WARNING'
    else:
        return 'OK'
def check(failed_logins, total_attempts):
    """ This calculated the available login attempts remaining and percent """
    available_logins = total_attempts - failed_logins
    percent = (failed_logins/total_attempts) * 100
    return available_logins, percent
def print_report(source_ip, failed_logins, total_attempts, available_logins, percent, status):
    """ This prints the report """
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {source_ip}")
    print("=" * 34)
    print(f'{' Source IP':<18}: {source_ip:>12}')
    print(f'{' Failed logins':<18}: {failed_logins:>12.2f}')
    print(f'{' Total attempts':<18}: {total_attempts:>12.2f}')
    print(f'{' Available logins':<18}: {available_logins:>+12.2f}')
    print(f'{' Percent':<18}: {percent:>12.2f} %')
    print(f'{' Status':<18}: {status:>12}')
    print("=" * 34)




# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
overlimit = 0
while True:
  source_ip = input('Source IP : ')
  if source_ip == 'quit':
      break
  failed_logins = float(input('Failed logins : '))
  total_attempts = float(input('Total Attempts : '))
 


# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
#
#    Threshold : call status_of() to get the status. Work out the
#                difference and percentage inline, not in a function.
#    Typical   : call check() to get the difference and percentage instead.

  available_logins, percent = check(failed_logins, total_attempts)  # replace with your code

  status = status_of(percent)
  if status == 'OVER LIMIT':
      overlimit += 1


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : call print_report() instead of printing directly here, and
#                wrap sections 2-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

  

  print_report(source_ip, failed_logins, total_attempts, available_logins, percent, status)
print(f'Over limit is {overlimit}')


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
