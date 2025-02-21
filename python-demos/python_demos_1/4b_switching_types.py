num = 42
print(type(num))

pi = 3.142
print(type(pi))

num = num/pi
print(num)
print(type(num))

port = 8081
# TypeError: can only concatenate str (not "int") to str
# print("Unused port: " + port)

port_as_string = str(port)
print(type(port_as_string))
print("Unused port: " + port_as_string)

# explicit cast to str
print("Unused port: " + str(port))

port_as_float = float(port)
print(port_as_float)

list_within_a_list = ['Cheddar', ['Camembert', 'Brie'], 'Stilton']
print(list_within_a_list)
print(type(list_within_a_list))
print(list_within_a_list[2])
print(list_within_a_list[1])
print(list_within_a_list[1][0])
print(list_within_a_list[1][1])

list_within_a_list[1][1] = 'Roquefort'
print(list_within_a_list)

print(list_within_a_list[-1])
print(list_within_a_list[-3])