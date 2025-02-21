#!/usr/bin/python

# Example Python script
# another comment
# CTRL + /

import sys

# argv is part of the sys module
# argument vector a.k.a the list of parameters or inputs to the program

# argument_count is our variable that stores the number of inputs to the program
# print(len("toria"))
argument_count = len(sys.argv)
print(argument_count)

# 'if' is called a condition expression
if argument_count > 1:
    print('Too many args')
    print('Please try again')
else:
    # where is a variable whose value is a string 'World'
    where = 'World'
    print("Hello", where)

print('Goodbye from ' + sys.argv[0])
print('Goodbye from ', sys.argv[0])
print('one', 'two', 'three', sep="!!!", end="!\n\n\n")
print('four')
# print(sys.argv[1])
# print(sys.argv[2])
# print(sys.argv[3])
# print(sys.argv[4])
# print(sys.argv[1])