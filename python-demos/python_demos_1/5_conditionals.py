temp = 0

if temp < 10:
    print("That’s cold")
elif temp <= 15:
    print("That’s mild")
else:
    print("That’s warm")


name = 'Victoria'
print(id(name))

name2 = 'Bob'
print(id(name2))

name3 = name2
print(id(name3))

team1 = ['Alex', 'Dom', 'Kamil', 'Nihal', 'Prakash']

team2 = ['Ismail', 'James', 'Nathan', 'Weronika']

if team1 == team2:
    print("The teams are the same")
else:
    print("The teams are different")

team3 = team2

if team2 == team3:
    print("Team 2 and Team 3 are the same team")

team4 = ['Alex', 'Dom', 'Kamil', 'Nihal', 'Prakash']

if team1 == team4:
    print("Team 4 and Team 1 are the same team")

if 'Prakash' in team1:
    print("Prakash is in team 1!")
else:
    print("Prakash is in team 2!!")

print('Team1', id(team1))
print('Team2', id(team2))
print('Team3', id(team3))
print('Team4', id(team4))

# == is called value equality

# 'is' uses the id() function under the hood for reference equality
print(team2 is team4)
print(team2 is team3)
print(team1 is team4)

# use == for value equality
# use is for reference equality


