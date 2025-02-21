# create a function
# we define a function

def say_hello():
    print("Hello World!")
    print("Goodbye World!")
    print("~" * 50)


# default parameter
def greet_someone(name="World"):
    print(f"Welcome {name}!")
    print(f"Hi {name.capitalize()}, how are you today?")
    print("#" * 60)


def display_info(name, lucky_number, hobby='Coding', favourite_place='PyCharm'):
    print("*" * 50)
    print(f"Your name is: {name}.\nYour lucky number is: {lucky_number}.\nYour hobby is: {hobby}."
          f"\nYour favourite place is: {favourite_place}")
    print("*" * 50)
# the 'main' trick
# when function dev runs this file they should see the tests
# when the using dev imports this module they should NOT see the tests


if __name__ == "__main__":
    # test the function
    print("This is a test")
    say_hello()
    greet_someone('Minahil')
    greet_someone('Ben')
    print("This is the 'functions' file")
    print(f"The name of the greetings_function file is {__name__}")
    display_info('Lisa', 10, hobby='Playing the sax', favourite_place='School')
    display_info(name='Bart', lucky_number=5, hobby='Playing truant', favourite_place='The treehouse')
    display_info('Katy', 10, favourite_place="VS Code")
    print("The end of the tests")
