
user = {
    'dob':151980,
    'balance':1000,   
}
def Withdraw():
    while True:
        amount = int(input("Enter the amount of money you want to widthdraw: "))
        if amount > user['balance']:
            print("You don't have sufficient balance to make this widthdrawal")
        else:
            user['balance'] = user['balance'] - amount
            print(f"{amount} Dollars successfully withdrawn your remaining balance is {user['balance']} Dollars")
            print('')
            return query

def Deposit():
    print(f"Total balance {user['balance']} Dollars")
    print('')
    return query
def Withdraw_limit():
    print("Withdraw limit to 5000 $")
    return query

account = "BCB000001"

is_quit = False

print("Welcome to the Beautiful Canada Bank")
print(" Enter 1 Create a checking account \n Enter 2 Create a saving account")
number = str(input('Enter your choice:'))
fname = str(input('Please enter your first name: '))
lname = str(input('Please enter your last name: '))
dob = str(input('Please enter your date of birth: '))
dob = int(input('Confirm your date of birth: '))



if dob == user['dob']:
    while is_quit == False:

        
        print(f"\nCongratulations!!! {fname} {lname} Welcome to Beautiful Canada Bank Family")

        print(f"\nYour account number is: {account} ")

        print(f"\nWhat would you like to do today {fname}  ")
        print(" Enter 1 Withdraw  \n Enter 2 Deposit \n enter 3 Increase the Withdraw limit to 5000 \n enter 4 Quit")

        query = int(input("Enter the number corresponding to the activity you want to do: "))

        if query == 1:
            Withdraw()
        elif query == 2:
            Deposit()
        elif query == 3:
            Withdraw_limit()
        elif query == 4:
            is_quit = True

        else:
            print("Please enter a correct value shown")
else:
    print("Entered wrong info")
