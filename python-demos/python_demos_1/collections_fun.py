person1 = 'Melissa'
person2 = 'Rob'
person3 = 'Serene'
person4 = 'Callum'

# tuple
person_tuple = 'Melissa', 'Rob', 'Serene', 'Callum'

print(person_tuple)
print(type(person_tuple))

# this tuple has brackets - the brackets are optional
second_tuple = ('Jordan', 'Lou')

print(second_tuple)
print(type(second_tuple))

print(person_tuple[1])
print(person_tuple[3])
print(person_tuple[-1])
# a tuple is IMMUTABLE

marmite_lover = True, True, False

lucky_numbers = [5, 8, 13]
# a list is MUTABLE

print(lucky_numbers)
print(type(lucky_numbers))

# square brackets make lists, items separated by commas
names_list = ['Stephen', 'Mark', 'Nav', 'Nik', 'Lewis']
print(names_list)
print(type(names_list))

names_list.append('Melissa')
print(names_list)
names_list.append('Lewis')
print(names_list)

print(names_list[0])

# dictionaries
# key value pairs

numbers_dictionary = {'Mark': 5, 'Lewis': 8, 'Rob': 2}
print(numbers_dictionary)
print(type(numbers_dictionary))


# sets
# an unique collection
# no duplicates

names_set = {'Lewis', 'Nik', 'Serene', 'Nav', 'Lewis', 'Stephen', 'Nav'}
print(names_set)
print(type(names_set))

number_of_lewises = names_list.count('Lewis')
print(number_of_lewises)