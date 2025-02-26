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

def calculate(**pdb):
    for key, value in pdb.items():
        print(f"{key}: {value}")

dict1 = {}
count = 1
while count <= 2:
    key1 = input("Please Enter Sequence: ")
    value1 = input("Please Enter Sequence Value: ")
    dict1[key1] = value1 # Correct way to add key-value pairs
    count += 1

calculate(**dict1) # Correct way to pass the dictionary as keyword arguments


### Code we have written
def emailname(*pdb):
    for email in pdb:
        # print(f"Your Email:  {email}")
        # print(email.split("@"))
        yourname = email.split("@")[0]
        company = email.split("@")[1]
        # print(f"Your Name:  {yourname}")
        # print(f"Your Company:  {company}")
        fname = yourname.split(".")[0]
        lname = yourname.split(".")[1]
        company1 = company.split(".")[0]
        print(f"First Name:  {fname}, Last Name:  {lname}, company Name: {company1}")
        



def emailname(*pdb):
    for email in pdb:
        yourname = email.split("@")[0]
        company = email.split("@")[1]
        fname = yourname.split(".")[0]
        lname = yourname.split(".")[-1]
        if len(yourname.split(".")) > 2:
            mname = yourname.split(".")[1:-1]
            middle = ' '.join(mname)
        else:
            middle = " "
        company1 = company.split(".")[0]
        print(f"First Name:  {fname}, Middle Name:  {middle}, Last Name:  {lname}, company Name: {company1}")
        # print(f"Middle Name: {mname}")

emails = []
count = 1
while count <= 1:
    email = input("Please Enter email: ")
    emails.append(email)
    count += 1

emailname(*emails) # Correct way to pass the dictionary as keyword arguments




##### Chat GPT code
def emailname(*emails):
    """
    Extracts first, middle, last names, and company name from email addresses.

    Args:
        *emails: Variable number of email address strings.
    """
    for email in emails:
        parts = email.split("@")
        if len(parts) != 2: # handle invalid email
          print(f"Invalid email: {email}")
          continue

        yourname, company = parts
        names = yourname.split(".")
        fname = names[0]
        lname = names[-1]

        middle = " ".join(names[1:-1]) if len(names) > 2 else ""

        company1 = company.split(".")[0]

        print(f"First Name: {fname} Middle Name: {middle} Last Name: {lname} Company Name: {company1}")

emails = []
while True:
    email = input("Enter email (or 'done' to finish): ")
    if email.lower() == "done":
        break
    emails.append(email)

emailname(*emails)
# email = input("Please Enter email: ") #simplified, only one email
# emails.append(email)
#
# emailname(*emails)



#Functions - Basics
def my_first_function(x, y): #defining a function that takes two parameters
    sum = x + y
    return sum #this statement is used to exit a function and return something when the function is called
    
my_first_function(1, 2) #calling a function and passing two POSITIONAL arguments, the values of 1 and 2; result is 3
 
my_first_function(x = 1, y = 2) #calling a function and passing two KEYWORD arguments, the values of 1 and 2; result is 3
 
my_first_function(1, y = 2) #calling a function and passing mixed types of arguments, the values of 1 and 2; result is 3; rule: positional arguments always before keyword arguments!
 
def my_first_function(x, y, z = 3): #specifying a default parameter value in a function definition
 
def my_first_function(x, *args) #specifying a variable number of positional parameters in a function definition; args is a tuple
 
def my_first_function(x, **kwargs) #specifying a variable number of keyword parameters in a function definition; kwargs is a dictionary
 
global my_var #"importing" a variable in the global namespace to the local namespace of a function
