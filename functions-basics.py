'''
exceptions: 
  ImportError
  ModuleNotFoundError
  ZeroDivisionError
  NameError-->usually happens, when Variable is not defined, but trying to use 
  TypeError --> when trying to perform operation on different unsupported data types
  IndexError --> when trying to access out of bound index from either list, sets, tuples. 
  functions are re-usable blocks of code.
  docstring is descriptive comments right after function definition noted in "", if you type help(FUN_NAME) it will print comments in ""
  params are the one's that are defined in function definition. args are the one's that are defined in function calling. 
  1. If the function contains a print statement inside:
You just call the function; there's no need for an additional print().

2. If the function returns a value:
You need to use print() explicitly when calling the function to display its return value.
If you just call add(3, 5) without print(), it returns the value but doesn’t display it in the output.

print() inside the function → just call the function.
return inside the function → use print(function_call) to display the result.
positional arguments means, args(in function call) and params (in function definiton) will map one to one. 
keyword args helps us pass args in any order, you have to use variable name in function calling. 
*** positional arguments have to be specified first, followed by keyword args when calling function and if you have both positional and keyword args. 
*args in function definition will be considered as tuples
**kwargs in function defition will considered as dictionaries.
you can have any strings for args or kwargs, only thing is one star and two stars matter. 
  
'''

def calculate(a,**pdb):
    # x = (a+b)*c
    # return x
    print(a)
    # print(pdb)
    for argument in pdb:
        print(argument)
    # return x,y,z,xy


    def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"Argument {key}: {value}")

example_function(name="Alice", age=30, city="New York")
# Expected output:
# Argument name: Alice
# Argument age: 30
# Argument city: New York
In this example, example_function is defined to accept any number of keyword arguments using **kwargs. When the function is called with name="Alice", age=30, and city="New York", these arguments are collected into a dictionary kwargs, which is then iterated over to print each argument's name and value.
