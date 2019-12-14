import csv
import re
data = []

with open('customerData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

for row in data:
    row["Spent Past 30 Days"] = re.sub(r'[^\d.]', '', row["Spent Past 30 Days"])
    if float(row["Spent Past 30 Days"]) > 0:
        print(row["Name"], row["Email"])    