# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value    # stored as "amount", not "value"
        self.limit = limit

r = Record("R-001", 87.0, 100.0)
print(r.value)
