# A Tuple is a immunatable typr of a list ie it cannot change.
# To introduce a tuple we use paranthesis ()
counties = ("Nairobi", "Mombasa", "Nakuru", "Eldoret", "Kajiado", "Kisii")
print(counties)
print(type(counties))

# Slicing of tuples
print(counties[3:])

# Accessinf items of a tuple by use of indexes
print(counties[5])
print(counties[9])

# Note: Below will generate an error
#Attribute error
counties.append("Machakos")
print(counties)