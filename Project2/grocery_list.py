# Joel Guerra
# IT-140
# Project 2 Final
# 12-3-2019

grocery_history = []
stop = 'go' #will become Q or C as user quits or continues

while stop != 'q': #loop until user presses Q
  # collect attributes of grocery item and put it in a dict
  grocery_item = {}
  grocery_item['name'] = input("Item name:\n")
  # If the user enteres letters or other symbols and causes a type conversion error then this TRY/EXCEPT block will warn the user and start a new loop
  try:
    grocery_item['number'] = int(input("Quantity purchased:\n"))
  except:
    print("Quantity must be a number! Try again.")
    continue
  try:
    grocery_item['price'] = float(input("Price per item:\n"))
  except:
    print("Price must be a number! Try again.")
    continue
  # append the dict to the list
  grocery_history.append(grocery_item)
  # find out if the user is done
  stop = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")
    
def print_and_sum_item(item): # this function will print out the line summary for an item passed in as an argument and return the total for that item
  print(str(item['number']) + " " + item['name'] + " @ $" + str(item['price'])+ " ea $"+format(item['price']*item['number'], ".2f"))
  return item['number'] * item['price']

grand_total = 0  

for item in grocery_history:
  grand_total += print_and_sum_item(item)
  # call the function to print out the item and add its return to the grand total

print("Grand total: $"+format(grand_total, ".2f")) #formats the string to 2 decimals 