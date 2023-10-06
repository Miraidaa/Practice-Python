#print("Hello", end=" ")
#print("World")
#output - Hello World - in a one line - by default World should be in a new line 

#print("apple", "banana", "cherry", sep=", ")
#output - apple, banana, cherry - by default separated by space 

#print("* \n * * \n  * * \n  * *\n *** *** \n  * *\n  * * \n  ***** ")

#print("* \n  * * \n   * * \n  * *\n *** *** \n  * *\n   * * \n  ***** ")

#John had three apples, Mary had five apples, and Adam had six apples.

#create the variables: john, mary, and adam;​

#assign values to the variables. The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively;​
john = 3
mary = 5
adam = 6

#having stored the numbers in the variables, print the variables on one line, and separate each of them with a comma;​
print (john, mary, adam, sep=","); 
#now create a new variable named total_apples equal to addition of the three former variables.​
total_apples = john + mary + adam
#print the value stored in total_apples to the console;​
print(total_apples)
#experiment with your code: create new variables, assign different values to them, and perform various arithmetic operations on  them (e.g., +, -, *, /, //, etc.). 
#Try to print a string and an integer together on one line, e.g., "Total number of apples:" and  total_apples.​


#task2 
'''
kilometers = 12.25​
miles = 7.38;​

miles_to_kilometers = miles * 1.61; 
kilometers_to_miles = kilometers / 1.61;


print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers") 
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
'''

#task3

'''
Take a look at the code in the editor: it reads a float value, puts it into a variable named  x, 
and prints the value of a variable named y. Your task is to complete the code in order  to evaluate the following expression:​

3x3 - 2x2 + 3x - 1​

'''

user_x1 = input ("Enter the number to evaluate the expression:")
user_floatX = float (user_x1)


#hard coded version 
'''
x_int = 1​
x = float(x_int)​
'''

y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("The result of the expression is:", y)


#task4

'''
Your task is to prepare a simple code able to evaluate the end time of a period of time,  
given as a number of minutes (it could be arbitrarily large). 
The start time is given as a  pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.​
'''
hour = int(input("Starting time (0-23): "))
mins = int(input("Starting time (0-59): "))
dura = int(input("Event duration (0-59): "))

end_hour = (hour + (mins + dura) // 60) % 24
end_mins = (mins + dura) % 60

print(f"End time: {end_hour:02}:{end_mins:02}")
