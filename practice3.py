#   Functions in Python 

''' 
def is a keyword, return is optional 
'''
#example 1 
def say_hello():
    print("Hello, world!")

say_hello()

#example 2
def greet(name):
    print(f"Hello, {name}!")

# Call the function with an argument
greet("Alice")
greet("Bob")

#example 3 
def countSum (a, b) :
    result = a + b 
    print (result) 

countSum(2,88)
countSum(78,89)

#example 4 - function with multiple return values 
def get_name_and_age():
    name = "Alice"
    age = 30
    return name, age

name, age = get_name_and_age()
print(f"Name: {name}, Age: {age}")

# example 5 
def get_sum_difference_product(a, b):
    sum_result = a + b
    difference = a - b
    product = a * b

    print(f"The sum is : {sum_result}")
    print(f"The difference is : {difference}")
    print(f"The product is : {product}")

get_sum_difference_product(4, 5)


# Tuples in Python 

#example 1
my_tuple = (1, 2, 3, "hello", 3.14)

#accessing elements through their index

print(my_tuple[0])  # Accesses the first element (1)
print(my_tuple[3])  # Accesses the fourth element ("hello")


#Packing and unpacking tuples 

coordinates = (3, 4)
x, y = coordinates  # Unpacking the tuple into individual variables
print(f"x: {x}, y: {y}")


#Task 1 
'''
Questions:
1. Write a Python program to create a tuple with different data types.
2. Swap two tuples in Python Given: 
       tuple1 = (10, 55) 
       tuple2 = (29, 45)
3. Write a python program that Counts the number of occurrences of item 36 from a tuple.
        tuple1 = (50, 36, 60, 70, 36,75,96)
4. Write a python program to Access value 20 from the tuple.
       tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
'''
#1 
diffData = ("hey", 20, True, [3,6,7,8])

#2 
tuple1 = (10, 55) 
swap1 = tuple1[1]
swap2 = tuple1[0]
print(swap1, swap2)

tuple2 = (29, 45)
swapT1 = tuple2[1]
swapT2 = tuple2[0]
print(swapT1, swapT2)

#3 - count occurence of 36 
cntOcc = (50, 36, 60, 70, 36,75,96) 
cnt = 0 

for element in cntOcc : 
    if element == 36 :
        cnt += 1

print (cnt)
    
#4 Write a python program to Access value 20 from the tuple.
get20 = ("Orange", [10, 20, 30], (5, 15, 25))
value = get20[1][1]
print(value)


#Sets in Python 
'''ets are defined using curly braces {} or by using the set() constructor.
 Sets are widely used for tasks that involve eliminating duplicate values and performing 
 set operations like union, intersection, and difference. '''

 #example  1
fruits = {"apple", "banana", "cherry"} # can use curly braces 
numbers = set([1, 2, 3, 4, 5]) # can use set()

#exmaple 2 
fruits.add("orange")
fruits.remove("banana")
fruits.discard("pear")

#Set Operations 

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Union
union_set = set1 | set2  # or set1.union(set2)

# Intersection
intersection_set = set1 & set2  # or set1.intersection(set2)

# Difference
difference_set = set1 - set2  # or set1.difference(set2)
 


#iterating 
for fruit in fruits:
    print(fruit)

#checking elements 
if "apple" in fruits:
    print("Yes, apple is in the set.")

#set comprehension 
squared_numbers = {x**2 for x in range(1, 6)}

#Task2 
'''
1.Write a Python program to create a set with different data types.
2.Create a set using for loop.
       fruit_set = {"apple", "banana", "cherry"}
3.  Return a new set of identical items from two sets
        set1 = {15, 25, 80, 85, 90} 
        set2 = {25, 80, 82, 85, 100} 
        Output: 
        {25, 80, 85}
'''

#1 
difSet = {"eating", 12, True, ['l', 'v', 'm', 'h']}

#2 
mtSet = set()
listToAdd = ["apple", "banana", "cherry"]
for element in listToAdd:
 mtSet.add(element)

print(mtSet)

#3 Return a new set of identical items from two sets
set1 = {15, 25, 80, 85, 90} 
set2 = {25, 80, 82, 85, 100} 

for element in set1 : 
    if element in set2: 
        print(element)