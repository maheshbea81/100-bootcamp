import re

numbers = ['zero', 'wun', 'two', 'tree', 'fower', 'fife', 'six', 'seven', 'ait', 'niner']

alphas = ['alpha', 'bravo', 'charlie', 'delta', 'echo',
           'foxtrot', 'golf', 'hotel', 'india', 'juliet',
           'kilo', 'lima', 'mike', 'november', 'oscar', 'papa',
           'quebec', 'romeo', 'sierra', 'tango', 'uniform',
           'victor', 'whisky', 'xray', 'yankee', 'zulu']

# this is a dictionary comprehension (key is i, value is name)
codes = {str(i): name for i, name in enumerate(numbers)}
print("Number dictionary:")
print(codes)

# append alphabet to the number code
codes.update({name[0].upper(): name for name in alphas})

print("#" * 25)
print("Number and words dictionary:")
print(codes)

reg = 'WG07 OKD'

# substitute each word (letter), with a new value found by searching the key in the codes doct, from the reg string
result = re.sub(r'(\w)', lambda m: codes[m.groups()[0]]+' ', reg)
print("#" * 25)
print(reg)
print(result)
