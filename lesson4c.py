# A for loo can also be used to iterate through a list, tuple or a dictionary
name = "Caleb"

for letter in name :
    if letter == "l":
        print("The letter is l")
    else:
        print(letter)


print("==================")

# Below is a list of counties

counties = [ "Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret", "Kajiado", "Machakos","Meru", "Embu"]

print(counties)

for county in counties:
    print(county)


print("==================")

for county in counties:
    if "Nairobi" in counties:
        print("The county is in the list")
        break
    else:
        print("County not in the list")


print("=====================================")

# The for loop can be used to iterate through a dictionary

player = {
    "name": "Mbappe",
    "age": 25,
    "teams": ("PSG","Monaco", "France"),
    "nationality": "French"

}

for key in player:
    print(key)
print("=================")

for values in player.values():
    print(values)
for value in player:
    print(player[value])


print("=================")
# loop through the teams the player has played for

for values in player:
    print(player["teams"])
    break
print("=================")
for team in ["teams"]:
    print(team)








    