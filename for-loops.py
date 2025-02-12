'''
1. 
'''


#For / For Else loops - executes a block of code a number of times, depending on the sequence it iterates on; the "else" clause is optional
vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]
 
for element in vendors: #interating over a sequence and executing the code indented under the "for" clause for each element in the sequence
    print(element)
else: #the indented code below "else" will be executed when "for" has finished looping over the entire list
    print("The end of the list has been reached")
    
#result of the above "for" block
Cisco
HP
Nortel
Avaya
Juniper
The end of the list has been reached


#If / For / While Nesting
x = "Cisco"
 
if "i" in x: 
    if len(x) > 3: #if nesting
        print(x, len(x))
 
Cisco 5 #result of the above block
 
list1 = [4, 5, 6]
list2 = [10, 20, 30]
for i in list1:
    for j in list2: #for nesting
        print(i*j)
 
40 80 120 50 100 150 60 120 180 #result of the above block
 
x = 1
while x <= 10:
    z = 5
    x += 1
    while z <= 10:  #while nesting
        print(z)
        z += 1
        
5 6 7 8 9 10 5 6 7 8 9 10 5 6 7 8 9 10 5 6 7 8 9 10 5 6 7 8 9 10 5 6 7 8 9 10 5 6 7 8 9 10 5 6 7 8 9 10 5 6 7 8 9 10 5 6 7 8 9 10	#result of the above block
 
for number in range(10):
    if 5 <= number <= 9: #mixed nesting
        print(number)
 
5 6 7 8 9 #result of the above block

