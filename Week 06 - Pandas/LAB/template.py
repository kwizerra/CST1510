"""
RECORD CHECK  -  my version
===========================

Name  : Shaun Michael Tamale
Lane  :  Cyber
Date  : 31/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
import matplotlib.pyplot as plt
# ==================================================================== LOAD

#load data from external csv file
df = pd.read_csv("cyber_records.csv")


# ================================================================= PROCESS

# adding percent and rounding off to 2 decimals
df["percent"] = ((df["failed_logins"]/df["total_attempts"]) * 100).round(2)
#Label each record: 100%+ = OVER LIMIT, 90%+ = WARNING, below 90% = OK 
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 
    else "WARNING" if p >= 90 
    else "OK")

# ================================================================== OUTPUT
# 3. Print the DataFrame.

#print df
print(df)
not_ok = df[df["status"] != "OK"]
#print rows that are not "OK"
print(not_ok)
status_count = df.groupby("status").size()
#print status_count
print(status_count)
#save full DataFrame to a new csv file
df.to_csv("cyber_output.csv", index=False)
status_count.plot(kind="bar")
plt.title("Records per status")
plt.tight_layout()#adjust spacing so labels and titles dont get cut off in the image
plt.savefig("status.png")#save bar chart of counts per status



# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
