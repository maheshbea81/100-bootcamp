'''
1. use FOR loop when we are iterating in a collection eg, range, list, set of items.
2. use WHILE loop when we have to evaluate a condition or an expression. 
3. break, continue are for FOR and WHILE loops only and not for if/else's. 
4.break will stop checking further in the current loop (collections(ranges,lists etc) for FOR loops, and conditions for WHILE loops). 
5. continue will stop executing stmts below condition but will continue with loop/next iteration. 
6. pass is basically a place holder to write code later in loop without getting an error (EOF error). 
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



#Break, Continue, Pass
list1 = [4, 5, 6]
list2 = [10, 20, 30]
 
for i in list1:
    for j in list2:
        if j == 20:
            break #stops the execution here, ignores the print statement below and completely quits THIS "for" loop; however, it doesn't quit the outer "for" loop, too!
        print(i * j)
    print("Outside the nested loop")
    
#result of the above block
40
Outside the nested loop
50
Outside the nested loop
60
Outside the nested loop
 
list1 = [4, 5, 6]
list2 = [10, 20, 30]
 
for i in list1:
    for j in list2:
        if j == 20:
            continue #ignores the rest of the code below for the current iteration, then goes up to the top of the loop (inner "for") and starts the next iteration
        print(i * j)
    print("Outside the nested loop")
 
#result of the above block
40
120
Outside the nested loop
50
150
Outside the nested loop
60
180
Outside the nested loop
 
for i in range(10):
    pass #pass is the equivalent of "do nothing"; it is actually a placeholder for when you just want to write a piece of code that you will treat later


#Try / Except / Else / Finally - handling an exception when it occurs and telling Python to keep executing the rest of the lines of code in the program
try:
    print(4/0) #in the "try" clause you insert the code that you think might generate an exception at some point
except ZeroDivisionError:
    print("Division Error!") #specifying what exception types Python should expect as a consequence of running the code inside the "try" block and how to handle them
else:
    print("No exceptions raised by the try block!") #executed if the code inside the "try" block raises NO exceptions
finally:
    print("I don't care if an exception was raised or not!") #executed whether the code inside the "try" block raises an exception or not
 
#result of the above block
Division Error!
I don't care if an exception was raised or not!
