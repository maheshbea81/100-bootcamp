# global variable
result = 3


def my_func():
    # new local variable that shadows the global 'result' variable
    result = 12

    def scope_test():
        # non-local instructs python to use the enclosing variable (12) rather
        # than attempt to create a new variable within this local function
        nonlocal result
        # print(result)
        if result < 15:
            result += 1
            print(result)
            scope_test()

    scope_test()
    print(result, "from my_func")


my_func()
print(result, "from main")

# use the Debugger
# result uses the non-local var defined in my_func so starts at 12
# with each recursive call to scope_test its value is tested against 15
# then it is incremented by one each call until it is no longer > 15
# you can see the stack return from each call to scope_test before returning to my_func


