# function annotations
# an optional feature to add arbitrary comments to parameters and return types
# they add extra data. They do not enforce type checking

# default parameter

def greet_someone(name="World"):
    print(f"Welcome {name}!")
    print(f"Hi {name.capitalize()}, how are you today?")
    print("#" * 60)


# with annotation
def greet_someone2(name: 'str' = "World"):
    print(f"Welcome {name}!")
    print(f"Hi {name.capitalize()}, how are you today?")
    print("#" * 60)


# annotating tuple and dictionary params
def print_vat(**kwargs: 'VAT, gross and message'):
    print(kwargs)


# annotating return type
# this function returns a tuple
def do_magic(number1, number2) -> 'tuple':
    number1_squared = number1 * number1
    number2_doubled = number2 * 2
    return number1_squared, number2_doubled


# see the annotation using __annotations__
print(greet_someone.__annotations__)
print(greet_someone2.__annotations__)
print(print_vat.__annotations__)
print(do_magic.__annotations__)
