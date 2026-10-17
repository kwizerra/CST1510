# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

with open("records.txt", "w") as f:
    f.write("Some text")
with open("records.txt") as f:
    print(f.read())
