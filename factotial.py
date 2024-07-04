
def factorial(f):

    if f == 1:
        return 1
    else:
        return (f * factorial(f-1))

f = int(input("factorial of numder:"))
print(factorial(f))

#1. Write a number to check if that is a prime member of, for example 3, 5, 7, 23 etc

def is_prime(p):
    if p < 2:
        return False
    i = 2
    while i*i <= p:
        if p % i == 0:
            return False
        i += 1
    return True
p = int(input("Check if prime : "))
print(is_prime(p))

2. #Write a function to calculate the Fibonacci sequence up to n numbers.

def fibonacci(n):
    a = 0
    b = 1

    if n < 0:
        print("Incorrect input")
         
    elif n == 0:
        return 0
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b
n = int(input("fibonacci of : "))
print(fibonacci(n))

#3. Write a function to find the common elements between two lists.
def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
 
    if (a_set & b_set):
        print(a_set & b_set)
    else:
        print("No common elements") 
          
  
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
common_member(a, b)
  
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
common_member(a, b)

a = ['this','not','that','that']
b = ['this','this','n','that']
common_member(a, b)
a = ['this','not','that','that']
b = ['maybe','notyet','n','yes']
common_member(a, b)

# Write a function to sum all the numbers in a list.

numbers = [1,2,3,4,5,1,4,5]
number_list = [1,2,3,4,5,1,4,5] 
number_list1 = [1,2,3,4,5,1,4,5]
Sum = sum(numbers)
print(Sum)
 
Sum = sum(numbers + number_list + number_list1 )
print(Sum)
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
#please try this problem, so it should sum only the even numbers here from the list
sum_even_numbers = [1, 2, 3, 4, 5, 6]
 

even_nos = [num for num in sum_even_numbers if num % 2 == 0]

sum = sum(even_nos)
 
print(sum)

#Task 1: Create a function that takes an input from the user and fills up the whitespaces with + sign


def remove_whitespace(s):
    return '+'.join(s.split())
print(remove_whitespace("george ibrahim"))  # Output: "george+ibrahim"


#Task 2: Create a function that takes a number as an input from the user and checks if
# it is lower than 500 but higher than 250
number = int(input("Enter number: "))
if number > 250 and number < 500:  #the issue is here how can i rewrite it to allow this?
    print("Correct choice")
else:
    print("not correct choice")
#Please give user an option to give a list of integer, once input is provided, then ask the question, 
# "do you want the minimum or maximum? type 'minimum; to see the number that is smallest" and vice versa the maxmum




