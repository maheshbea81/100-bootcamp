 '''
1. min, max, len methods works on lists and any mutable (AKA editable/manipulative methods) will work on lists. 
2. 3 ways to remove an elemenet from list
    1. del list1[index]  --> this will remove index position from list1 variable. del list1 --> this will remove complete list1
    2. list1.pop(index) --> this will remove element at index position and give the output as this indexed/popped value, and original list is also editable. 
    3. list1.remove(ELEMENT)  --> this will remove ELEMENT itself from list1 variable.  use case: if you know what value you are going to remove, use remove method. 
3. list1.insert(index,'value')  --> this will insert (not update existing indexed position) value , list1[index]="value" --> this will update the existing value at indexed position. 
4. list1.extend(list2) --> this will add list2 elements to list1 at the end., will modify list1 and not list2, if you want both lists to be not modified,but still concatenante, use list1+list2
5. list1.index(value) --> returns indexed position for value.
6. list1.sort() --> this will sort elements of same data types, either strings or numbers in list, original list will be modified.
7. sorted(list1, reverse=True/False) --> this will sort and original list will not be modified
8.list1+list2 --> will concatenate list1 and list2, but original list1 and list2 will not be modified. 
9. list1.clear() will clear the list contents.
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


#Lists
list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]  #creating a list
 
len(list) #returns the number of elements in the list
 
list1[0] #returns "Cisco" which is the first element in the list (index 0)
 
list1[0] = "HP" #replacing the first element in the list with another value
 
#Lists - methods
list2 = [-11, 2, 12]
 
min(list2) #returns the smallest element (value) in the list
 
max(list2) #returns the largest element (value) in the list
 
list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]
 
list1.append(100) #appending a new element to the list
 
del list1[4] #removing an element from the list by index
 
list1.pop(0) #removing an element from the list by index
 
list1.remove("HP") #removing an element from the list by value
 
list1.insert(2, "Nortel") #inserting an element at a particular index
 
list1.extend(list2) #appending a list to another list
 
list1.index(-11) #returns the index of element -11
 
list1.count(10) #returns the number of times element 10 is in the list
 
list2 = [9, 99, 999, 1, 25, 500]
 
list2.sort() #sorts the list elements in ascending order; modifies the list in place
 
list2.reverse() #reverses the elements of the list
 
sorted(list2) #sorts the elements of a list in ascending order and creates a new list at the same time
 
sorted(list2, reverse = True) #sorts the elements of a list in descending order and creates a new list at the same time
 
list1 + list2 #concatenating two lists
 
list1 * 3 #repetition of a list
 
#Lists - slicing (works the same as string slicing, but with list elements instead of string characters)
a_list[5:15] #slice starting at index 5 up to, but NOT including, index 15; so index 14 represents the last element in the slice
a_list[5:] #slice starting at index 5 up to the end of the list
a_list[:10] #slice starting at the beginning of the list up to, but NOT including, index 10
a_list[:] #returns the entire list
a_list[-1] #returns the last element in the list
a_list[-2] #returns the second to last element in the list
a_list[-9:-1] #extracts a certain sublist using negative indexes
a_list[-5:] #returns the last 5 elements in the list
a_list[:-5] #returns the list minus its last 5 elements
a_list[::2] #adds a third element called step; skips every second element of the list
a_list[::-1] #returns a_list's elements in reverse order
print(fruits)  # Output: ["apple", "banana", "cherry", "orange"]

numbers.reverse()
print(numbers)  # Output: [5, 4, 3, 10, 1]

print(len(mixed_list))  # Output: 4




-----Test
