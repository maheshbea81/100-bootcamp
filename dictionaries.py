'''
1. dictionaries are key valued pairs , enclosed in {key:value, key2:pair2}
'''

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
len(dict1)

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
