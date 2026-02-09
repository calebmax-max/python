# Loops - Sometimes we may need to do a piece of work a number of repeated times in such cases we may use loops.
# A loop is a control structure that allows us to execute a block of code repeatedly until a certain condition is met.
# There are two types of loops in python, the for loop and the while loop.

# Below is a syntax of a for loop in python:
"""
for variable in range(n):
    # block of code to be executed
"""

for greeting in range(5):
    print("Hello Moses")

print("========================")

for number in range(10,20):
    print(number)
print("==================")
# find the even numbers from the range of 50 - 71
for number in range(50,71,2):
    print(number)

print("===========================")
# create a python program that prints odd numbers from 100 - 150

for number in range(101,150,2):
    print(number)

for number in range(100,150):
    if number % 2 != 0:
        print(number)
print("===========================")

# create  a program that prints the multiples of 3 from 201 to 150

for number in range(201,150,-1):
    if number % 3 == 0:
        print(number)

for number in range(201,150,-3):
    print(number)
print("==========================================")

# create a pyhton program that prints the leap years in between 2000 and 2024

for years in range(2000,2024,4):
    print(years)
    
    


