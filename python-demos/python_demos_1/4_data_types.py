number = 3.142
print(type(number))

hex_number = 0x3f
print(type(hex_number))

int_number = 42
print(type(int_number))

# bytes and strings
# 00000000
# 11111111
# 00000001
# 00000010
# 00000011
# 1
# 2
# 4
# 8
# 16
# 32
# 64
# 128
# 256
# 512
# 1026

byte_string = b'hello'
print(byte_string)
print(type(byte_string))

# unicode string
string_string = 'hello'
print(string_string)
print(type(string_string))

# collection types
# tuples vs lists
# immutable - mutable
name_tuple = 'Weronika', 'Ismail', 'Nathan'
print(name_tuple)
print(type(name_tuple))

thing = 'Alex',
print(thing)
print(type(thing))

thing = 'Dom'
print(thing)
print(type(thing))

name_list = ['Kamil', 'Prakash']
print(name_list)
print(type(name_list))
name_list.append('James')
print(name_list)

# dictionaries and sets
books = {'ISBN1': 'Gone with the Wind', 'ISBN2': 'War and Peace'}
print(books)

# subscript notation [n]
print(name_list[0])
print(name_list[1])
print(name_list[2])
name_list.append('Nihal')
print(name_list[3])

print(name_tuple)
print(name_tuple[1])

print(books['ISBN1'])
print(books['ISBN2'])
print(books)


# set
# unique - no duplicates
name_set = {'Dave', 'Julie', 'Bob', 'Dave', 'Sarah'}
print(name_set)
print(type(name_set))
# print(name_set[0])


print(name_tuple)
print(name_tuple[-1])
# name_tuple[-1] = 'Alex'

another_tuple = ('one', 'two', ['nine', 'ten'])
print(another_tuple)
# another_tuple[0] = 'zero'
print(another_tuple[2])
another_tuple[2][0] = 'eleven'
print(another_tuple)


print(books)
print(books['ISBN2'])
books['ISBN3'] = 'Another book title'
print(books)
