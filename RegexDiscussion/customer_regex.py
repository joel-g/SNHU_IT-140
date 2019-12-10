import csv
import re
data = []

with open('customerData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

ranges = ("Spent Past 30 Days", "Spent Past 12 Months", "Spent Past 6 Months")
for row in data:
    for range in ranges:
        row[range] = re.sub(r'[^\d.]', '', row[range])

with open('customerDataClean.csv', 'w', newline='') as csvfile:
    w = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
    w.writeheader()
    for row in data:
        w.writerow(row)
  
