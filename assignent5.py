# 1.
def area():
    length = 20
    width = 10
    area = length * width
    print("The area is :", area)

area()
print("==============================")
# 2.
def numbers(num1,num2):
    sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    division = num1 / num2
    print("The sum is:", sum,"difference is: ", difference," product is:", product,"and division is:", division)

numbers(200,20)
print("==============================")
# 3.

def check_number():

    number = int(input("Enter a number: "))
  
    if number > 0:
        print("The number  is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number  is zero.")
check_number()

print("==============================")
# 4.
def sum_of_number(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    print("THe sum is: ", sum)

n = int(input("Enter a number: "))
sum_of_number(n)








print("==============================")
# 5.
def square_of_numbers(n):
    i = 1
while i <= n:
    square=i**2
    print("The square of ", square)
    i+=1
n= int(input("Enter a number"))
square_of_numbers(n)


print("==============================")
















