'''
1. sets are unordered (unsorted), mutable, unique lists, denoted with {}
2. sets are created using set function or elements in {}
3. set1.add(16) , will insert 16 to set1 , len(set1) will give length
4. set1.clear() --> will delete all elements in set
5. set1.intersection(set2), set1.difference(set2), set1.union(set2) --> will give intersection, difference and union of two sets.
6. frozensets are nothing more than immutable sets, can be created using frozeset function
7. frozenset.add/remove/pop/clear() methods wont work on frozensets , because fs are immutable, however, intersections, union etc will work. 
8. fs1.pop() will remove FIRST element from set, whereas list1.pop() will remove LAST element from list. 
9. 
'''


# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Creating a set from a list
my_list = [1, 2, 2, 3, 4, 4, 5]
my_set = set(my_list)
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Adding elements to a set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Removing elements from a set
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5, 6}
print(set1 | set2)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection
print(set1.intersection(set2))  # Output: {3, 4}
print(set1 & set2)  # Output: {3, 4}

# Difference
print(set1.difference(set2))  # Output: {1, 2}
print(set1 - set2)  # Output: {1, 2}

# Symmetric difference
print(set1.symmetric_difference(set2))  # Output: {1, 2, 5, 6}
print(set1 ^ set2)  # Output: {1, 2, 5, 6}

# Checking if an element is in a set
print(2 in set1)  # Output: True
print(7 in set1)  # Output: False




#Sets - unordered collections of unique elements
set1 = {"1.1.1.1", "2.2.2.2", "3.3.3.3", "4.4.4.4"} #creating a set
 
list1 = [11, 12, 13, 14, 15, 15, 15, 11]
string1 = "aaabcdeeefgg"
 
set1 = set(list1) #creating a set from a list; removing duplicate elements; returns {11, 12, 13, 14, 15}
 
set2 = set(string1) #creating a set from a string; removing duplicate characters; returns {'b', 'a', 'g', 'f', 'c', 'd', 'e'}; remeber that sets are UNORDERED collections of elements
 
len(set1) #returns the number of elements in the set
 
11 in set1 #returns True; checking if a value is an element of a set
 
10 not in set 1 #returns True; checking if a value is an element of a set
 
set1.add(16) #adding an element to a set
 
set1.remove(16) #removing an element from a set
 
#Frozensets - immutable sets. The elements of a frozenset remain the same after creation.
fs1 = frozenset(list1) #defining a frozenset
 
fs1
frozenset({11, 12, 13, 14, 15}) #the result
 
type(fs1)
<class 'frozenset'> #the result
 
#proving that frozensets are indeed immutable
fs1.add(10)
AttributeError: 'frozenset' object has no attribute 'add'
 
fs1.remove(1)
AttributeError: 'frozenset' object has no attribute 'remove'
 
fs1.pop()
AttributeError: 'frozenset' object has no attribute 'pop'
 
fs1.clear()
AttributeError: 'frozenset' object has no attribute 'clear'
 
#Sets - methods
set1.intersection(set2) #returns the common elements of the two sets
 
set1.difference(set2) #returns the elements that set1 has and set2 doesn't
 
set1.union(set2) #unifying two sets; the result is also a set, so there are no duplicate elements; not to be confused with concatenation
 
set1.pop() #removes a random element from the set; set elements cannot be removed by index because sets are UNORDERED collections of elements, so there are no indexes to use
 
set1.clear() #clearing a set; the result is an empty set
