# a variable is a place to store data that can change
# python is a dynamically-typed language a.k.a weakly-typed
# java is a strongly-typed language a.k.a statically-typed

# python variable - we just give it a name
first_name = 'Victoria'
print(first_name)

print(type(first_name))

last_name = "Lloyd"
print(last_name)

print(type(last_name))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# This is NOT Python - this is JAVA

# String firstName = "Victoria";
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# concatenation (gluing strings together)

print(first_name)
print(last_name)

full_name = first_name + last_name
print(full_name)

full_name_with_space = first_name + ' ' + last_name
print(full_name_with_space)

chips = 2.50
fish = 4.50
total_cost = fish + chips
print(total_cost)

# operator overloading
# '+' is either concatenation when given strings to work with
# or '+' is addition when given numbers to work with

dinner = 2.50
dinner = dinner + fish
dinner = dinner + 'mushy_peas'

print('The price of dinner is ' + str(dinner))

# short-hand syntax (augmented assignment) / compound operators
dinner += fish

print('The price of dinner is ' + str(dinner))

dinner = dinner - chips
dinner -= chips

print('Friday')
print(123)
print(True)
print('hello', 'Zippy', 'George')
print('hello', 7, 'George', 11)
print('hello ' + str(7))
