#task1 

'''Using one of the comparison operators in Python, write a simple two-line
 program that takes the parameter n as input, which is an integer, and prints False if n is less than 100, and True if n is greater than or equal to 100.
'''

n = int (input("Enter the number"))
number = n 
if (number < 100) :
    print("False")
else :
        print ("True")


#task2 

''' 
As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.

Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

if the year number isn't divisible by four, it's a common year; 
otherwise, if the year number isn't divisible by 100, it's a leap year; 
otherwise, if the year number isn't divisible by 400, it's a common year; 
otherwise, it's a leap year.


The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.

It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian 
calendar period. Tip: use the != and % operators.

'''

getYear = int (input("Enter the year : "))
year = getYear

if (year % 4 != 0) :
    print("Its a common year")
elif (year % 100 != 0) : 
    print("Its a leap year") 
elif (year % 400 != 0) :
    print("Its a common year")
else : 
    print ("Its a leap year") 

#task3 

'''Scenario

A junior magician has picked a secret number. He has hidden it in a variable named secret_number. He wants everyone who run his program to play the Guess
 the secret number game, and guess what number he has picked for them. Those who don't guess the number will be stuck in an endless loop forever! Unfortunately, 
 e does not know how to complete the code.

Your task is to help the magician complete the code in the editor in such a way so that the code:

will ask the user to enter an integer number; will use a while loop;
will check whether the number entered by the user is the same as the number picked by the magician.
 If the number chosen by the user is different than the magician's secret number, the user should see the message "Ha ha! You're stuck in my loop!"
  and be prompted to enter a number again. If the number entered by the user matches the number picked by the magician, the number should be printed to the screen, 
  and the magician should say the following words: "Well done, muggle! You are free now."
'''
secret_number = 209

while True:
    userNum = int(input("Guess the number: "))
    
    if userNum == secret_number:
        print("Well done, muggle! You are free now.")
        break  
    else:
        print("Ha ha! You're stuck in my loop!")

#task4 

'''Scenario

In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) which can be described in the following way:

take any non-negative and non-zero integer number and name it c0;
if it's even, evaluate a new c0 as c0 ÷ 2;
otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
if c0 ≠ 1, skip to point 2.

The hypothesis says that regardless of the initial value of c0, it will always go to 1.

Of course, it's an extremely complex task to use a computer in order to prove the hypothesis for any natural number (it may even require artificial intelligence),
 but you can use Python to check some individual numbers. Maybe you'll even find the one which would disprove the hypothesis.

Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1. 
We also want you to count the steps needed to achieve the goal.
Your code should output all the intermediate values of c0, too.

Hint: the most important part of the problem is how to transform Collatz's idea into a while loop - this is the key to success.
Scenario

'''

getNum = int(input("Enter a non-negative, non-zero number:"))
steps = 0  # Initialize the step count

while getNum != 1:
    if getNum % 2 == 0:
        getNum = getNum // 2  
    else:
        getNum = 3 * getNum + 1
    steps += 1  # Increment the step count
    print(getNum)

print("Number of steps needed to reach 1: {steps}")

#task5

'''
Scenario

The break statement is used to exit/terminate a loop.

Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters "chupacabra" as the secret exit word, 
in which case the message "You've successfully left the loop." should be printed to the screen, and the loop should terminate.

Don't print any of the words entered by the user. Use the concept of conditional execution and the break statement.

'''
secret_exit_word = "chupacabra"
usersWord = input("Enter a word: ")

while usersWord != secret_exit_word:
    usersWord = input("Enter a word: ")

print("You've successfully left the loop.")

#task6 

user_word = input ("Please enter the word")
user_word = user_word.upper()
vowels = "AEIOU"
result = ""
for char in user_word:
    if char in vowels :
        continue 
    result += char 
print (result) 

#LISTS

#task7

'''
Scenario

There once was a hat. The hat contained no rabbit, but a list of five numbers: 
1, 2, 3, 4, and 5.

Your task is to:

write a line of code that prompts the user to replace the middle number in 	the list with an integer number entered by the user (Step 1)
write a line of code that removes the last element from the list (Step 2) write a line of code that prints the length of the existing list (Step 3).

'''

hat_list = [1,2,3,4,5]
user_num = int (input("Enter the number")) 

#step 1
hat_list.insert (len(hat_list)//2 , user_num)

#step 2 
hat_list.pop()

#step 3
print("Updated list:", hat_list)
print("Length of the list:", len(hat_list))






#task8 

'''The Beatles were one of the most popular music group of the 1960s, and the best-selling band in history. 
Some people consider them to be the most influential act of the rock era. Indeed, they were included in Time magazine's compilation of the 20th Century's 100 most 
influential people.

The band underwent many line-up changes, culminating in 1962 with the line-up of John Lennon, Paul McCartney, George Harrison, and Richard Starkey 
(better known as Ringo 
Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:

step 1: create an empty list named beatles;
step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
step 5: use the insert() method to add Ringo Starr to the beginning of the list.
'''

#step 1
beatles = []

# step 2 
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

#step3 
for _ in range(2): 
    otherMembers = input ("Enter the names of other two members")
    beatles.append(otherMembers)

#step4 
del beatles[3]
del beatles [3]

#step 5 
beatles.insert(0, " Ringo Starr ")

print (beatles)

task9 
'''Scenario
Imagine a list - not very long, not very complicated, just a simple list containing some integer numbers. Some of these numbers may
 be repeated, and this is the clue. We don't want any repetitions. We want them to be removed.

Your task is to write a program which removes all the number repetitions from the list. The goal is to have a list in which
 all the numbers appear not more than once.

Note: assume that the source list is hard-coded inside the code - you don't have to enter it from the keyboard. 
Of course, you can improve the code and add a part that can carry out a conversation with the user and obtain all the data from her/him.

Hint: we encourage you to create a new list as a temporary work area - you don't
need to update the list in situ.

We've provided no test data, as that would be too easy. You can use our skeleton instead.
'''


test_input  = [1,2,34,2,5,6,7,7,7,6]
result = []
for item in test_input :
    if item not in test_input :
        result.append(item)
    print(result)