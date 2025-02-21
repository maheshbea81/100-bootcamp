# lambda functions are anonymous short-hand functions

print("######## Example 1 ########")
compare = lambda a, b: -1 if a < b else (+1 if a > b else 0)

x = 42
y = 3

# print("a > b returns:", compare(x, y))
print(f"{x} > {y} returns:", compare(x, y))

x = 2
print(f"{x} > {y} returns:", compare(x, y))

x = 3
print(f"{x} > {y} returns:", compare(x, y))

print("######## Example 2 ########")
numbers_list = [0, 1, 2, 3, 5, 8, 13, 21]
print(f"Original list of numbers: {numbers_list}")

numbers_plus1_list = list(map(lambda num: num + 1, numbers_list))
print(f"New list of numbers plus 1: {numbers_plus1_list}")

numbers_times10_list = list(map(lambda num: num * 10, numbers_list))
print(f"New list of numbers x 10: {numbers_times10_list}")

numbers_squared_list = list(map(lambda num: num * num, numbers_list))
print(f"New list of numbers squared: {numbers_squared_list}")
