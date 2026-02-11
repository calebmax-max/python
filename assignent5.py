# 1.
def area():
    length = 20
    width = 10
    area = length * width
    print("The area is :", area)

area()

# 2.
def numbers(num1,num2):
    sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    division = num1 / num2
    print("The sum is:", sum,"difference is: ", difference," product is:", product,"and division is:", division)

numbers(200,20)

# 3.


number = int(input("Enter a number: "))
  
if number > 0:
    print("The number  is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number  is zero.")


# 4.
number = int(input("Enter number"))

for number in range(10):
     print(number)
     number += number

# 5.
number = int(input("Enter number: "))

while number > 1:
    print(number)
    number = number ** 2


















