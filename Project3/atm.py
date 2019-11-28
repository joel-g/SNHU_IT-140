import sys
 
account_balance = float(500.25) # balance will be mutated throughout the script

userchoice = input ("What would you like to do?\n")

# business logic here. if statements navigate user input and call appropriate functions to calculate balance 
if (userchoice == 'D'):
  deposit_amount = float(input('How much would you like to deposit today?\n'))
  account_balance = deposit(account_balance, deposit_amount)
elif userchoice == 'B':
  printbalance(account_balance)
elif userchoice == 'W':
  withdrawal_amount = float(input('How much would you like to withdraw today?\n'))
  account_balance = withdraw(account_balance, withdrawal_amount)
elif userchoice == 'Q':
  print('Thank you for banking with us.')

  #printbalance prints balance, has no return 
def printbalance(bal):
  print('Your current balance:')
  print(bal)

#deposit function, calculates balance, outputs message to user and returns new balance
def deposit(bal, dep):
  bal += dep
  print("Deposit was $"+format(dep, '.2f') + ", current balance is $" + format(bal, '.2f'))
  return bal
  
#withdraw function, calculates balance, outputs message to user and returns new balance
def withdraw(bal, wit):
  if bal >= wit:
    bal -= wit
    print("Withdrawal amount was $"+format(wit, '.2f') + ", current balance is $" + str(bal))
  else:
    print('$'+format(withdrawal_amount, '.2f')+ ' is greater than your account balance of $' +format(account_balance, '.2f'))
  return bal