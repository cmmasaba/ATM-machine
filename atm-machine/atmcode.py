import json
from datetime import datetime

with open('bankinfo.json') as f:
    data = json.load(f)

# for client in userdata['client_data']: print("Your name:\n", client['name'], "\nYour email:\n", client['email'],
# "\nYour account number:\n", client['accountNumber'], "\nYour account balance:\n", client['balance'])

useraccount = input("Please enter your ATM card number:\n")
userpin = input("Please enter your ATM card pin number:\n")

for client in data['bankData']['clientData']:
    while userpin == client['pin'] and useraccount == client['accountNumber']:
        print("BANK OF KENYA. YOUR HOME FOR INVESTMENT AND FINANCIAL SOLTUIONS.")
        print("Welcome to your account\n", client['name'], "\nWhich service would you like today")
        service = input("""
                    1. Withdraw money
                    2. Deposit money
                    3. Check account balance
                    4. Transfer money
                    5. Exit
                    """)
        if service == "1":
            w_choice = input("""Which currency do you want to withdraw?
                        1. Kshs
                        2. Usd
                        """)
            if w_choice == "1":
                balance = client['balance']['Kshs']
                w_amount = input('Enter amount to withdraw:\n')
                withdrawAmount = int(w_amount)
                Balance = int(balance)
                try:
                    if withdrawAmount > Balance:
                        raise Exception
                except Exception:
                    print(
                        "Please enter a lower amount. The amount you previously entered exceeds your account balance")
                else:
                    transactionRate = 0.07
                    transactionFee = transactionRate*withdrawAmount
                    newBalance = Balance - (withdrawAmount+transactionFee)
                    client['balance']['Kshs'] = str(newBalance)
                    newBalanceUsd = newBalance/114
                    client['balance']['Usd'] = str(newBalanceUsd)
                    loyalty = client['loyaltyPoints']
                    loyalty += 10
                    print("Successfully withdrew the money. Your account balance is:     ", client['balance'])
                    receipt = input("""Would you like a receipt?
                                1. Yes
                                2. No
                                """)
                    if receipt == "1":
                        today = datetime.today()
                        print("Transaction type:     Withdraw Money")
                        print("The date and time of transaction:        ", today)
                        print("Your account card number:     ", client['accountNumber'])
                        print("Transaction fee:     ", transactionFee)
                        print("The amount withdrew was:   Kshs  ", withdrawAmount)
                        print("Your account balance is:     ", client['balance'])
                        print('Your total promotional points are:       ', loyalty)
                        print("BANK OF KENYA. YOUR HOME FOR INVESTMENT AND FINANCIAL SOLTUIONS.\n")
                    else:
                        print("Thank you for being a valuable customer")
                        print("BANK OF KENYA. YOUR HOME FOR INVESTMENT AND FINANCIAL SOLTUIONS.")
            elif w_choice == "2":
                balance = client['balance']['Usd']
                w_amount = input('Enter amount to withdraw:\n')
                withdrawAmount = int(w_amount)
                Balance = int(balance)
                try:
                    if withdrawAmount > Balance:
                        raise Exception
                except Exception:
                    print(
                        "Please enter a lower amount. The amount you previously entered exceeds your account balance")
                else:
                    transactionRate = 0.07
                    transactionFee = transactionRate*withdrawAmount
                    newBalance = Balance - (withdrawAmount+transactionFee)
                    client['balance']['Usd'] = str(newBalance)
                    newBalanceShs = newBalance*114
                    client['balance']['Kshs'] = str(newBalanceShs)
                    loyalty = client['loyaltyPoints']
                    loyalty += 10
                    print("Successfully withdrew the money. Your account balance is:     ", client['balance'])
                    receipt = input("""Would you like a receipt?
                                1. Yes
                                2. No
                                """)
                    if receipt == "1":
                        today = datetime.today()
                        print("Transaction type:     Withdraw Money")
                        print("The date and time of transaction:        ", today)
                        print("Your account card number:     ", client['accountNumber'])
                        print("Transaction fee:     ", transactionFee)
                        print("The amount withdrew was:   Usd  ", withdrawAmount)
                        print("Your account balance is:     ", client['balance'])
                        print('Your total promotional points are:       ', loyalty)
                        print("BANK OF KENYA. YOUR HOME FOR INVESTMENT AND FINANCIAL SOLTUIONS.\n")
                    else:
                        print("Thank you for being a valuable customer")
                        print("BANK OF KENYA. YOUR HOME FOR INVESTMENT AND FINANCIAL SOLTUIONS.")
            else:
                print("Please pick a valid withdrawal option from above.\n")
        if service == "2":
            depositChoice = input("""Which currency would you like to deposit?
                             1. Kshs
                             2. Usd
                             """)
            if depositChoice == "1":
                balance = client['balance']['Kshs']
                Balance = int(balance)
                d_amount = input('Enter amount to deposit:\n')
                depositAmount = int(d_amount)
                try:
                    if depositAmount > 500000:
                        raise Exception
                except Exception:
                    print("""Failed to process your deposit. The maximum deposit amount allowed is 500,000 Kenyan Shillings.
                        Visit your nearest local bank to make larger deposits or try with a lower amount
                        """)
                else:
                    transactionRate = 0.00
                    transactionFee = transactionRate*depositAmount
                    newBalance = Balance + (depositAmount - transactionFee)
                    client['balance']['Kshs'] = str(newBalance)
                    newBalanceUsd = newBalance/114
                    client['balance']['Usd'] = str(newBalanceUsd)
                    loyalty = client['loyaltyPoints']
                    loyalty += 5
                    print("Successfully deposited the money. Your account balance is:     ", client['balance'])
                    receipt = input("""Would you like a receipt?
                                1. Yes
                                2. No
                                """)
                    if receipt == "1":
                        today = datetime.today()
                        print("Transaction type:     Deposit Money")
                        print("The date and time of transaction:        ", today)
                        print("Your account card number:     ", client['accountNumber'])
                        print("Transaction fee:     ", transactionFee)
                        print("The amount deposited was:   Kshs  ", depositAmount)
                        print("Your account balance is:     ", client['balance'])
                        print('Your total promotional points are:       ', loyalty)
                        print("BANK OF KENYA. YOUR HOME FOR INVESTMENT AND FINANCIAL SOLTUIONS.\n")
                    else:
                        print("Thank you for being a valuable customer")
                        print("BANK OF KENYA. YOUR HOME FOR INVESTMENT AND FINANCIAL SOLTUIONS.")
            if depositChoice == "2":
                balance = client['balance']['Usd']
                Balance = int(balance)
                d_amount = input('Enter amount to deposit:\n')
                depositAmount = int(d_amount)
                try:
                    if depositAmount > 4390:
                        raise Exception
                except Exception:
                    print("""Failed to process your deposit. The maximum deposit amount allowed is 4,390 US dollars.
                        Visit your nearest local bank to make larger deposits or try with a lower amount
                        """)
                else:
                    transactionRate = 0.00
                    transactionFee = transactionRate*depositAmount
                    newBalance = Balance + (depositAmount - transactionFee)
                    client['balance']['Usd'] = str(newBalance)
                    newBalanceKshs = newBalance*114
                    client['balance']['Kshs'] = str(newBalanceKshs)
                    loyalty = client['loyaltyPoints']
                    loyalty += 5
                    print("Successfully deposited the money. Your account balance is:     ", client['balance'])
                    receipt = input("""Would you like a receipt?
                                1. Yes
                                2. No
                                """)
                    if receipt == "1":
                        today = datetime.today()
                        print("Transaction type:     Deposit Money")
                        print("The date and time of transaction:        ", today)
                        print("Your account card number:     ", client['accountNumber'])
                        print("Transaction fee:     ", transactionFee)
                        print("The amount deposited was:   Usd  ", depositAmount)
                        print("Your account balance is:     ", client['balance'])
                        print('Your total promotional points are:       ', loyalty)
                        print("BANK OF KENYA. YOUR HOME FOR INVESTMENT AND FINANCIAL SOLTUIONS.\n")
                    else:
                        print("Thank you for being a valuable customer")
                        print("BANK OF KENYA. YOUR HOME FOR INVESTMENT AND FINANCIAL SOLTUIONS.")

            else:
                print("Please pick a valid deposit option from above.\n")
        elif service == "3":
            today = datetime.today()
            print("Your account balance is:     ", client['balance'])
            print("The date and time of transaction:        ", today)
