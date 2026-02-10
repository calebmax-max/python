# functions with parameters
# Parameters: They are values that get passed as arguments given to a function inside of the paranthesis


def greeting(name):
    print(f"{name} How are you ? Hope everything is fine")

greeting("Caleb")
greeting("Andy")
greeting("Max")

print("=====================================")
def message(names):
    print(f"Hello {names} .We shall be having a general meeting on date ..... Please avail yourself.")

message("Joy")
message("Stephen")

print("=====================================")
# create  a function that accepts parameters to add two numbers

def addition(num1,num2):
    sum = num1 + num2
    print(f"The total is:", sum)
addition(6,3)


