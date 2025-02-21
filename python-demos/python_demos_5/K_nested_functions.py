# Nested functions

def outer():
    num = 42

    def inner():
        print(num, "in inner")
        print("This function is inside the other so 'num' is in scope")

    inner()
    print(num, "in outer")


outer()
# inner()
