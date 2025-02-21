# # import the functions so that we can use them
# import greet_functions
#
# print("My __name__ is", __name__, " I am the use_greet_functions file")
#
# greet_functions.say_hello()

from greet_functions import create_greeting_message

print(create_greeting_message("Dave"))

# a is a variable
# 42 is a numeric literal - an integer, a whole number
a = 42

message_one = "How are you doing?"
message_two = "How are y'all doing?"
message_three = "Peter shouted 'BOO!' at Jane"
message_four = 'Peter shouted "BOO!" at Jane'

# a single = is the assignment operator
# is a right-associative operator

print(a)
a = None
print(a)

# del is not a function
# del is a statement
del a

# print(a)

# print "Hello World"
print("Hello World")

print(locals())



