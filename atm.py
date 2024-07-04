# PYTHON ATM PROGRAM BY PYTHONDEX
# Visit https://pythondex.com for more information

user = {
    'dob':151980,
    'balance':500
}
def Withdraw():
    while True:
        amount = int(input("Enter the amount of money you want to widthdraw: "))
        if amount > user['balance']:
            print("You don't have sufficient balance to make this widthdrawal")
        else:
            user['balance'] = user['balance'] - amount
            print(f"{amount} Dollars successfully widthdrawn your remaining balance is {user['balance']} Dollars")
            print('')
            return False

def Deposit():
    print(f"Total balance {user['balance']} Dollars")
    print('')

is_quit = False

print('')

print("Welcome to the GEORGE IBRAHIM ATM")
fname = str(input('Please enter your first name: '))
lname = str(input('Please enter your last name: '))
dob = int(input('Please enter your date of birth: '))



if dob == user['dob']:
    while is_quit == False:
        print("Welcome GEORGE, what would you like to do today")
        print(" Enter 1 to Withdraw \n Enter 2 for Deposit \n Take out the card")

        query = int(input("Enter the number corresponding to the activity you want to do: "))

        if query == 1:
            Withdraw()
        elif query == 2:
            Deposit()
        elif query == 3:
            is_quit = True

        else:
            print("Please enter a correct value shown")
else:
    print("Entered wrong info")
