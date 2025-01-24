'''
1.
'''

# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed_list = ["hello", 42, True, 3.14]

# Accessing elements
print(fruits[0])  # Output: "apple"
print(numbers[2])  # Output: 3

# Slicing
print(fruits[1:3])  # Output: ["banana", "cherry"]

# Modifying lists
fruits.append("orange")
print(fruits)  # Output: ["apple", "banana", "cherry", "orange"]

numbers[1] = 10
print(numbers)  # Output: [1, 10, 3, 4, 5]

# List methods
fruits.sort()
print(fruits)  # Output: ["apple", "banana", "cherry", "orange"]

numbers.reverse()
print(numbers)  # Output: [5, 4, 3, 10, 1]

print(len(mixed_list))  # Output: 4