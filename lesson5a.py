# Python funtions
# They are a block pf code/statement that performs a given task/action. They can be reused .
# They are defined using the def keyword. (define)
# We have two main types of functions i.e:
# 1. In-built functions -> They come preinstalled with the interpreter i.e print(), pop(), range(), append() etc.
# 2. User defined function => They are created by a programmer to solve a given task.
# To define a function you need to give it a name followed by paranthesis.
# For the functions , it is usually indented and to invoke a function we use the function name.

def greeting():
    print("Hello, how are you")
 # Below we call a function by its   

greeting()

print("=====================================")
# Addition function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the numbers is: ", sum)
addition()

print("=====================================")

# create a function that is able to multiply three values
def multiplication():
    num1 = 1
    num2 = 2
    num3 = 4
    product = num1 * num2 * num3
    print("The product of the numbers is: ", product)

multiplication()

print("=====================================")
# below is a division function
def divide():
    number1 = int(input("Enter the first number"))
    number2 = int(input("Enter the second number"))
    quotient = number1 / number2
    print("The answer is: ", quotient)
    print("-------")

for function in range(3):
    divide()
