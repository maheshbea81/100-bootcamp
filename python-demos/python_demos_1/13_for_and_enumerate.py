# classic counting for loop

# single param to range is the STOP value
for i in range(5):
    print(i)

# two params to range is the START + STOP values
for i in range(1, 6):
    print(i)

names = ['Dom', 'Weronika', 'Nihal', 'Alex']
print(names)

# classic for each style loop

# for var in collection:
for name in names:
    print("Hello", name)

# enumerate
for index, name in enumerate(names, start=1):
    print(index, name)

# three params to range is the START + STOP + STEP values
for number in range(2, 11, 2):
    print(number)

for i in range(0, len(names)):
    print(names[i])

numbers = [1, 2, 3, 4]
print("Numbers before loop", numbers)
# foreach style loop
for n in numbers:
    print(n)
    # the sequence values will not change
    n = n + 5

print("Numbers after loop", numbers)

# counting for loop
# an index is needed to alter the sequence
for index, n in enumerate(numbers):
    print(index, n)
    # the sequence values will change because an index is used
    numbers[index] += 100

print("Numbers after loop", numbers)

