result = 3


def scope_test1():
    #  this variable shadows (hides) result from outer scope
    result = 42
    print("Result inside the function:", result)


scope_test1()
print("Result outside the function:", result)

# ############################################


def scope_test2():
    # instruction to use the global variable inside this function
    global result
    result = 42
    print("Result inside the function:", result)


print("=" * 30)
scope_test2()
print("Result outside the function:", result)
