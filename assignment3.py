income = float(input("Enter your income:"))

if income > 0 and income < 5999:
  print("Your monthly contribution is Ksh 150.00")
elif income > 6000 and income < 7999:
  print("Your monthly contribution is Ksh 300.00 ")
elif income > 8000 and income < 11999:
  print("Your monthly contribution is Ksh 400.00")
elif income > 12000 and income < 14999:
  print("Your monthly contribution is Ksh 500.00")
elif income > 15000 and income < 19900:
  print("Your monthly contribution is Ksh 600.00 ")
elif income > 20000 and income < 24999:
  print("Your monthly contribution is Ksh 750.00")
elif income > 25000 and income < 29000:
  print("Your monthly contribution is Ksh 850.00")
elif income > 30000 and income < 49000:
  print("Your monthly contribution is Ksh 1000.00")
elif income > 50000 and income < 99999:
  print("Your monthly contribution is Ksh 1500.00")
else:
  print("Your monthly contribution is Ksh 2000.00")





# Loops
#The while Loop
#With the while loop we can execute a set of statements as long as a condition is true.
i = 1
while i < 6:
  print(i)
  i += 1

#The break Statement
#With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
#The continue Statement
#With the continue statement we can stop the current iteration, and continue with the next:


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#The else Statement
#With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


#Python For Loops
#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#The range() Function
#To loop through a set of code a specified number of times, we can use the range() function,
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

for x in range(6):
  print(x)
#Else in For Loop
#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

for x in range(6):
  print(x)
else:
  print("Finally finished!")

#The pass Statement
#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass