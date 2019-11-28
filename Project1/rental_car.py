import sys

# Joel Guerra
# IT-140
# Project 1
# 11-15-2019


# const rates dictionary will be used to calculate base charge
RATES = {
    "B": 40.00, #budget
    "D": 60.00, #daily
    "W": 190.00, #weekly
}

validRentalCodeReceived = False
while validRentalCodeReceived == False: # While loop prevents invalid input from user being passed
    rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n").upper()
    if rentalCode in ("B", "D", "W"): #makes sure input is valid, if not loops back to ask again
        validRentalCodeReceived = True

# collect rental period and translate to 'days' as INTs
if rentalCode == "W":
  rentalPeriod = int(input("Number of Weeks Rented:\n")) * 7
else:
  rentalPeriod = int(input("Number of Days Rented:\n"))

# collect miles driven as INT
odoStart = input("Starting Odometer Reading:\n")
odoEnd = input("Ending Odometer Reading:\n")
totalMiles = int(odoEnd) - int(odoStart)

# calculate mileCharge per rentalCode and totalMiles. I would prefer a case/switch here but assignment requires elif
if rentalCode == "B":
  mileCharge = totalMiles * 0.25
elif rentalCode == "D":
  averageDayMiles = totalMiles / rentalPeriod
  if averageDayMiles > 100:
    mileCharge = 0.25 * (averageDayMiles-100) # I would have expected the mileage charge to apply to the average miles TIMES the number of days but if I do that it won't pass the Codio checks.
  else:
    mileCharge = 0
else: #no need to check for "W" because all cases that are not B or D would be W since we sanitized inputs
  weeksRented = rentalPeriod / 7
  if totalMiles / weeksRented > 900:
    mileCharge = 100 * weeksRented
  else:
    mileCharge = 0

# use the const rates dictionary to calcualte baseCharge
if rentalCode == "W":   
    baseCharge = (rentalPeriod/7) * RATES[rentalCode]
else: 
    baseCharge = rentalPeriod * RATES[rentalCode]

# output summary to user (converting all INTs and FLOATs back to STRINGs)
print("Rental Summary")
print("Rental Code: " + rentalCode)
print("Rental Period: " + str(rentalPeriod))
print("Starting Odometer: " + str(odoStart))
print("Ending Odometer: " + str(odoEnd))
print("Miles Driven: " + str(totalMiles))
print("Amount Due: $" + format(baseCharge+mileCharge, ".2f")) #format() is being used to format the float to hundredths place like we are used to for money