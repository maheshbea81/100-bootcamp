'''
1. dictionaries are key valued pairs , enclosed in {key:value, key2:pair2}, mutable.
2. int,float, boolean, strings, +tuples --> immutable, dictionaries, lists, sets --> mutable. 
Dictionary is mutable and set of unorderd key value pair.
It is combination of ":" and ",".
>>> dict1 = {}
>>> dict1
   {}
>>> type(dict1)
>>> <class 'dict'>
If empty {} will always be a Dictionary.
If inside {} we have ":" then it will be Dictionary. If it will have 
Below are DICTIONARY:
A = {}
A = {"A1":10}
A = {"A1":10,"A2":11}
Below are set
A = {10}
A = {"A1"}
A = {10,11}

dict1 = {"Vendor":"Cisco", "Model":"2600","IOS":"12.4", "Ports":"404"}
Below are some common class/methods/operations can be performed on dictionary:
## To delete a key pair
del dict1["Ports"]
## length of dictionary
len(dict1) --> will give # of key:value pairs

"IOS" in dict1
True
"IOS2" in dict1
False
dict1.keys()
dict1.values()
dict1.items() ---- This will return output as tupple
dict1['Vendor']

Strings, Tuples/Frozenset and Dictionary keys are immutable
List/Sets/ Dictionary Key value are mutable

3. dict1={1:'a',2:'b',3:'c'}
   list(reversed(dict1.items()))  --> output in reversed format [(3, 'c'), (2, 'b'), (1, 'a')], you can use list(reversed(dict1.values()), list(reversed(dict1.keys())


'''



# dictionary construction

country_capitals = {'Australia': 'Canberra', 'Eire': 'Dublin',
                    'France': 'Paris', 'Finland': 'Helsinki',
                    'UK': 'London', 'US': 'Washington'}

alternate_country_capitals = dict(Hungary='Budapest', Sweden='Stockholm')

print(f"Country Capital Dictionary: {country_capitals}")
print(f"Alternate Country Capital Dictionary: {alternate_country_capitals}")

print(f"UK Capital City: {country_capitals['UK']}")

# add a key-value pair
country = 'Iceland'
country_capitals[country] = 'Reykjavik'
print(f"Country Capital Dictionary: {country_capitals}")

# add a key-value pair
country = 'Germany'
capital = 'Berlin'
country_capitals[country] = capital
print(f"Country Capital Dictionary: {country_capitals}")

# dictionary of string keys and list values
country_cities = {'UK': ['London', 'Wigan', 'Macclesfield', 'Bolton'],
                  'US': ['Miami', 'Springfield', 'New York', 'Boston']}

print(f"Country Cities Dictionary: {country_cities}")

print(f"Third UK City: {country_cities['UK'][2]}")

homer = 1
print(country_cities['US'][homer])

# add a key-value pair
country_cities['FR'] = ['Paris', 'Lyon', 'Bordeaux', 'Toulouse']

for country in country_cities.keys():
    print(country, ': ', country_cities[country])

# remove an item

del country_cities['US']

print(f"Country Cities Dictionary: {country_cities}")

removed_item = country_cities.pop('FR')
print(f"Removed item: {removed_item}")

# key error
# removed_item = country_cities.pop('DE')

# clear the dictionary
country_cities.clear()
print(f"Country Cities Dictionary: {country_cities}")

# merge two dictionaries
fruit = {1: 'Apple', 2: 'Banana', 3: 'Cherries'}
vegetables = {11: 'Tomatoes', 12: 'Carrots'}

for k, v in fruit.items():
    print(k, v)


for k, v in vegetables.items():
    print(k, v)

fruit.update(vegetables)

for k, v in fruit.items():
    print(k, v)


# as a tuple
for kv in vegetables.items():
    print(kv)

# turn values into a list
veggies_list = list(vegetables.values())
print(veggies_list)

# see keys in either dictionary using | operator
all_keys = fruit.keys() | vegetables.keys()
print(all_keys)


