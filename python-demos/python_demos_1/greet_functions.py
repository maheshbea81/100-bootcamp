

def say_hello():
    print("Hello World!!!")
    print("Goodbye World!!!")


def create_greeting_message(name):
    # declare a variable called message and
    # assign to it the concatenated result of 'Hello' and a name
    message = "Hello " + name
    # use the return keyword to hand an output to the caller
    return message


# The * represents a variadic parameter
def greet_many(*names):
    print(names)
    print(type(names))


def test_my_functions():
    # test my functions
    say_hello()
    say_hello()
    say_hello()

    # declare a greeting variable and assign to it the created greeting message (function call)
    greeting = create_greeting_message("Nihal")
    # output the string to the standard output stream
    print(greeting)
    # output the string as uppercase (uses a method) to the standard output stream
    print(greeting.upper())

    greet_many("James", "Dom", "Kamil")


print("My __name__ is", __name__, " I am the greet_functions file")

if __name__ == "__main__":
    test_my_functions()
    print(__name__)
