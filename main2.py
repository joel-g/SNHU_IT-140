import sys
'''
Section 1: Collect customer input
'''
#Add customer input 1 here, rentalCode = ? 

valid_rental_code_received = False
while valid_rental_code_received == False:
    rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")
    for code in ["B", "D", "W"]: #makes sure input is valid, if not loops back to ask again
        if rentalCode == code:
            valid_rental_code_received = True

print(rentalCode)

## This is needed but isn't explicitly asked for in the assignement. Oversight?

if rentalCode == "W":
  rentalPeriod = int(input("Number of Weeks Rented:\n")) / 7
else:
  rentalPeriod = int(input("Number of Days Rented:\n"))


#Collect Customer Data - Part 2

#4)Collect Mileage information:
#a)	Prompt the user to input the starting odometer reading and store it as the variable odoStart

#Prompt -->"Starting Odometer Reading:\n"
# odoStart = ?
odoStart = input("Starting Odometer Reading:\n")

#b)	Prompt the user to input the ending odometer reading and store it as the variable odoEnd

#Prompt -->"Ending Odometer Reading:"
# odoEnd = ?

odoEnd = input("Ending Odometer Reading:\n")

#c) Calculate total miles
totalMiles = int(odoEnd) - int(odoStart)

#Print odoStart, odoEnd and totalMiles
print(odoStart, odoEnd, totalMiles)

# Calculate Charges 2

##	Calculate the mileage charge and store it as 
#   the variable mileCharge:

#a)	Code 'B' (budget) mileage charge: $0.25 for each mile driven

if rentalCode == "B":
  mileCharge = totalMiles * 0.25
  

#b)	Code 'D' (daily) mileage charge: no charge if the average
#   number of miles driven per day is 100 miles or less;
#   i)	Calculate the averageDayMiles (totalMiles/rentalPeriod)

averageDayMiles = totalMiles / rentalPeriod

#   ii)	If averageDayMiles is above the 100 mile per day
#       limit:
#     (1)	calculate extraMiles (averageDayMiles  - 100)
#     (2)	mileCharge is the charge for extraMiles, 
#         $0.25 for each mile

if averageDayMiles > 100:
  mileCharge = 0.25 * (averageDayMiles-100) * rentalPeriod
else:
  mileCharge = 0

#c)	Code 'W' (weekly) mileage charge: no charge if the 
#   average number of miles driven per week is 
#   900 miles or less;
 
#   i)	Calculate the averageWeekMiles (totalMiles/ rentalPeriod)

#   ii)	mileCharge is $100.00 per week if the average number of miles driven per week exceeds 900 miles


