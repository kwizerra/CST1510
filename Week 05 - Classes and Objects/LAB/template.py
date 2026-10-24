"""
RECORD CHECK  -  my version
===========================

Name  :  Shaun Michael Tamale
Lane  :  AI     (delete two)
Date  :  24/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.

class Record:
    #Counter is shared by every record and not tied to any singuar object
    over_limit_count = 0
    def __init__(self, dataset_name, rows_loaded, rows_expected):
        """Stores the dataset name and its rows loaded/expected """
        self.dataset_name = dataset_name
        self.rows_loaded = rows_loaded
        self.rows_expected = rows_expected
    def status(self):
        """Returns OVER LIMIT, WARNING or OK based on percent"""
        # rows loaded expressed as a percentage of rows expected
        percent = (self.rows_loaded/self.rows_expected) * 100
        if percent >= 100:
            #update the counter when a record is over limit
            Record.over_limit_count += 1
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"    
                                               

# ==================================================================== RECORDS
# 2. Create your records.

def load_records(path):
    """Reads dataset name and rows loaded/expected from a file and returns them in a list."""
    records = []
    with open(path) as f:
        for line in f:
            #Remove the new line and split itinto 3 parts
            dataset_name, rows_loaded, rows_expected = line.strip().split(",")
            # Numbers returned as strings so converted to floats 
            record = Record(dataset_name, float(rows_loaded), float(rows_expected)) 
            records.append(record)
    return records

records = load_records("datasets.txt")

# ==================================================================== OUTPUT
# Bordered report printed per record
for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.dataset_name}")
    print("=" * 34)
    print(f'{' Dataset':<18}: {record.dataset_name:>12}')
    print(f'{' Rows Loaded':<18}: {record.rows_loaded:>12.2f}')
    print(f'{' Rows Expected':<18}: {record.rows_expected:>12.2f}')
    print(f'{' Status':<18}: {record.status():>12}')
    print("=" * 34)
#Over limit total printed once after the loop has finished
print()
print(f"{Record.over_limit_count} records were OVER LIMIT")
print()
# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
