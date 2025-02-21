# run with hi and hello then done
# run again with hi then bye

import sys

line = None

while line != 'done':
    line = input("Enter a message to echo or type 'done' to complete: ")
    print('<', line, '>')
    if line == 'bye':
        sys.exit("Goodbye")

print("Program continues from here...")