'''
string slicing:
name = 'mahesh reddy'
name[START:STOP:STEP]   where STOP is not included in the output.
if no ':' are specified , it is START position. name[0] --> will print m, name[-1]  will print y
if 1 ':' and there are values before and after :, they are START and STOP , name[0:10]  --> mahesh red will be printed, remember STOP value is NOT included.
if 2 ':' are specified, first value is START, second is STOP and third is STEP.
Why Are Strings, Integers, and Floats Immutable?
  When you assign a new value to a string, integer, or float, Python doesn't actually "modify" the original object.
  Instead, it creates a new object in memory and updates the variable reference to point to this new object.           
'''

my_string = "Hello, World!"
# Get the first 5 characters
print(my_string[:5])  # Output: Hello
# Get characters from index 7 to 11 (inclusive)
print(my_string[7:12])  # Output: World
# Get every other character
print(my_string[::2])  # Output: Hlo ol!
# Reverse the string
print(my_string[::-1])  # Output: !dlroW ,olleH

