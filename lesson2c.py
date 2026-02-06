# A  is a date type that stores data in terms of key  -value pair
# It is introduced by the use of curly braces{}
# The values stored insid eof a dictionary can be of any data type
# To access the values in a dictionary we use the keys


phonebook = {
    "Benson" : "254747483930",
    "Mary" : "254783920101",
    "Stephen" : "254736292029"
}

#showing the entire dictionary
print(phonebook)
print(type(phonebook))

#printing our benson's number

print(phonebook["Benson"])
print('======================')

player = {
    "name" : "Messi",
    "age" : 40,
    "teams" : ["PSG", "Barcelona", "Argentina"],
    "more" : {
        "children" : 3,
        "residence" : "US",
        "phone" : (254737483783, 254737373838, 25437839392)
    }
}
# print Barcelona - the second tean he played for
print(player["teams"][1])

#print messi second number

print( "Messi's second number is: ", player["more"]["phone"][1])

