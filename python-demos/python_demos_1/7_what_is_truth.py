# What is truth?

a = 0
b = 1

# use function bool() to test an object as a Boolean
a_result = bool(a)
b_result = bool(b)

print(f"a {a} is {a_result}")
print(f"b {b} is {b_result}")
print("0 evaluates to False")

print(f"An empty string is always", bool(""))

print(f"An empty list is always", bool([]))

print(f"Any empty collection is always", bool({}))

print(f"Any non-empty collection is always", bool({0}))

print(f"Any non-empty collection is always", bool([1,2,3]))