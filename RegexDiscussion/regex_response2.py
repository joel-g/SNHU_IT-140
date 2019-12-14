import csv
import re
data = []

with open('customerData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

men = []
women = []

for row in data:
    row["Spent Past 12 Months"] = re.sub(r'[^\d.]', '', row["Spent Past 12 Months"])
    if row["Gender"] == "male":
        men.append(row)
    elif row["Gender"] == "female":
        women.append(row)

def average_purchases(people):
    total = 0
    for person in people:
        total += float(person["Spent Past 12 Months"])
    return total / len(people)

men_average = average_purchases(men)
women_average = average_purchases(women)
percentage_men = len(men) / (len(men) + len(women)) * 100
percentage_women = len(women) / (len(men) + len(women)) * 100

print(format(percentage_men, ".2f") + "% of our customers are men and they spent on average $"+ format(men_average, ".2f") +" each in the past 12 months.")
print(format(percentage_women, ".2f") + "% of our customers are women and they spent on average $"+ format(women_average,".2f") +" each in the past 12 months.")

print(float("$1,234.00"))