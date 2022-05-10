"""These are modules needed by the application"""
import json
import logging
from datetime import datetime

"""customizing logging parameters to be used for logging purposes"""
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('atm.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

"""all client information is stored in the bankinfo.json file"""
with open('bankinfo.json') as f:
    data = json.load(f)

"""
defining all the exception error handlers that will be used
I use try and except blocks so that I can capture errors that may arise
and give back insightful messages
"""


class invalidTransfer(Exception):
    pass


class unregisteredUser(Exception):
    pass


class wrongCredentials(Exception):
    pass


class excessDeposit(Exception):
    pass


class insufficientBalance(Exception):
    pass


class maxTransfer(Exception):
    pass


atm_machine = True

loginAttempts = 0
while atm_machine:
    useraccount = int(input("Please enter your ATM account number:  \n"))
    """tried using getpass and pwinput to mask the client pins but it failed"""
    userpin = int(input("Please enter your ATM pin number:  \n"))

    loginSuccess = False
    """traversing the json file to check if the details provided by user match any records stored there"""
    for client in data['bankData']['clientData']:
        while userpin == client['pin'] and useraccount == client['accountNumber']:
            """if a match of user pin and account number is found the user is allowed in"""
            loginSuccess = True
            print("BANK OF KENYA. YOUR HOME FOR INVESTMENT AND FINANCIAL SOLUTIONS.\n")
            print("Welcome to your account", client['name'], "\nWhich service would you like today\n")
            """logs who signed into the system"""
            logger.info("Sign in by: " + str(client['name']) + " " + str(client['accountNumber']))
            service = input("""
                1. Withdraw money
                2. Deposit money
                3. Check account balance
                4. Transfer money
                5. Exit\n
                """)
            if service == "1":
                """logs which service was selected"""
                logger.info("Service picked: " + service)
                w_choice = input("""
                    Which currency do you want to withdraw?
                    1. Kshs
                    2. Usd\n
                    """)
                if w_choice == "1":
                    """logs the currency that was used for the transaction"""
                    logger.info("Currency picked for withdrawal: " + w_choice)
                    withdrawAmount = int(input('Enter amount to withdraw:  '))
                    try:
                        """ensures you can't withdraw more than is in your account"""
                        if withdrawAmount > client['balance']['Kshs']:
                            raise insufficientBalance
                    except insufficientBalance:
                        print("Insufficient balance. Please enter a lower amount.\n")
                        """logs the error message"""
                        logger.info("Insufficient balance.")
                    else:
                        """withdrawal executed if no problem is encountered"""
                        transactionRate = 0.07
                        transactionFee = transactionRate * withdrawAmount
                        client['balance']['Kshs'] -= withdrawAmount + transactionFee
                        client['balance']['Usd'] = client['balance']['Kshs'] / 114
                        loyalty = client['loyaltyPoints']
                        loyalty += 10
                        print("Withdrawal successful. Your account balance is %.2f: ", client['balance'])
                        """logs the successful withdrawal message"""
                        logger.info("Successful withdrawal. Account balance: " + str(client['balance']))
                        """a receipt can be generated if needed"""
                        receipt = input("""
                            Would you like a receipt?
                            1. Yes
                            2. No\n
                            """)
                        if receipt == "1":
                            today = datetime.today()
                            print("Transaction type:  Withdraw Money")
                            print("The date and time of transaction: ", today)
                            print("Your account card number: ", client['accountNumber'])
                            print("Transaction fee: ", transactionFee)
                            print("The amount withdrew was: Kshs ", withdrawAmount)
                            print("Your account balance is: ", client['balance'])
                            print('Your total promotional points are:  ', loyalty)
                            print("BANK OF KENYA. YOUR HOME FOR INVESTMENT AND FINANCIAL SOLUTIONS.\n")
                        else:
                            print("Thank you for being a valuable customer")
                            print("BANK OF KENYA. YOUR HOME FOR INVESTMENT AND FINANCIAL SOLUTIONS.\n")
                else:
                    """logs the currency that was used for the transaction"""
                    logger.info("Currency picked for withdrawal: " + w_choice)
                    withdrawAmount = int(input('Enter amount to withdraw:  '))
                    try:
                        """ensures you can't withdraw more than is in your account"""
                        if withdrawAmount > client['balance']['Usd']:
                            raise insufficientBalance
                    except insufficientBalance:
                        print("Insufficient balance. Please enter a lower amount.\n")
                        """logs the error message"""
                        logger.info("Insufficient balance.")
                    else:
                        """withdrawal executed if no problem is encountered"""
                        transactionRate = 0.07
                        transactionFee = transactionRate * withdrawAmount
                        client['balance']['Usd'] -= withdrawAmount + transactionFee
                        client['balance']['Kshs'] = client['balance']['Usd'] * 114
                        loyalty = client['loyaltyPoints']
                        loyalty += 10
                        print("Withdrawal successful. Your account balance is %.2f: ", client['balance'])
                        """logs the successful withdrawal message"""
                        logger.info("Successful withdrawal. Account balance: " + str(client['balance']))
                        """a receipt can be generated if needed"""
                        receipt = input("""
                            Would you like a receipt?
                            1. Yes
                            2. No\n
                            """)
                        if receipt == "1":
                            today = datetime.today()
                            print("Transaction type:  Withdraw Money")
                            print("The date and time of transaction: ", today)
                            print("Your account card number: ", client['accountNumber'])
                            print("Transaction fee: ", transactionFee)
                            print("The amount withdrew was: Usd ", withdrawAmount)
                            print("Your account balance is: ", client['balance'])
                            print("Your total promotional points are: ", loyalty)
                            print("BANK OF KENYA. YOUR HOME FOR INVESTMENT AND FINANCIAL SOLUTIONS.\n")
                        else:
                            print("Thank you for being a valuable customer")
                            print("BANK OF KENYA. YOUR HOME FOR INVESTMENT AND FINANCIAL SOLUTIONS.\n")
            elif service == "2":
                """logs which service was selected"""
                logger.info("Service: " + service)
                depositChoice = input("""
                    Which currency would you like to deposit?
                    1. Kshs
                    2. Usd\n
                    """)
                if depositChoice == "1":
                    """logs the currency that was used for the transaction"""
                    logger.info("Currency picked for deposit: " + depositChoice)
                    depositAmount = int(input("Enter amount to deposit:  "))
                    try:
                        """enforces a limit to the amount that can be deposited"""
                        if depositAmount > 500000:
                            raise excessDeposit
                    except excessDeposit:
                        print("Deposit limit is 500,000 Kenyan Shillings. Visit your nearest local bank or try with a "
                              "lower amount\n")
                        """logs the error message"""
                        logger.info("Deposit amount exceeds limit.")
                    else:
                        """deposit process to be executed if no errors are encountered"""
                        logger.info("Deposit amount: " + str(depositAmount))
                        transactionRate = 0.00
                        transactionFee = transactionRate * depositAmount
                        client['balance']['Kshs'] += depositAmount - transactionFee
                        client['balance']['Usd'] = client['balance']['Kshs'] / 114
                        loyalty = client['loyaltyPoints']
                        loyalty += 5
                        print("Successful deposit. Your account balance is %.2f:  ", client['balance'])
                        """logs the successful transaction message"""
                        logger.info("Deposit successful. Account balance:  " + str(client['balance']))
                        """a receipt can be generated if needed"""
                        receipt = input("""
                            Would you like a receipt?
                            1. Yes
                            2. No\n
                            """)
                        if receipt == "1":
                            today = datetime.today()
                            print("Transaction type:  Deposit Money")
                            print("The date and time of transaction:  ", today)
                            print("Your account card number:  ", client['accountNumber'])
                            print("Transaction fee:  ", transactionFee)
                            print("The amount deposited was: Kshs ", depositAmount)
                            print("Your account balance is:  ", client['balance'])
                            print("Your total promotional points are:  ", loyalty)
                            print("BANK OF KENYA. YOUR HOME FOR INVESTMENT AND FINANCIAL SOLUTIONS.\n")
                        else:
                            print("Thank you for being a valuable customer")
                            print("BANK OF KENYA. YOUR HOME FOR INVESTMENT AND FINANCIAL SOLUTIONS.\n")
                else:
                    """logs the currency that was used for the transaction"""
                    logger.info("Currency picked for deposit: " + depositChoice)
                    depositAmount = int(input('Enter amount to deposit: '))
                    try:
                        """enforces a limit to the amount that can be deposited"""
                        if depositAmount > 4390:
                            raise excessDeposit
                    except excessDeposit:
                        print("Deposit limit is 4390 US dollars. Visit your nearest local bank or try with a lower "
                              "amount\n")
                        """logs the error message"""
                        logger.info("Deposit amount exceeds limit.")
                    else:
                        """deposit process to be executed if no errors are encountered"""
                        logger.info("Deposit amount: " + str(depositAmount))
                        transactionRate = 0.00
                        transactionFee = transactionRate * depositAmount
                        client['balance']['Usd'] += depositAmount - transactionFee
                        client['balance']['Kshs'] = client['balance']['Usd'] * 114
                        loyalty = client['loyaltyPoints']
                        loyalty += 5
                        print("Successful deposit the money. Your account balance is %.2f: ", client['balance'])
                        """logs the successful transaction message"""
                        logger.info("Deposit successful. Account balance:  " + str(client['balance']))
                        """a receipt can be generated if needed"""
                        receipt = input("""
                            Would you like a receipt?
                            1. Yes
                            2. No\n
                            """)
                        if receipt == "1":
                            today = datetime.today()
                            print("Transaction type:  Deposit Money")
                            print("The date and time of transaction:  ", today)
                            print("Your account card number:  ", client['accountNumber'])
                            print("Transaction fee:  ", transactionFee)
                            print("The amount deposited was: Usd ", depositAmount)
                            print("Your account balance is:  ", client['balance'])
                            print("Your total promotional points are:  ", loyalty)
                            print("BANK OF KENYA. YOUR HOME FOR INVESTMENT AND FINANCIAL SOLUTIONS.\n")
                        else:
                            print("Thank you for being a valuable customer")
                            print("BANK OF KENYA. YOUR HOME FOR INVESTMENT AND FINANCIAL SOLUTIONS.\n")
            elif service == "3":
                """logs which service was selected"""
                logger.info("Service picked: " + service)
                today = datetime.today()
                """displays the client balance and date and time of transaction"""
                print("Your account balance is %.2f:  ", client['balance'])
                print("The date and time of transaction:  ", today)
                logger.info("Account balance: " + str(client['balance']))
            elif service == "4":
                """logs which service was selected"""
                logger.info("Service picked: " + service)
                successfulTransfer = False
                accountTransferNo = int(input("Enter the account number you want to transfer money to: "))
                """
                traverses the json file and tries to find a match for the account number given
                checks to ensure the client account number is not the recipient account number
                """
                for accountTransfer in data['bankData']['clientData']:
                    if accountTransferNo != client['accountNumber'] and accountTransferNo \
                            == accountTransfer['accountNumber']:
                        successfulTransfer = True
                        """logs who the recipient of the money transfer is"""
                        logger.info("Account to be transferred to: " + str(accountTransfer['accountNumber']))
                        transferChoice = input("""
                            Which currency would you like to transfer?
                            1. Kshs
                            2. Usd\n
                            """)
                        if transferChoice == "1":
                            """logs the currency that was used for the transaction"""
                            logger.info("Currency picked for transfer: " + transferChoice)
                            transactionRate = 0.03
                            loyalty = client['loyaltyPoints']
                            loyalty += 7
                            transferAmount = int(input("Enter the amount you want to transfer:  "))
                            try:
                                """enforces a limit to the amount that can be transferred"""
                                if transferAmount > 500000:
                                    raise maxTransfer
                            except maxTransfer:
                                print("Maximum transfer is 500000 Kshs. Try a lower amount.")
                                """logs the error message"""
                                logger.info("Transfer amount exceeds limit.")
                            else:
                                """transfere process to be executed if not error is encountered"""
                                transactionFee = transactionRate * transferAmount
                                client['balance']['Kshs'] -= transferAmount + transactionFee
                                client['balance']['Usd'] = client['balance']['Kshs'] / 114
                                accountTransfer['balance']['Kshs'] += transferAmount
                                accountTransfer['balance']['Usd'] = accountTransfer['balance']['Kshs'] / 114
                                print("Successful transfer. Your account balance is %.2f: ", client['balance'])
                                """logs the successful transaction message"""
                                logger.info("Transfer successful. Account balance : " + str(client['balance']))
                                """a receipt can be generated if needed"""
                                receipt = input("""
                                    Would you like a receipt?
                                    1. Yes
                                    2. No\n
                                    """)
                                if receipt == "1":
                                    today = datetime.today()
                                    print("Transaction type:  Transfer Money")
                                    print("The date and time of transaction:  ", today)
                                    print("Your account card number:  ", client['accountNumber'])
                                    print("Transaction fee:  ", transactionFee)
                                    print("The amount transferred was:  Kshs ", transferAmount)
                                    print("Your account balance is:  ", client['balance'])
                                    print('Your total promotional points are:  ', loyalty)
                                    print("BANK OF KENYA. YOUR HOME FOR INVESTMENT AND FINANCIAL SOLUTIONS.\n")
                                else:
                                    print("Thank you for being a valuable customer")
                                    print("BANK OF KENYA. YOUR HOME FOR INVESTMENT AND FINANCIAL SOLUTIONS.\n")
                        else:
                            """logs the currency that was used for the transaction"""
                            logger.info("Currency picked for transfer: " + transferChoice)
                            transactionRate = 0.03
                            loyalty = client['loyaltyPoints']
                            loyalty += 7
                            transferAmount = int(input("Enter the amount you want to transfer:  "))
                            try:
                                if transferAmount > 4390:
                                    raise maxTransfer
                            except maxTransfer:
                                print("Maximum transfer is 4390 Usd. Try a lower amount.")
                                """logs the error message"""
                                logger.info("Transfer amount exceeds limit.")
                            else:
                                """transfer process to be executed if no error is encountered"""
                                transactionFee = transactionRate * transferAmount
                                client['balance']['Usd'] -= transferAmount + transactionFee
                                client['balance']['Kshs'] = client['balance']['Usd'] * 114
                                accountTransfer['balance']['Usd'] += transferAmount
                                accountTransfer['balance']['Usd'] = accountTransfer['balance']['Kshs'] * 114
                                print("Successful transfer. Your account balance is %.2f: ", client['balance'])
                                """logs the successful transaction message"""
                                logger.info("Transfer successful. Account balance : " + str(client['balance']))
                                """a receipt can be generated if needed"""
                                receipt = input("""
                                    Would you like a receipt?
                                    1. Yes
                                    2. No\n
                                    """)
                                if receipt == "1":
                                    today = datetime.today()
                                    print("Transaction type:  Transfer Money")
                                    print("The date and time of transaction:  ", today)
                                    print("Your account card number:  ", client['accountNumber'])
                                    print("Transaction fee:     ", transactionFee)
                                    print("The amount transferred was:  Kshs ", transferAmount)
                                    print("Your account balance is:  ", client['balance'])
                                    print("Your total promotional points are:  ", loyalty)
                                    print("BANK OF KENYA. YOUR HOME FOR INVESTMENT AND FINANCIAL SOLUTIONS.\n")
                                else:
                                    print("Thank you for being a valuable customer")
                                    print("BANK OF KENYA. YOUR HOME FOR INVESTMENT AND FINANCIAL SOLUTIONS.\n")
                if not successfulTransfer:
                    """error handler for when client tries to send money to themselves or unregistered persons"""
                    for accountTransfer in data['bankData']['clientData']:
                        try:
                            if accountTransferNo == client['accountNumber']:
                                raise invalidTransfer
                            if accountTransferNo != accountTransfer['accountNumber']:
                                raise unregisteredUser
                        except invalidTransfer:
                            print("This operation cannot be executed because you are trying to send money to your "
                                  "account\n")
                            """logs the error message"""
                            logger.info("Invalid operation. Sender is recipient.")
                            break
                        except unregisteredUser:
                            print("This user account is not registered in our system.\n")
                            """logs the error message"""
                            logger.info("Invalid operation. User is not registered")
                            break
            else:
                """if client chooses to exit their session"""
                logger.info("Service picked: " + service)
                """the json file updated with new details from the user session"""
                with open('bankinfo.json', 'w') as f:
                    json.dump(data, f, indent=3)
                break
    if not loginSuccess:
        """error handler for when user tries to log in with wrong credentials"""
        for client in data['bankData']['clientData']:
            try:
                while userpin != client['pin'] and useraccount != client['accountNumber']:
                    raise wrongCredentials
            except wrongCredentials:
                print("Incorrect login credentials. Try again.\n")
                logger.info("Incorrect login credentials. Try again.")
                break