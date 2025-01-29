# Still need to add balance to option 1 and format better / loop better
# Add a no reason provided to skip reason
# Add a try/except to numbers not 1-4
# Make see transaction aligned
# EX: DEPOSIT: 200.0 | REASON:  Paycheck
# DEPOSIT: 50.0 | REASON:
# PURCHASE: 2892.0 | REASON:  Fuck it

transaction_dict = {}


# Menu function
def menu():
  print("-----------------------------------------")
  print("1. See recent transactions")
  print("2. Enter a deposit")
  print("3. Enter a purchase")
  print("4. Close the app")
  choice = input("Please select an option (1-4): ")
  return choice


def recent_transactions():
  print("Here are your recent transactions:")
  print('----------------------------------')
  for key, value in transaction_dict.items():
    print(key, value)


def deposit(account, account_balance):
  deposit_amount = input(("How much would you like to deposit?: "))
  try:
    deposit_amount = float(deposit_amount)
    print(f"You've selected to deposit ${deposit_amount:.2f}.")
  except ValueError:
    print("Please enter a number.")
    return account_balance

  reason = input(("What is the reason for this deposit? (Enter to skip): "))
  print(
      f"{deposit_amount} has been succesfully deposited to your {account} account."
  )
  account_balance += deposit_amount
  print(f"New Account Balance: {account_balance:.2f}")

  transaction_dict[f"DEPOSIT: {deposit_amount} | REASON: "] = reason

  return account_balance


def purchase(account, account_balance):
  purchase_amount = input(("Please enter the purchase amount: "))
  try:
    purchase_amount = float(purchase_amount)
    print(f"You've entered a ${purchase_amount:.2f} purchase.")
  except ValueError:
    print("Please enter a number.")
    return account_balance

  reason = input(("What is the reason for this purchase? (Enter to skip): "))
  print(
      f"Your ${purchase_amount} purchase has been succesfully entered to your {account} account."
  )
  account_balance -= purchase_amount
  print(f"New Account Balance: {account_balance:.2f}")

  transaction_dict[f"PURCHASE: {purchase_amount} | REASON: "] = reason

  return account_balance


def close_app(name):
  print(f"Thank you for using the budget tracker today {name}!")


def select_option(choice, account, account_balance, name):
  if choice == "1":
    recent_transactions()
  elif choice == "2":
    account_balance = deposit(account, account_balance)
  elif choice == "3":
    account_balance = purchase(account, account_balance)
  if choice == "4":
    close_app(name)

  return account_balance


# Main app function
def main():

  global transaction_dict
  account_balance = 1000

  print("Welcome to your Budget Tracker!")
  name = input(("What is your name?: "))
  account = input(("What is your bank name?:"))
  print("")

  print(f"Hi {name}, here are your options today!")

  while True:
    choice = menu()
    account_balance = select_option(choice, account, account_balance, name)
    if choice == "4":
      break


if __name__ == "__main__":
  main()
