
user = {
    'sin':123456789,
    'fr0':53359,
    'fr1':58197,
    'fr2':69695,
    'fr3':106717,
    'fr4':164914,
    'fr5':234609,    
}
def f_tax():
    while True:
        amount = int(input("Enter your income: "))
        if  amount <= user['fr0']:
             user['fr1'] = (amount * 15) /100
             print(f"Your federal tax is {user['fr1']} Dollars")
        elif  amount > user['fr0'] <= user['fr3']:
            user['fr2'] = (amount - user['fr0'] * 20.5/100 ) + (user['fr0'] * 15/100)
            print(f"Your federal tax is {user['fr2']} Dollars")
        elif  amount <= user['fr3'] <= user['fr4']:
            user['fr4'] = (amount - user['fr3'] * 26/100 ) + (user['fr0'] * 15/100) + (user['fr1'] *20.5/100)
            print(f"Your federal tax is {user['fr3']} Dollars")
        elif  amount >= user['fr1']:
            user['fr5'] = amount * 15 /100
            print(f"Your federal tax is {user['fr1']} Dollars")    
        else:
            user['balance'] = user['balance'] - amount
            print(f"{amount} Dollars successfully widthdrawn, your remaining balance is {user['balance']} Dollars")
         

account = "BCB000001"

is_quit = False

print("Welcome to CRA Canada ")
fname = str(input('Please enter your first name: '))
lname = str(input('Please enter your last name: '))
sin = str(input('Please enter your SIN Number: '))
sin = int(input('Confirm your SIN Number: '))



if sin == user['sin']:
    while is_quit == False:

        print(f"\nWelcome to CRA Canada {fname}  ")
        print(" Enter 1 For Federal TAX  \n Enter 2 Ontario TAX \n Enter 3 Quebec TAX \n Enter 4 Alberta TAX \n Enter 4 Logout ")

        query = int(input("Enter Your Choise : "))

        if query == 1:
            f_tax()
        elif query == 2:
            o_tax()
        elif query == 3:
            q_tax()
        elif query == 4:
            a_tax()
        elif query == 5:
            is_quit = True

        else:
            print("Please enter a correct value shown")
else:
    print("Entered wrong info")
