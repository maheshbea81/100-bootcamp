# guess who

# name must be a STRING STR
name = "Dave"
print(name)
# print(name.upper())
name_capitalized = name.upper()
print(name)
print(name_capitalized)

am_I_uppercase = name_capitalized.isupper()
print(am_I_uppercase)


names = ["Tinky Winky", "Dipsy", "La-la", "Po"]
count_of_names = names.count("Po")
print(count_of_names)

print(len(names))

popped_item = names.pop(1)
print(popped_item)
print(names)
