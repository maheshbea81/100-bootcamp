number = 10
distance = 100

if 0 < number < 42 < distance:
    print("number and distance are within range")
else:
    print("number and distance are out of range")


# equivalent to:
if 0 < number and number < 42 and 42 < distance:
    print("number and distance are within range")
else:
    print("number and distance are out of range")


if 0 < number < 42 and distance != 20:
    print("number is within range and the distance is not 20")
else:
    print("number or distance are out of range")

a = 2
b = 3
c = a * b

print("=" * 120)

minimum_age = 18
maximum_age = 75
age = 36

if minimum_age <= age <= maximum_age:
    print("Your age is within the valid range")



