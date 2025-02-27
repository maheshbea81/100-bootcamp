'''
namespaces: 
1. builtin namespace: len, max, range, sort functions etc
2. global: all variables you define or import into your program, global variable. 
3. local: local variable, available within specific function. 
#Modules and importing - Basics
 
#Importing the sys module; the import statements should be placed before any other code in your application
import sys 
 
#Importing only a variable (pi) from the math module
from math import pi 
 
#Importing only a function (sin()) from the math module; there's no need to add the parentheses of the function when importing it
from math import sin 
 
#Importing all the names (variables and functions) from the math module
from math import * 
'''


The if __name__ == "__main__": block is a common construct used to define code that should only be executed when the script is run directly. This is useful for testing functions or running specific code blocks without unintended execution when the module is imported into another script.
Here's an example:
Python


def my_function():
    print("Function executed")

if __name__ == "__main__":
    print("Script executed directly")
    my_function()
If this script is run directly, the output will be:
Code

Script executed directly
Function executed
However, if this script is imported as a module into another script, the code within the if __name__ == "__main__": block will not be executed.
