#Python lists
# A list in python is a collection of items that are ordered in a certain way.
# A list is introduced by the ude of the square brackets []. 
# The items of a list ar estored inside of indexes.
# In programming we start counting from index 0.
# A list is mutable ie the contents of a list can be changed.

cars = ["BMW", "Benz", "Hiance", "Prado", "Probox", "Mclarel", "Range"]
print(cars)
print(type(cars))

# Accessing items of a list
print(cars[2])
print("The car in index four is: ", cars[4])

# List slicing - This is cresting from a given bigger list
print(cars[4:])

# printing from index 0 to three
print(cars[:4])

# printing from hiance to probox
print(cars[2:5])

# List mutability
# We use the function append to add an item at the end of list
cars.append("Mercedes")
print(cars)

cars.append("Subaru")
print(cars)
# We use the pop function to remove an item in the end of the list
cars.pop()
print(cars)
 # We can use index to add items to a list
cars[5] = "Pajero"
print(cars)

# we can use the sort function to sort the items in the list in alphabetical order
# From the last alphabet
cars.sort(reverse=True)
print(cars)
#From the first alphabet
cars.sort(reverse=False)
print(cars)

