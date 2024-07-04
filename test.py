
def remove_whitespace(s):
    return '+'.join(s.split())
print(remove_whitespace("george


#Task 2: Create a function that
# it is lower than 500 but high
number = int(input("Enter numbe
if number > 250 and number < 50
    print("Correct choice")
else:
    print("not correct choice")
     #1-please take an input from the user and count vowels in the given string
user = input(" type a string:")
string_List = user.split()
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for word in string_List:
    vowelCount = 0
    for i in range(0, len(word)):
        if word[i] in vowels:
            vowelCount += 1
    print("in the word", word, "there is ", vowelCount, "vowels")

#2-Please give user an option to give a list of integer, once input is provided, then ask the question, 
# "do you want the minimum or maximum? type 'minimum; to see the number that is smallest" and vice versa the maxmum

lst = [12, 15, 17]
 
for i in lst:
    print(i, end="")
    
name = input("What is your name? ")
print("Hello,", name)
question = "How old are you, " + name + "? "
age = int(input(question))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("enter the number"))
print(factorial(n))

def mcit_factorial_iterative(n):
   result = 1
   for i in range(1, n + 1):
       result *= i
   return result










    


