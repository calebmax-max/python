# Create a python program that is able to determine whether a number entered is an old number or an even number.
# number = int(input("Enter number: "))
# if number % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is old")

# Create a python program that is able to determine whether a person can donate blood based on the age and weight of a person. If the weight is greater than 50kg and age is above 18 he can be able to donate blood else not possible

weight = float(input("Enter your weight: "))
age = int(input("Enter your age: "))
if age >= 18 and weight >50:
    print("Can donate")
else:
    print("Not possible")
    
