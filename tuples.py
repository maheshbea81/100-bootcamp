'''
IMMUTABLE --> any datatype, that you cannot update(add/remove) after creation BUT can delete.
1. tuples are immutable, i.e cannot add/remove any elements. 
2. create tuple using tup=(), if there is only one element in tuple, you have to add , at the end of element, like tup=(9,) or tupl=('A',)
3. tuples supports indexing 
4. in comparision to frozen sets, frozensets are also immutable, but unique elements, whereas tuples doesn't have to be unique. 
5. variable mapping and unmapping, tupl=('ABC''DEF','FGI'), we can assign elements to variables using single line like this (a,b,c)=tupl, this will assign a='ABC',b='DEF and c='FGI'.
   this variable assignment works for lists,sets and strings ALSO. 
6. (a,b,c)=(1,2,3) is easy way of defining multiple variables, this also works for sets, strings and lists. 
7. a=(), b=[], if you want to know what builtin methods available for lists and tuples , use dir(a) or dir(b) will list ALL available methods. 
8. tuples and frozensets usually have less methods. 
9. len, min, max, tuple1+tuple2 and indexing works in tuples. 
10. my_tuple = (1,2,3,4) my_tuple[2]*4  will multiply ACTUAL element with 4, so ans would be 3*4=12, BUT
my_tuple = (1,2,'3',4) , my_tuple[2]*4 will give '3333'

'''

#Tuples - immutable lists (their contents cannot be changed by adding, removing or replacing elements)
my_tuple = () #creating an empty tuple
 
my_tuple = (9,) #creating a tuple with a single element; DO NOT forget the comma
 
my_tuple = (1, 2, 3, 4)
 
#Tuples - the same indexing & slicing rules apply as for strings and lists
len(my_tuple) #returns the number of elements in the tuple
 
my_tuple[0] #returns the first element in the tuple (index 0)
my_tuple[-1] #returns the last element in the tuple (index -1)
my_tuple[0:2] #returns (1, 2)
my_tuple[:2] #returns (1, 2)
my_tuple[1:] #returns (2, 3, 4)
my_tuple[:] #returns (1, 2, 3, 4)
my_tuple[:-2] #returns (1, 2)
my_tuple[-2:] #returns (3, 4)
my_tuple[::-1] #returns (4, 3, 2, 1)
my_tuple[::2] #returns (1, 3)
 
#Tuples - tuple assignment / packing and unpacking
tuple1 = ("Cisco", "2600", "12.4")
 
(vendor, model, ios) = tuple1 #vendor will be mapped to "Cisco" and so are the rest of the elements with their corresponding values; both tuples should have the same number of elements
 
(a, b, c) = (1, 2, 3) #assigning values in a tuple to variables in another tuple
 
min(tuple1) #returns "12.4"
 
max(tuple1) #returns "Cisco"
 
tuple1 + (5, 6, 7) #tuple concatenation
 
tuple1 * 20 #tuple multiplication
 
"2600" in tuple1 #returns True
 
784 not in tuple1 #returns True
 
del tuple1 #deleting a tuple
