# importing a module
import A_greetings_functions

print("This is the 'using' file")

# greetings_functions module has a function called say_hello
A_greetings_functions.say_hello()
A_greetings_functions.greet_someone('Jiya')

print(f"The name of the use_greeting_functions file is {__name__}")
print(f"The name of the greeting_functions file is {A_greetings_functions.__name__}")
print("The end")

A_greetings_functions.greet_someone()
A_greetings_functions.greet_someone('Paulene')