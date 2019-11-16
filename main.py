import sys
'''
Section 1: Collect customer input
'''

##Collect Customer Data - Part 1
RATES = {
    "budget": 40.00,
    "daily": 60.00,
    "weekly": 190,
}
#1)	Request Rental code:
#Prompt --> "(B)udget, (D)aily, or (W)eekly rental?"
#rentalCode = ?

valid_rental_code_received = False
while valid_rental_code_received == False:
    rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")
    for code in ["B", "D", "W"]: #makes sure input is valid, if not loops back to ask again
        if rentalCode == code:
            valid_rental_code_received = True


#2)	Request time period the car was rented.
#Prompt --> "Number of Days Rented:"
#rentalPeriod = ?
#	OR
#Prompt --> "Number of Weeks Rented:"
#rentalPeriod = ?

if rentalCode == "W":
  rentalPeriod = input("Number of Weeks Rented:\n")
else:
  rentalPeriod = input("Number of Days Rented:\n")
  
print(rentalCode)
print(rentalPeriod)


#CUSTOMER DATA CHECK 1
#ADD CODE HERE TO PRINT:
#rentalCode
#rentalPeriod


#Calculation Part 1

##Set the base charge for the rental type as the variable baseCharge. 
#The base charge is the rental period * the appropriate rate: