'''
strings can be denoted using '' or "", you can use ''' ''' for multi line comment
name[-1] is last char in the string, you can use -1,-2,-3 to get last chars 
variable.index('i') --> will get us the index value of first occurance. 
variable.strip() --> will strip spaces in front and end of variabl, you can also strip other chars from string
variable.replace(' ', '') --> will replace  empty space in WHOLE STRING
variable.split('$')  --> output is a LIST of chars without delimiter $, compared to replace method, split's output is a LIST of items
variabl.count("c") --> number of occurance of c
variabl.find("c") --> will give FIRST index occurance of c, will give -1 if string not present
variabl.lower(), variabl.upper()
variabl.split(',')  --> output is a LIST of items with no delimiter (remember it like this, split=list, split=list, read it 5 times)
"_".join(variable) --> will insert _ after each char. --> join and split are opposite, join takes list as input and string as output.
variabl.removeprefix and variable.removesuffix() are newly introduced in 3.9 python to remove prefixes and suffixes from strings. 
string formating: "cisco: %s, wan switchs, %f ports" % ("",2,3.4)
string-var[::-1] -->prints chars from last to first, use case: palindrome finding etc 
abs(5) and abs(-5) returns 5, absolute is nothing but, distance between number and zero. 
'''

'''accessing dictionary values'''
person = {"name": "Bob", "occupation": "Engineer"}
print(f"Name: {person['name']}, Occupation: {person['occupation']}")

'''formating numbers'''
pi = 3.14159
print(f"The value of pi is approximately {pi:.2f}")

'''expression evaluation'''
x = 10
y = 5
print(f"The sum of {x} and {y} is {x + y}")

''' basic python evaluation'''
name = "Alice"
age = 30
print(f"Hello, my name is {name} and I am {age} years old.")

'''calling functions'''
def square(x):
    return x * x
print(f"The square of 5 is {square(5)}")

