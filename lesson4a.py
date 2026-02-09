# Nested if statement
# It is an if statement that is contained within another if statement

age = 20
weight = 60

if age > 15:
    if weight > 50:
        print("You can donate blood")
    else:
        print("You cannot donate blood because of your weight")
else:
    print("You cannot donate blood because of your age")