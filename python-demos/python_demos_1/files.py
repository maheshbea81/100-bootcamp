'''
#Files - opening and reading a file in the same directory/folder
myfile = open("routers.txt", "r") #"r" is the file access mode for reading and it is the default mode when opening a file
 
#Files - opening and reading a file in another directory/folder on Windows
myfile = open("C:\\Users\\john\\routers.txt", "r") #"r" is the file access mode for reading and it is the default mode when opening a file
 
myfile.mode #checking the mode in which a file has been opened
 
myfile.read() #method that returns the entire content of a file in the form of a string
 
myfile.read(5) #returning only the first 5 characters (bytes) in the file
 
myfile.seek(0) #moving the cursor at the beginning of the file
 
myfile.tell() #checking the current position of the cursor inside the file
 
myfile.readline() #returns the file content one line a ta time, each time you use the method
 
myfile.readlines() #returns a list where each element is a line in the file
 
#Files - writing and appending to a file
newfile = open("newfile.txt", "w") #opens/creates a new file for writing; the "w" method also creates the file for writing if the file doesn’t exist and overrides the file if the file already exists; remember to close the file after writing to it to save the changes!
 
newfile.writelines(["Cisco", "Juniper", "HP", "\n"]) #this method takes a sequence of strings as an argument and writes those strings to the file
 
newfile = open("newfile.txt", "a") #opening a file for appending
 
newfile = open("newfile.txt", "w+") #opens a file for both writing and reading at the same time
 
newfile = open("newfile.txt", "x") #opens for exclusive creation, failing if the file already exists
 
#Files - closing a file
newfile.closed #checking if a file is closed
 
newfile.close() #closing a file
 
with open("python.txt", "w") as f: #using the with-as solution, the files gets closed automatically, without needing the close() method
    f.write("Hello Python!\n")
    r -- 
	1.Can read
	2.Can not write
r+ -- 
	1.Can write if file exist
	2.If file does not exist then it will trough error while opening
	3.We have to use seek to read the file from the beginning, if we dont want to close
w --
	1.If file does not exist it wont throw error and it will create the file
	2.Everytime it ill override previous content
	3.We cant read the file, until we close and open in r or r+ 
w+ --
	1. We can read only if we are writing something
	2. If we want to read, we need not to
'''

with open(r'/Users/maheshwarvavilla/my_file.txt', "w+") as file:
    file.write("Hello, world!\n")
    file.seek(0)  # Reset the file pointer to the beginning
    content = file.read()
    print(content)
# Output: Hello, world!


myfile = open("myfile.txt", "w")
myfile.write("Python\nJava\nJavascript\nC++\nHTML\nCSS\nSwift")
myfile.close()
myfile = open("myfile.txt")
#This should return "Javascript"
print(myfile.readlines()[2])



myfile = open("myfile2.txt", "w")
myfile.write("Python\nJava\nJavascript\nC++\nHTML\nCSS\nSwift\n")
myfile.close()
myfile = open("myfile2.txt", "a+")
myfile.write("Ruby")
myfile.seek(0)
#This should return "Ruby"
print(myfile.readlines()[-1])
