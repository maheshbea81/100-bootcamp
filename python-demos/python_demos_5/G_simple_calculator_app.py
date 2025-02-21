from F_arithmetic_functions import *

# help(F_arithmetic_functions)

result = None
value1 = 123
value2 = 567

# passing the arguments positionally
result = add(value1, value2)
print(f"The first result is: {result}")

result = add(value2, 42)
print(f"The second result is: {result}")

# no return
print("Print does something - it does not return anything")

# # input has a 'return' statement
# firstname = input("What is your name?")
# print("Your firstname is " + firstname)

subtract_result = subtract(864, 34)
print(f"The subtract result is: {subtract_result}")

subtract_result2 = subtract(value2, value1)
subtract_result2 = subtract(number2=value2, number1=value1)

add_a = add_many(2, 5, 7, 89, 43, 12)
print(add_a)

nums = 20, 41, 9, 34, 1, 56, 8, 3
# call the function and unpack the tuple
add_b = add_many(*nums)
print(add_b)

print(f"Value 1: {value1}, Value 2: {value2}")
squared, doubled = do_magic(value1, value2)
print(squared, doubled)


