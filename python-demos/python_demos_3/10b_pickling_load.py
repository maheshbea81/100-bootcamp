import pickle

inp = open('capitals.p', 'rb')
caps = pickle.load(inp)
inp.close()

print(caps)

# shows which version of the pickle protocol is being used
print(pickle.DEFAULT_PROTOCOL)