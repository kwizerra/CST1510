"""
RECORD CHECK  -  my version
===========================

Name  :Shaun Michael Tamale
Lane  :IT
Date  :16/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS

def check_record(gb_used, gb_total):
    """ This calculates the available GB remaining and percent used and its status. """
    gb_available = gb_total- gb_used
    percent = (gb_used/gb_total) * 100
    if percent >= 100:
            status = 'OVER LIMIT'
    elif percent >= 90:
            status = 'WARNING'
    else:
            status = 'OK'
    return gb_available , percent, status
def print_report(hostname, gb_used, gb_total, gb_available, percent, status):
    """ Prints a formatted report per server """
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {hostname}")
    print("=" * 34)
    print(f'{' Hostname':<18}: {hostname:>12}')
    print(f'{' Used GB':<18}: {gb_used:>12.2f}')
    print(f'{' Total GB':<18}: {gb_total:>12.2f}')
    print(f'{' Available GB':<18}: {gb_available:>+12.2f}')
    print(f'{' Percent':<18}: {percent:>12.2f} %')
    print(f'{' Status':<18}: {status:>12}')
    print("=" * 34)


# ====================================================================== STORE

def load_records(path):
      """Reads hostnames, gbused and total from a file and returns a list of dicts."""
      records = []
      with open(path) as f:
            for line in f:
                  label, value, limit = line.strip().split(",")
                  records.append({"Hostname": label, "Used GB": float(value), "Total GB": float(limit)} )
      return records
#load the file but if it's missing, carry on with an empty list
try:
      records =load_records("servers.txt")
except FileNotFoundError:
      print("Sorry File not found.")
      records = []  

# =============================================================== PROCESS + OUTPUT

counter = 0
server_status = []
# check eah server, print its report, count OVER LIMITs keeps (hostname, status) paris.
for record in records:
      gb_available, percent, status = check_record(record["Used GB"],record["Total GB"])
      print_report(record["Hostname"], record["Used GB"], record["Total GB"], gb_available, percent, status)
      if status == "OVER LIMIT":
            counter += 1
      server_status.append((record["Hostname"], status))
# write one hostname, status line per server
with open("server_status.txt", "w") as f:
      for hostname, status in server_status:
            f.write(f"{hostname},{status}\n")
print(f"The number of OVERLIMITS were {counter}")#count is printed once after the loop
# ==========================================================================
# 4. Before you finish:
